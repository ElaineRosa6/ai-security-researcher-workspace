"""
LLM Client - AI推理核心模块
支持 OpenAI, Claude 和本地模型
"""
import os
import logging
from typing import Dict, List, Optional, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass
import json

logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    content: str
    model: str
    tokens_used: int = 0
    finish_reason: str = "stop"
    metadata: Optional[Dict[str, Any]] = None


class BaseLLMProvider(ABC):
    @abstractmethod
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> LLMResponse:
        pass


class OpenAIProvider(BaseLLMProvider):
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        try:
            import openai
        except ImportError:
            raise ImportError("Please install openai: pip install openai")
        
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        self.model = model
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> LLMResponse:
        logger.debug(f"Calling OpenAI model {self.model}")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=kwargs.get("temperature", 0.7),
            max_tokens=kwargs.get("max_tokens", 2048)
        )
        
        return LLMResponse(
            content=response.choices[0].message.content,
            model=self.model,
            tokens_used=response.usage.total_tokens if response.usage else 0,
            finish_reason=response.choices[0].finish_reason
        )


class AnthropicProvider(BaseLLMProvider):
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-opus-20240229"):
        try:
            import anthropic
        except ImportError:
            raise ImportError("Please install anthropic: pip install anthropic")
        
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key is required. Set ANTHROPIC_API_KEY environment variable or pass api_key parameter.")
        self.model = model
        self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> LLMResponse:
        logger.debug(f"Calling Anthropic model {self.model}")
        
        system_msg = [m for m in messages if m["role"] == "system"]
        other_msg = [m for m in messages if m["role"] != "system"]
        
        system_prompt = system_msg[0]["content"] if system_msg else ""
        
        response = self.client.messages.create(
            model=self.model,
            system=system_prompt,
            messages=other_msg,
            temperature=kwargs.get("temperature", 0.7),
            max_tokens=kwargs.get("max_tokens", 2048)
        )
        
        return LLMResponse(
            content=response.content[0].text,
            model=self.model,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens
        )


class MockProvider(BaseLLMProvider):
    """Mock provider for testing without real LLM API keys"""
    def __init__(self, model: str = "mock-model"):
        self.model = model
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> LLMResponse:
        logger.warning("Using Mock LLM Provider - responses may be mocked")
        
        last_msg = messages[-1]["content"] if messages else ""
        
        return LLMResponse(
            content=f"[Mock LLM Response] Received: {last_msg[:50]}...",
            model=self.model,
            tokens_used=0
        )


class LLMClient:
    """统一的 LLM 客户端
    支持多种后端: OpenAI, Anthropic, Mock (测试用)
    """
    
    PROVIDERS = {
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
        "mock": MockProvider
    }
    
    def __init__(
        self,
        provider: str = "mock",
        model: Optional[str] = None,
        **kwargs
    ):
        self.provider_name = provider
        self.provider_class = self.PROVIDERS.get(provider, MockProvider)
        self._provider = self.provider_class(model=model, **kwargs)
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> LLMResponse:
        """发送聊天请求
        
        Args:
            messages: 消息列表 [{"role": "user/system/assistant", "content": "..."}]
            system_prompt: 可选的系统提示词
        """
        all_messages = messages.copy()
        
        if system_prompt:
            all_messages.insert(0, {"role": "system", "content": system_prompt})
        
        try:
            response = self._provider.chat(all_messages, **kwargs)
            logger.debug(f"Got LLM call succeeded, model: {response.model}")
            return response
        except Exception as e:
            logger.error(f"LLM call failed: {e}")
            return LLMResponse(
                content=f"[Error] Failed to call LLM: {str(e)}",
                model="error"
            )
    
    def ask(
        self,
        user_prompt: str,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        """简化的接口：单条消息对话"""
        messages = [{"role": "user", "content": user_prompt}]
        response = self.chat(messages, system_prompt=system_prompt, **kwargs)
        return response.content
    
    def try_parse_json(self, text: str) -> Dict[str, Any]:
        """尝试从LLM返回的内容里解析JSON"""
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            json_match = text.strip()
            if "{" in json_match and "}" in json_match:
                start = json_match.find("{")
                end = json_match.rfind("}") + 1
                try:
                    return json.loads(json_match[start:end])
                except:
                    pass
            return {"raw": text}
