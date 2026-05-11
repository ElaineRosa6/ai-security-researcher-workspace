"""
Awareness System - State Awareness, Context Awareness, Decision Guide
"""

import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class AgentAwareness:
    """Agent self-awareness and state perception"""
    
    def __init__(self, state_tracker, memory_manager):
        self.state_tracker = state_tracker
        self.memory_manager = memory_manager
    
    def get_self_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "current_state": self.state_tracker.get_current_state(),
            "context": self.state_tracker.get_context(),
            "memory_snapshot": self.memory_manager.get_summary(),
            "capabilities": self.get_capabilities(),
            "current_focus": self.get_current_focus(),
            "open_tasks": self.get_open_tasks(),
            "missing_info": self.identify_missing_info()
        }
    
    def get_capabilities(self) -> List[str]:
        """Get current available capabilities"""
        capabilities = [
            "web_security_testing",
            "network_scanning",
            "vulnerability_assessment",
            "exploitation",
            "report_generation"
        ]
        
        return capabilities
    
    def get_current_focus(self) -> str:
        """Get current focus area"""
        state = self.state_tracker.get_current_state()
        context = self.state_tracker.get_context()
        
        if state == "RECON":
            return "Information gathering"
        elif state == "SCANNING":
            return "Service enumeration"
        elif state == "VULN_ASSESS":
            return "Vulnerability identification"
        elif state == "EXPLOITATION":
            return "Exploitation"
        elif state == "POST_EXPLOIT":
            return "Post-exploitation"
        elif state == "REPORTING":
            return "Report generation"
        else:
            return context.get('current_phase', 'Unknown')
    
    def get_open_tasks(self) -> List[Dict[str, Any]]:
        """Get pending tasks"""
        plan = self.state_tracker.get_context('current_plan')
        
        if not plan:
            return []
        
        current_phase = self.state_tracker.get_context('current_phase')
        
        tasks = []
        for phase in plan.get('phases', []):
            if phase.get('name') == current_phase:
                tasks = phase.get('tasks', [])
                break
        
        return tasks
    
    def identify_missing_info(self) -> List[str]:
        """Identify missing information"""
        missing = []
        
        context = self.state_tracker.get_context()
        
        if not context.get('requirement'):
            missing.append("Requirement information")
        
        target_profile = context.get('target_profile', {})
        if not target_profile or not target_profile.get('discovered'):
            missing.append("Target information")
        
        discoveries = context.get('discoveries', [])
        if not discoveries:
            missing.append("Security findings")
        
        return missing
    
    def should_ask_for_clarification(self) -> bool:
        """Determine if clarification is needed"""
        missing = self.identify_missing_info()
        
        critical_missing = [
            "Requirement information",
            "Target information"
        ]
        
        for item in critical_missing:
            if item in missing:
                return True
        
        return False


class ContextAwareness:
    """Context understanding and management"""
    
    def __init__(self, memory_manager, knowledge_graph):
        self.memory_manager = memory_manager
        self.knowledge_graph = knowledge_graph
    
    def get_relevant_context(self, query: str) -> Dict[str, Any]:
        """Get context relevant to query"""
        context = {
            "query": query,
            "related_memories": [],
            "related_knowledge": [],
            "similar_episodes": []
        }
        
        context["related_memories"] = self.memory_manager.retrieve(
            query=query
        )
        
        context["related_knowledge"] = self.knowledge_graph.query({
            "query": query
        })
        
        context["similar_episodes"] = self.memory_manager.retrieve(
            'episodic',
            {'type': 'security_test'}
        )
        
        return context
    
    def build_context_window(self) -> Dict[str, Any]:
        """Build context window for current operations"""
        window = {
            "timestamp": datetime.now().isoformat(),
            "short_term": self.memory_manager.retrieve('short_term'),
            "recent_discoveries": self.memory_manager.retrieve('medium_term').get('discoveries', [])[-5:],
            "target_summary": self._get_target_summary()
        }
        
        return window
    
    def _get_target_summary(self) -> Dict[str, Any]:
        """Get target summary"""
        target_profile = self.memory_manager.retrieve('medium_term').get('target_profile', {})
        
        return {
            "type": target_profile.get('type'),
            "services_count": len(target_profile.get('services', [])),
            "vulnerabilities_count": len(target_profile.get('vulnerabilities', [])),
            "risk_level": self._calculate_risk_level(target_profile)
        }
    
    def _calculate_risk_level(self, profile: Dict) -> str:
        """Calculate overall risk level"""
        vulns = profile.get('vulnerabilities', [])
        
        critical_count = sum(1 for v in vulns if v.get('severity') == 'critical')
        high_count = sum(1 for v in vulns if v.get('severity') == 'high')
        
        if critical_count > 0:
            return "CRITICAL"
        elif high_count > 0:
            return "HIGH"
        elif len(vulns) > 0:
            return "MEDIUM"
        else:
            return "LOW"


