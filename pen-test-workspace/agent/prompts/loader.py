"""
Prompt Loader - 提示词加载和管理
"""
import os
import logging
from typing import Dict, Optional, Any
from pathlib import Path
from jinja2 import Template

logger = logging.getLogger(__name__)


class PromptLoader:
    """提示词加载器"""
    
    def __init__(self, prompts_dir: Optional[str] = None):
        if prompts_dir is None:
            self.prompts_dir = Path(__file__).parent
        else:
            self.prompts_dir = Path(prompts_dir)
        
        self._prompts: Dict[str, str] = {}
        self._load_from_dir(self.prompts_dir)
    
    def _load_from_dir(self, base_dir: Path):
        """从目录加载所有.md文件"""
        for root, _, files in os.walk(base_dir):
            for file_name in files:
                if file_name.endswith(".md"):
                    try:
                        with open(Path(root)/file_name, 'r', encoding='utf-8') as f:
                            name = Path(file_name).stem
                            self._prompts[name] = f.read()
                            logger.debug(f"Loaded prompt: {name}")
                    except Exception as e:
                        logger.warning(f"Failed to load {file_name}: {e}")
    
    def get(self, name: str) -> Optional[str]:
        """获取提示词"""
        return self._prompts.get(name)
    
    def render(self, name: str, **kwargs) -> Optional[str]:
        """渲染模板"""
        raw = self.get(name)
        if not raw:
            return None
        return Template(raw).render(**kwargs)
