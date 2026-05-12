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
        
        # Add parent directory to path
        parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Add both possible paths for ai-agent directory
        ai_agent_path = os.path.join(parent_dir, 'ai-agent')
        if os.path.exists(ai_agent_path) and ai_agent_path not in sys.path:
            sys.path.insert(0, parent_dir)
    
    def register_all(self, brain):
        """注册所有可用的技能到 Brain"""
        logger.info("Registering all skills...")
        
        # Red Team Skills
        self._register_web_security_skill(brain)
        self._register_domain_pentest_skill(brain)
        
        # Blue Team Skills
        self._register_incident_response_skill(brain)
        self._register_threat_intel_skill(brain)
        
        # Purple Team Skills
        self._register_forensics_skill(brain)
        
        # Compliance Skills
        self._register_compliance_skill(brain)
        
        # General Skills
        self._register_general_skill(brain)
        
        logger.info(f"Registered {len(self.skills)} skills: {list(self.skills.keys())}")
    
    def _load_skill_file(self, relative_path: str, class_name: str):
        """直接加载技能文件"""
        parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(parent_dir, 'ai-agent', 'skills', relative_path + '.py')
        
        if not os.path.exists(file_path):
            logger.warning(f"Skill file not found: {file_path}")
            return None
        
        import importlib.util
        spec = importlib.util.spec_from_file_location(class_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, class_name):
                return getattr(module, class_name)(self.config)
        
        return None
    
    def _register_web_security_skill(self, brain):
        """注册 Web 安全技能"""
        skill_class = self._load_skill_file("red_team/web_security", "WebSecuritySkill")
        if skill_class:
            brain.register_skill("WebSecuritySkill", skill_class)
            self.skills["WebSecuritySkill"] = skill_class
    
    def _register_domain_pentest_skill(self, brain):
        """注册域渗透测试技能"""
        skill_class = self._load_skill_file("red_team/domain_pentest", "DomainPentestSkill")
        if skill_class:
            brain.register_skill("DomainPentestSkill", skill_class)
            self.skills["DomainPentestSkill"] = skill_class
    
    def _register_incident_response_skill(self, brain):
        """注册事件响应技能"""
        skill_class = self._load_skill_file("blue_team/incident_response", "IncidentResponseSkill")
        if skill_class:
            brain.register_skill("IncidentResponseSkill", skill_class)
            self.skills["IncidentResponseSkill"] = skill_class
    
    def _register_threat_intel_skill(self, brain):
        """注册威胁情报技能"""
        skill_class = self._load_skill_file("blue_team/threat_intel", "ThreatIntelSkill")
        if skill_class:
            brain.register_skill("ThreatIntelSkill", skill_class)
            self.skills["ThreatIntelSkill"] = skill_class
    
    def _register_forensics_skill(self, brain):
        """注册取证技能"""
        skill_class = self._load_skill_file("purple_team/forensics", "ForensicsSkill")
        if skill_class:
            brain.register_skill("ForensicsSkill", skill_class)
            self.skills["ForensicsSkill"] = skill_class
    
    def _register_compliance_skill(self, brain):
        """注册合规技能"""
        skill_class = self._load_skill_file("compliance/compliance", "ComplianceSkill")
        if skill_class:
            brain.register_skill("ComplianceSkill", skill_class)
            self.skills["ComplianceSkill"] = skill_class
    
    def _register_general_skill(self, brain):
        """注册通用技能"""
        skill_class = self._load_skill_file("general/general", "GeneralSkill")
        if skill_class:
            brain.register_skill("GeneralSkill", skill_class)
            self.skills["GeneralSkill"] = skill_class
    
    def get_skill(self, name):
        """获取已注册的技能"""
        return self.skills.get(name)
