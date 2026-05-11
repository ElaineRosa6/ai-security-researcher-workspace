"""
Quality Control and Self-Assessment System
"""

import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class Validator:
    """Validates execution results and findings"""
    
    def __init__(self):
        self.validation_rules = self._load_validation_rules()
    
    def _load_validation_rules(self) -> Dict[str, Any]:
        """Load validation rules"""
        return {
            "vulnerability": {
                "required_fields": ["type", "severity", "description"],
                "severity_levels": ["critical", "high", "medium", "low", "info"]
            },
            "evidence": {
                "required_fields": ["file_path", "hash", "timestamp"]
            },
            "execution": {
                "required_fields": ["task_id", "status", "timestamp"]
            }
        }
    
    def validate_result(self, result: Any, expected_criteria: Dict[str, Any] = None) -> Dict[str, Any]:
        """Validate execution result"""
        validation_result = {
            "is_valid": True,
            "issues": [],
            "quality_score": 0,
            "confidence": 0,
            "timestamp": datetime.now().isoformat()
        }
        
        if isinstance(result, dict):
            completeness_score = self.check_completeness(result, expected_criteria)
            accuracy_score = self.check_accuracy(result)
            consistency_score = self.check_consistency(result)
            
            validation_result["completeness"] = completeness_score
            validation_result["accuracy"] = accuracy_score
            validation_result["consistency"] = consistency_score
            
            validation_result["quality_score"] = (
                completeness_score * 0.3 +
                accuracy_score * 0.3 +
                consistency_score * 0.2
            )
            
            validation_result["confidence"] = validation_result["quality_score"]
            
            if completeness_score < 0.7:
                validation_result["is_valid"] = False
                validation_result["issues"].append("Incomplete result")
            
            if accuracy_score < 0.5:
                validation_result["is_valid"] = False
                validation_result["issues"].append("Low accuracy")
        
        return validation_result
    
    def check_completeness(self, result: Dict[str, Any], 
                          criteria: Dict[str, Any] = None) -> float:
        """Check result completeness"""
        if not criteria:
            criteria = self.validation_rules.get(
                result.get('type', 'execution'),
                {}
            )
        
        required_fields = criteria.get('required_fields', [])
        
        if not required_fields:
            return 1.0
        
        present_fields = sum(1 for f in required_fields if f in result and result[f])
        
        return present_fields / len(required_fields)
    
    def check_accuracy(self, result: Dict[str, Any]) -> float:
        """Check result accuracy"""
        score = 1.0
        
        if result.get('type') == 'vulnerability':
            severity = result.get('severity', '').lower()
            if severity not in ['critical', 'high', 'medium', 'low', 'info']:
                score -= 0.3
            
            if not result.get('description'):
                score -= 0.2
            
            if not result.get('evidence'):
                score -= 0.2
        
        elif result.get('type') == 'execution':
            if result.get('status') not in ['success', 'failed', 'skipped']:
                score -= 0.3
        
        return max(0.0, score)
    
    def check_consistency(self, result: Dict[str, Any]) -> float:
        """Check result consistency"""
        score = 1.0
        
        timestamp = result.get('timestamp')
        if timestamp:
            try:
                datetime.fromisoformat(timestamp)
            except:
                score -= 0.3
        
        if result.get('type') == 'vulnerability':
            if result.get('exploitable') and result.get('severity') == 'info':
                score -= 0.3
        
        return max(0.0, score)
    
    def validate_finding(self, finding: Dict[str, Any]) -> Dict[str, Any]:
        """Validate a security finding"""
        validation = self.validate_result(finding, self.validation_rules.get('vulnerability'))
        
        if finding.get('severity'):
            validation["severity_valid"] = finding['severity'] in \
                self.validation_rules['vulnerability']['severity_levels']
        
        return validation