class DecisionGuide:
    """Decision making guidance"""
    
    def __init__(self, knowledge_base, pattern_recognizer):
        self.knowledge_base = knowledge_base
        self.pattern_recognizer = pattern_recognizer
    
    def generate_options(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate decision options"""
        options = []
        
        standard_options = self._get_standard_options(context)
        options.extend(standard_options)
        
        innovative_options = self._generate_innovative_options(context)
        options.extend(innovative_options)
        
        fallback_options = self._generate_fallback_options(context)
        options.extend(fallback_options)
        
        return options
    
    def _get_standard_options(self, context: Dict) -> List[Dict]:
        """Get standard options"""
        state = context.get('current_state')
        
        standard_options = {
            "RECON": [
                {"action": "continue_recon", "name": "Continue reconnaissance", "confidence": 0.9},
                {"action": "expand_scope", "name": "Expand reconnaissance scope", "confidence": 0.7}
            ],
            "SCANNING": [
                {"action": "continue_scan", "name": "Continue scanning", "confidence": 0.9},
                {"action": "focus_web", "name": "Focus on web services", "confidence": 0.8}
            ],
            "VULN_ASSESS": [
                {"action": "test_vulns", "name": "Test identified vulnerabilities", "confidence": 0.9},
                {"action": "more_scan", "name": "Additional scanning", "confidence": 0.6}
            ],
            "EXPLOITATION": [
                {"action": "exploit_critical", "name": "Exploit critical findings", "confidence": 0.9},
                {"action": "pivot", "name": "Pivot to new target", "confidence": 0.7}
            ]
        }
        
        return standard_options.get(state, [])
    
    def _generate_innovative_options(self, context: Dict) -> List[Dict]:
        """Generate innovative options"""
        return []
    
    def _generate_fallback_options(self, context: Dict) -> List[Dict]:
        """Generate fallback options"""
        return [
            {"action": "report", "name": "Generate report with current findings", "confidence": 0.95},
            {"action": "pause", "name": "Pause and request guidance", "confidence": 0.85}
        ]
    
    def evaluate_options(self, options: List[Dict], criteria: Dict) -> List[Dict]:
        """Evaluate and rank options"""
        evaluations = []
        
        for option in options:
            evaluation = {
                "option": option,
                "score": self._calculate_score(option, criteria),
                "risks": self._identify_risks(option),
                "benefits": self._identify_benefits(option),
                "feasibility": self._assess_feasibility(option)
            }
            evaluations.append(evaluation)
        
        return sorted(evaluations, key=lambda x: x['score'], reverse=True)
    
    def _calculate_score(self, option: Dict, criteria: Dict) -> float:
        """Calculate option score"""
        base_score = option.get('confidence', 0.5)
        
        risk_weight = criteria.get('risk_tolerance', 0.3)
        
        feasibility = self._assess_feasibility(option)
        
        return base_score * (1 - risk_weight) + feasibility * risk_weight
    
    def _identify_risks(self, option: Dict) -> List[str]:
        """Identify risks for option"""
        risks = []
        
        action = option.get('action', '')
        
        if 'exploit' in action:
            risks.append("Detection risk")
            risks.append("Potential system damage")
        
        if 'scan' in action:
            risks.append("Network disruption")
        
        return risks
    
    def _identify_benefits(self, option: Dict) -> List[str]:
        """Identify benefits for option"""
        benefits = []
        
        action = option.get('action', '')
        
        if 'exploit' in action:
            benefits.append("Proof of concept")
            benefits.append("Full access demonstration")
        
        if 'scan' in action:
            benefits.append("Comprehensive coverage")
        
        return benefits
    
    def _assess_feasibility(self, option: Dict) -> float:
        """Assess feasibility of option"""
        confidence = option.get('confidence', 0.5)
        
        return confidence
    
    def make_recommendation(self, evaluations: List[Dict]) -> Dict:
        """Make final recommendation"""
        if not evaluations:
            return {
                "action": "pause",
                "reason": "No valid options available"
            }
        
        best = evaluations[0]
        
        return {
            "action": best['option'].get('action'),
            "name": best['option'].get('name'),
            "confidence": best['score'],
            "reasoning": f"Highest score: {best['score']:.2f}"
        }
