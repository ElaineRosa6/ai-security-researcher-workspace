"""
Skills Manager - 技能管理模块
"""
import logging
import sys
import os
from typing import Dict, Any

logger = logging.getLogger(__name__)


class SkillsManager:
    """技能管理器 - 负责加载和注册所有技能"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.skills: Dict[str, Any] = {}
        
        # Add ai-agent directory to path (handle hyphen vs underscore)
        parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        ai_agent_dir = os.path.join(parent_dir, 'ai-agent')
        if ai_agent_dir not in sys.path:
            sys.path.insert(0, ai_agent_dir)
    
    def register_all(self, brain):
        """注册所有可用的技能到 Brain"""
        logger.info("Registering all skills...")
        
        # Red Team Skills
        self._register_web_security_skill(brain)
        
        # Register more skills as needed
        logger.info(f"Registered {len(self.skills)} skills")
    
    def _register_web_security_skill(self, brain):
        """注册 Web 安全技能"""
        try:
            from red_team.web_security import WebSecuritySkill
            skill = WebSecuritySkill(self.config)
            brain.register_skill("WebSecuritySkill", skill)
            self.skills["WebSecuritySkill"] = skill
            logger.info("Registered WebSecuritySkill")
        except Exception as e:
            logger.warning(f"Failed to register WebSecuritySkill: {e}")
            # Try alternative import
            try:
                import importlib.util
                import os
                file_path = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                    'ai-agent', 'skills', 'red_team', 'web_security.py'
                )
                spec = importlib.util.spec_from_file_location("web_security", file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                skill = module.WebSecuritySkill(self.config)
                brain.register_skill("WebSecuritySkill", skill)
                self.skills["WebSecuritySkill"] = skill
                logger.info("Registered WebSecuritySkill (direct import)")
            except Exception as e2:
                logger.warning(f"Alternative import also failed: {e2}")
    
    def get_skill(self, name):
        """获取已注册的技能"""
        return self.skills.get(name)
