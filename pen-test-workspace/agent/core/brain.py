"""
Agent Brain - Intelligent Decision Center
Handles planning, reasoning, and decision making
"""

import json
import logging
import re
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class Brain:
    """Central intelligence module for the agent"""
    
    def __init__(
        self,
        memory: Any,
        knowledge: Any,
        state_tracker: Any,
        llm: Optional[Any] = None,
        prompt_loader: Optional[Any] = None
    ):
        self.memory = memory
        self.knowledge = knowledge
        self.state_tracker = state_tracker
        self.skills_registry = {}
        self.llm = llm
        self.prompt_loader = prompt_loader
        
    def register_skill(self, name: str, skill_instance: Any) -> None:
        """Register a skill in the brain"""
        self.skills_registry[name] = skill_instance
        logger.info(f"Registered skill: {name}")
        
    def set_llm(self, llm):
        """Set LLM client"""
        self.llm = llm
        
    def set_prompt_loader(self, prompt_loader):
        """Set prompt loader"""
        self.prompt_loader = prompt_loader
        
    def _ask_llm(self, user_prompt, system_prompt=None):
        """Helper method to use LLM with fallbacks"""
        if self.llm:
            try:
                return self.llm.ask(user_prompt, system_prompt=system_prompt)
            except Exception as e:
                logger.warning(f"LLM query failed: {e}, falling back to rules")
        return None
    
    def parse_requirement(self, requirement_text: str) -> Dict[str, Any]:
        """Parse user requirement into structured format"""
        if not requirement_text or not isinstance(requirement_text, str):
            raise ValueError("Requirement text must be a non-empty string")
        
        logger.info(f"Parsing requirement: {requirement_text}")
        
        requirement = {
            "raw_text": requirement_text,
            "timestamp": datetime.now().isoformat(),
            "task_type": self._identify_task_type(requirement_text),
            "target": self._extract_target(requirement_text),
            "scope": self._extract_scope(requirement_text),
            "constraints": self._extract_constraints(requirement_text),
            "objectives": self._extract_objectives(requirement_text),
            "deliverables": self._determine_deliverables()
        }
        
        self.state_tracker.update_context("requirement", requirement)
        
        return requirement
    
    def _identify_task_type(self, text: str) -> str:
        """Identify the type of security task"""
        text_lower = text.lower()
        
        if any(kw in text_lower for kw in ['pentest', 'penetration test', '渗透测试']):
            return 'pentest'
        elif any(kw in text_lower for kw in ['incident', '应急响应', 'breach']):
            return 'incident_response'
        elif any(kw in text_lower for kw in ['vulnerability', '漏洞', 'scan']):
            return 'vulnerability_assessment'
        elif any(kw in text_lower for kw in ['audit', '审计']):
            return 'security_audit'
        elif any(kw in text_lower for kw in ['forensic', '取证', 'investigation']):
            return 'forensics'
        else:
            return 'general_security'
    
    def _extract_target(self, text: str) -> Dict[str, Any]:
        """Extract target information from requirement"""
        target = {
            "type": "unknown",
            "value": None
        }
        
        if 'http' in text.lower() or 'www.' in text.lower():
            target['type'] = 'web'
            url_match = re.search(r'https?://[^\s]+', text)
            if url_match:
                target['value'] = url_match.group()
        elif any(kw in text.lower() for kw in ['domain', '域', 'ad ', 'active directory']):
            target['type'] = 'domain'
            domain_match = re.search(r'[\w.-]+\.[\w]+', text)
            if domain_match:
                target['value'] = domain_match.group()
        elif any(kw in text.lower() for kw in ['ip', '主机', 'host']):
            target['type'] = 'host'
            ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
            if ip_match:
                target['value'] = ip_match.group()
        
        return target
    
    def _extract_scope(self, text: str) -> List[str]:
        """Extract testing scope"""
        scope = []
        
        text_lower = text.lower()
        
        scope_mapping = {
            'web': ['web', '网站', 'web application', 'web应用'],
            'api': ['api', 'rest', 'graphql'],
            'network': ['network', '网络', 'port'],
            'mobile': ['mobile', '移动', 'android', 'ios', 'app'],
            'infrastructure': ['infrastructure', '基础设施', 'cloud', '云']
        }
        
        for scope_type, keywords in scope_mapping.items():
            if any(kw in text_lower for kw in keywords):
                scope.append(scope_type)
        
        if not scope:
            scope = ['full']
        
        return scope
    
    def _extract_constraints(self, text: str) -> Dict[str, Any]:
        """Extract constraints from requirement"""
        constraints = {
            "time_limited": False,
            "passive_only": False,
            "no_exploit": False
        }
        
        text_lower = text.lower()
        
        if any(kw in text_lower for kw in ['passive', '只做', '信息收集']):
            constraints['passive_only'] = True
        if any(kw in text_lower for kw in ['no exploit', '不利用', '不攻击']):
            constraints['no_exploit'] = True
        if any(kw in text_lower for kw in ['time', '时间', '限时']):
            constraints['time_limited'] = True
        
        return constraints
    
    def _extract_objectives(self, text: str) -> List[str]:
        """Extract testing objectives"""
        objectives = []
        
        text_lower = text.lower()
        
        if any(kw in text_lower for kw in ['vulnerability', '漏洞', 'find']):
            objectives.append('identify_vulnerabilities')
        if any(kw in text_lower for kw in ['exploit', '利用']):
            objectives.append('exploit_vulnerabilities')
        if any(kw in text_lower for kw in ['access', '权限', 'get access']):
            objectives.append('gain_access')
        if any(kw in text_lower for kw in ['data', '数据', 'sensitive']):
            objectives.append('access_sensitive_data')
        if any(kw in text_lower for kw in ['report', '报告']):
            objectives.append('generate_report')
        
        if not objectives:
            objectives = ['comprehensive_assessment']
        
        return objectives
    
    def _determine_deliverables(self) -> List[str]:
        """Determine expected deliverables"""
        return [
            'executive_summary',
            'technical_report',
            'findings_list',
            'evidence_attachments',
            'recommendations'
        ]
    
    def create_task_plan(self, requirement: Dict[str, Any]) -> Dict[str, Any]:
        """Create a detailed task plan based on requirement"""
        logger.info("Creating task plan")
        
        task_type = requirement.get('task_type')
        target = requirement.get('target')
        scope = requirement.get('scope', [])
        
        phases = []
        
        phases.append({
            "name": "reconnaissance",
            "description": "Information gathering and reconnaissance",
            "tasks": self._create_recon_tasks(target)
        })
        
        phases.append({
            "name": "scanning",
            "description": "Port and service scanning",
            "tasks": self._create_scan_tasks(target, scope)
        })
        
        if task_type in ['pentest', 'vulnerability_assessment']:
            phases.append({
                "name": "vulnerability_assessment",
                "description": "Vulnerability identification and assessment",
                "tasks": self._create_vuln_tasks(scope)
            })
            
            if not requirement.get('constraints', {}).get('no_exploit'):
                phases.append({
                    "name": "exploitation",
                    "description": "Vulnerability exploitation",
                    "tasks": self._create_exploit_tasks()
                })
                
                phases.append({
                    "name": "post_exploitation",
                    "description": "Post-exploitation activities",
                    "tasks": self._create_post_exp_tasks()
                })
        
        phases.append({
            "name": "reporting",
            "description": "Report generation",
            "tasks": self._create_report_tasks()
        })
        
        plan = {
            "requirement": requirement,
            "phases": phases,
            "created_at": datetime.now().isoformat(),
            "estimated_phases": len(phases)
        }
        
        self.state_tracker.update_context("current_plan", plan)
        
        return plan
    
    def _create_recon_tasks(self, target: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create reconnaissance tasks"""
        tasks = []
        
        target_type = target.get('type')
        target_value = target.get('value')
        
        if target_type == 'web':
            tasks.append({
                "id": "recon_web_discovery",
                "name": "Web Discovery",
                "skill": "WebSecuritySkill.recon",
                "params": {"target": target_value}
            })
            tasks.append({
                "id": "recon_subdomain",
                "name": "Subdomain Enumeration",
                "skill": "WebSecuritySkill.subdomain_enum",
                "params": {"target": target_value}
            })
        
        tasks.append({
            "id": "recon_osint",
            "name": "OSINT Information Gathering",
            "skill": "GeneralSkill.osint",
            "params": {"target": target_value}
        })
        
        return tasks
    
    def _create_scan_tasks(self, target: Dict[str, Any], scope: List[str]) -> List[Dict[str, Any]]:
        """Create scanning tasks"""
        tasks = []
        
        target_value = target.get('value')
        
        tasks.append({
            "id": "scan_nmap",
            "name": "Nmap Port Scan",
            "skill": "GeneralSkill.nmap_scan",
            "params": {"target": target_value, "flags": "-sV -sC -p-"}
        })
        
        if 'web' in scope:
            tasks.append({
                "id": "scan_web_enum",
                "name": "Web Enumeration",
                "skill": "WebSecuritySkill.enumerate",
                "params": {"target": target_value}
            })
        
        return tasks
    
    def _create_vuln_tasks(self, scope: List[str]) -> List[Dict[str, Any]]:
        """Create vulnerability assessment tasks"""
        tasks = []
        
        if 'web' in scope:
            tasks.append({
                "id": "vuln_web_test",
                "name": "Web Vulnerability Testing",
                "skill": "WebSecuritySkill.test_vulnerabilities",
                "params": {}
            })
        
        tasks.append({
            "id": "vuln_nuclei",
            "name": "Template-based Vulnerability Scan",
            "skill": "GeneralSkill.nuclei_scan",
            "params": {}
        })
        
        return tasks
    
    def _create_exploit_tasks(self) -> List[Dict[str, Any]]:
        """Create exploitation tasks"""
        tasks = []
        
        tasks.append({
            "id": "exp_validate",
            "name": "Validate Exploitable Vulnerabilities",
            "skill": "WebSecuritySkill.validate_exploitable",
            "params": {}
        })
        
        tasks.append({
            "id": "exp_execute",
            "name": "Execute Exploitation",
            "skill": "WebSecuritySkill.exploit",
            "params": {}
        })
        
        return tasks
    
    def _create_post_exp_tasks(self) -> List[Dict[str, Any]]:
        """Create post-exploitation tasks"""
        tasks = []
        
        tasks.append({
            "id": "post_priv_esc",
            "name": "Privilege Escalation",
            "skill": "DomainPentestSkill.privilege_escalation",
            "params": {}
        })
        
        tasks.append({
            "id": "post_lateral",
            "name": "Lateral Movement",
            "skill": "DomainPentestSkill.lateral_movement",
            "params": {}
        })
        
        tasks.append({
            "id": "post_collect",
            "name": "Data Collection",
            "skill": "DomainPentestSkill.collect_data",
            "params": {}
        })
        
        return tasks
    
    def _create_report_tasks(self) -> List[Dict[str, Any]]:
        """Create reporting tasks"""
        return [{
            "id": "report_generate",
            "name": "Generate Report",
            "skill": "GeneralSkill.generate_pentest_report",
            "params": {}
        }]
    
    def execute_skill(self, skill_name: str, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a registered skill"""
        if '.' in skill_name:
            parts = skill_name.split('.')
            skill_module = parts[0]
            skill_method = parts[1]
            
            if skill_module in self.skills_registry:
                skill = self.skills_registry[skill_module]
                if hasattr(skill, skill_method):
                    method = getattr(skill, skill_method)
                    try:
                        result = method(**task.get('params', {}))
                        return result
                    except Exception as e:
                        logger.error(f"Skill execution failed: {e}")
                        return {"status": "error", "reason": str(e)}
                else:
                    logger.warning(f"Method {skill_method} not found in skill {skill_module}")
                    return {"status": "skipped", "reason": f"Method {skill_method} not found"}
            else:
                logger.warning(f"Skill {skill_module} not registered")
                return {"status": "skipped", "reason": f"Skill {skill_module} not registered"}
        
        logger.warning(f"Invalid skill name format: {skill_name}")
        return {"status": "skipped", "reason": f"Invalid skill name format: {skill_name}"}
    
    def decide_next_action(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Decide next action based on current context"""
        current_state = self.state_tracker.get_current_state()
        discoveries = self.memory.retrieve("medium_term").get('discoveries', [])
        
        if current_state == "RECON":
            if len(discoveries) > 0:
                return {"action": "proceed_to_scanning", "confidence": 0.9}
            else:
                return {"action": "continue_recon", "confidence": 0.7}
        
        elif current_state == "SCANNING":
            return {"action": "proceed_to_vuln_assessment", "confidence": 0.85}
        
        elif current_state == "VULN_ASSESS":
            exploitable = [d for d in discoveries if d.get('exploitable')]
            if len(exploitable) > 0:
                return {"action": "proceed_to_exploitation", "confidence": 0.9}
            else:
                return {"action": "proceed_to_reporting", "confidence": 0.8}
        
        return {"action": "proceed_to_next_phase", "confidence": 0.5}