class Checker:
    """Performs various checks on findings and results"""
    
    def __init__(self):
        self.check_results = []
    
    def check_false_positive(self, finding: Dict[str, Any]) -> Dict[str, Any]:
        """Check if finding is a false positive"""
        indicators = []
        false_positive_score = 0.0
        
        if not finding.get('evidence'):
            indicators.append("No evidence provided")
            false_positive_score += 0.3
        
        if not finding.get('reproducible', True):
            indicators.append("Not reproducible")
            false_positive_score += 0.3
        
        if finding.get('confidence', 1.0) < 0.5:
            indicators.append("Low confidence")
            false_positive_score += 0.2
        
        return {
            "is_false_positive": false_positive_score > 0.5,
            "false_positive_score": false_positive_score,
            "indicators": indicators
        }
    
    def check_evidence_quality(self, evidence: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Check evidence quality"""
        quality = {
            "total_evidence": len(evidence),
            "has_screenshots": False,
            "has_logs": False,
            "has_hashes": False,
            "has_network_capture": False,
            "quality_score": 0.0
        }
        
        for e in evidence:
            if e.get('type') == 'screenshot':
                quality["has_screenshots"] = True
            elif e.get('type') == 'log':
                quality["has_logs"] = True
            elif e.get('type') == 'hash':
                quality["has_hashes"] = True
            elif e.get('type') == 'pcap':
                quality["has_network_capture"] = True
        
        quality["quality_score"] = sum([
            quality["has_screenshots"] * 0.25,
            quality["has_logs"] * 0.25,
            quality["has_hashes"] * 0.25,
            quality["has_network_capture"] * 0.25
        ])
        
        return quality
    
    def check_severity_rating(self, finding: Dict[str, Any]) -> Dict[str, Any]:
        """Check and validate severity rating"""
        severity = finding.get('severity', 'info')
        
        severity_scores = {
            'critical': 1.0,
            'high': 0.75,
            'medium': 0.5,
            'low': 0.25,
            'info': 0.1
        }
        
        expected_score = severity_scores.get(severity.lower(), 0.1)
        
        return {
            "severity": severity,
            "score": expected_score,
            "is_valid": True
        }


class Auditor:
    """Records all decisions and actions for audit purposes"""
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.audit_log = []
        self.decision_log = []
        self.action_log = []
        
        self.log_dir = Path('compliance/logs/audit')
        self.log_dir.mkdir(parents=True, exist_ok=True)
    
    def log_decision(self, decision: Dict[str, Any]) -> None:
        """Log a decision"""
        entry = {
            "log_id": self._generate_id(),
            "session_id": self.session_id,
            "type": "decision",
            "data": decision,
            "timestamp": datetime.now().isoformat()
        }
        
        self.decision_log.append(entry)
        self._persist_log()
    
    def log_action(self, action: Dict[str, Any]) -> None:
        """Log an action"""
        entry = {
            "log_id": self._generate_id(),
            "session_id": self.session_id,
            "type": "action",
            "data": action,
            "timestamp": datetime.now().isoformat()
        }
        
        self.action_log.append(entry)
        self._persist_log()
    
    def log_state_transition(self, from_state: str, to_state: str, reason: str) -> None:
        """Log state transition"""
        entry = {
            "log_id": self._generate_id(),
            "session_id": self.session_id,
            "type": "state_transition",
            "from_state": from_state,
            "to_state": to_state,
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        }
        
        self.audit_log.append(entry)
        self._persist_log()
    
    def get_audit_trail(self) -> List[Dict[str, Any]]:
        """Get complete audit trail"""
        return sorted(
            self.audit_log + self.decision_log + self.action_log,
            key=lambda x: x.get('timestamp', '')
        )
    
    def generate_audit_report(self) -> Dict[str, Any]:
        """Generate audit report"""
        return {
            "session_id": self.session_id,
            "total_decisions": len(self.decision_log),
            "total_actions": len(self.action_log),
            "total_state_transitions": len(self.audit_log),
            "timeline": self.get_audit_trail()
        }
    
    def _persist_log(self) -> None:
        """Persist logs to disk"""
        log_file = self.log_dir / f"{self.session_id}_audit.json"
        
        with open(log_file, 'w') as f:
            json.dump({
                "audit_log": self.audit_log,
                "decision_log": self.decision_log,
                "action_log": self.action_log
            }, f, indent=2)
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"audit_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


class SelfAssessment:
    """Self-assessment and performance evaluation"""
    
    def __init__(self, execution_history: List[Dict], memory_manager):
        self.execution_history = execution_history
        self.memory_manager = memory_manager
    
    def assess_performance(self) -> Dict[str, Any]:
        """Assess overall performance"""
        assessment = {
            "overall_score": 0,
            "strengths": [],
            "weaknesses": [],
            "recommendations": [],
            "lessons_learned": [],
            "metrics": {},
            "timestamp": datetime.now().isoformat()
        }
        
        completion_rate = self.calculate_completion_rate()
        quality_score = self.assess_result_quality()
        efficiency_score = self.assess_efficiency()
        decision_quality = self.assess_decision_quality()
        
        assessment["metrics"]["completion_rate"] = completion_rate
        assessment["metrics"]["quality_score"] = quality_score
        assessment["metrics"]["efficiency_score"] = efficiency_score
        assessment["metrics"]["decision_quality"] = decision_quality
        
        assessment["overall_score"] = (
            completion_rate * 0.25 +
            quality_score * 0.35 +
            efficiency_score * 0.2 +
            decision_quality * 0.2
        )
        
        if completion_rate > 0.8:
            assessment["strengths"].append("High task completion rate")
        else:
            assessment["weaknesses"].append("Low task completion rate")
        
        if quality_score > 0.8:
            assessment["strengths"].append("High result quality")
        else:
            assessment["weaknesses"].append("Result quality needs improvement")
        
        assessment["recommendations"] = self.generate_improvements()
        assessment["lessons_learned"] = self.extract_lessons()
        
        return assessment
    
    def calculate_completion_rate(self) -> float:
        """Calculate task completion rate"""
        if not self.execution_history:
            return 0.0
        
        completed = sum(1 for e in self.execution_history 
                        if e.get('status') == 'success')
        
        return completed / len(self.execution_history)
    
    def assess_result_quality(self) -> float:
        """Assess result quality"""
        discoveries = self.memory_manager.retrieve('medium_term').get('discoveries', [])
        
        if not discoveries:
            return 0.0
        
        total_confidence = sum(d.get('confidence', 0) for d in discoveries)
        avg_confidence = total_confidence / len(discoveries)
        
        return avg_confidence
    
    def assess_efficiency(self) -> float:
        """Assess efficiency"""
        if not self.execution_history:
            return 0.0
        
        failed = sum(1 for e in self.execution_history 
                    if e.get('status') == 'failed')
        
        efficiency = 1.0 - (failed / len(self.execution_history))
        
        return efficiency
    
    def assess_decision_quality(self) -> float:
        """Assess decision quality"""
        decisions = self.memory_manager.retrieve('medium_term').get('decision_history', [])
        
        if not decisions:
            return 0.5
        
        good_decisions = sum(1 for d in decisions 
                           if d.get('outcome') in ['success', 'partial_success'])
        
        return good_decisions / len(decisions)
    
    def generate_improvements(self) -> List[str]:
        """Generate improvement suggestions"""
        improvements = []
        
        completion = self.calculate_completion_rate()
        if completion < 0.8:
            improvements.append("Focus on improving task completion strategies")
        
        quality = self.assess_result_quality()
        if quality < 0.7:
            improvements.append("Improve evidence collection for findings")
        
        efficiency = self.assess_efficiency()
        if efficiency < 0.9:
            improvements.append("Reduce unnecessary tool executions")
        
        return improvements
    
    def extract_lessons(self) -> List[str]:
        """Extract lessons from current session"""
        lessons = []
        
        discoveries = self.memory_manager.retrieve('medium_term').get('discoveries', [])
        successful_types = set(d.get('type') for d in discoveries 
                              if d.get('confidence', 0) > 0.8)
        
        for stype in successful_types:
            lessons.append(f"Successful technique for {stype} identified")
        
        return lessons
