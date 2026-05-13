"""
Harness Integration - 将 Harness 框架与 Agent 集成
"""
import logging
import os
from typing import Dict, Any

logger = logging.getLogger(__name__)


class HarnessManager:
    """Harness 管理器 - 统一管理所有 Harness"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.harnesses: Dict[str, Any] = {}
        
        # 加载所有 Harness
        self._load_harnesses()
    
    def _load_harnesses(self):
        """加载所有可用的 Harness"""
        parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        harness_path = os.path.join(parent_dir, 'ai-agent', 'harness', 'harness.py')
        
        if not os.path.exists(harness_path):
            logger.warning(f"Harness file not found: {harness_path}")
            return
        
        import importlib.util
        spec = importlib.util.spec_from_file_location("harness_module", harness_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # 收集所有 Harness 类
            harness_classes = [
                'WebSecurityHarness',
                'BinaryHarness',
                'DomainPentestHarness',
                'IncidentResponseHarness',
                'ForensicsHarness',
                'AnonymityHarness',
                'ComplianceHarness',
                'SessionHarness',
                'GenericHarness'
            ]
            
            for class_name in harness_classes:
                if hasattr(module, class_name):
                    self.harnesses[class_name] = getattr(module, class_name)
                    logger.info(f"Loaded harness: {class_name}")
    
    def get_harness(self, name: str):
        """获取指定类型的 Harness 实例"""
        harness_class = self.harnesses.get(name)
        if harness_class:
            return harness_class(self.config)
        return None
    
    def list_harnesses(self):
        """列出所有可用的 Harness"""
        return list(self.harnesses.keys())
