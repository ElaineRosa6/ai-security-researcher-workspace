"""
Unit tests for Agent Awareness System
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.awareness.awareness import AgentAwareness, ContextAwareness, DecisionGuide


class MockStateTracker:
    """Mock state tracker for testing"""
    def __init__(self):
        self.current_state = "INITIALIZED"
        self.context = {}
    
    def get_current_state(self):
        return self.current_state
    
    def get_context(self, key=None):
        if key:
            return self.context.get(key)
        return self.context
    
    def transition_to(self, state, reason=None):
        self.current_state = state


class MockMemoryManager:
    """Mock memory manager for testing"""
    def __init__(self):
        self.short_term = {"current_task": None, "recent_actions": []}
        self.medium_term = {"discoveries": [], "target_profile": {}}
    
    def get_summary(self):
        return {
            "short_term_size": 10,
            "medium_term_discoveries": 5,
            "long_term_items": 100
        }
    
    def retrieve(self, memory_type, query=None):
        if memory_type == 'short_term':
            return self.short_term
        elif memory_type == 'medium_term':
            return self.medium_term
        return {}


class TestAgentAwareness:
    """Test AgentAwareness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.state_tracker = MockStateTracker()
        self.memory_manager = MockMemoryManager()
        self.awareness = AgentAwareness(self.state_tracker, self.memory_manager)
    
    def test_get_self_status(self):
        """Test getting agent self status"""
        status = self.awareness.get_self_status()
        
        assert 'current_state' in status
        assert 'context' in status
        assert 'memory_snapshot' in status
        assert 'capabilities' in status
        assert 'current_focus' in status
        assert status['current_state'] == "INITIALIZED"
    
    def test_get_capabilities(self):
        """Test getting available capabilities"""
        capabilities = self.awareness.get_capabilities()
        
        assert isinstance(capabilities, list)
        assert len(capabilities) > 0
        assert 'web_security_testing' in capabilities
    
    def test_get_current_focus(self):
        """Test getting current focus"""
        focus = self.awareness.get_current_focus()
        
        assert isinstance(focus, str)
        assert len(focus) > 0
    
    def test_get_open_tasks(self):
        """Test getting open tasks"""
        self.state_tracker.context['current_plan'] = {
            'phases': [
                {'name': 'recon', 'tasks': [{'id': 'task1', 'name': 'Test Task'}]}
            ]
        }
        self.state_tracker.context['current_phase'] = 'recon'
        
        tasks = self.awareness.get_open_tasks()
        
        assert isinstance(tasks, list)
    
    def test_identify_missing_info(self):
        """Test identifying missing information"""
        missing = self.awareness.identify_missing_info()
        
        assert isinstance(missing, list)
    
    def test_should_ask_for_clarification(self):
        """Test clarification requirement check"""
        result = self.awareness.should_ask_for_clarification()
        
        assert isinstance(result, bool)
    
    def test_state_awareness(self):
        """Test state awareness functionality"""
        self.state_tracker.current_state = "RECON"
        
        status = self.awareness.get_self_status()
        
        assert status['current_state'] == "RECON"
    
    def test_context_tracking(self):
        """Test context tracking"""
        self.state_tracker.context['test_key'] = 'test_value'
        
        status = self.awareness.get_self_status()
        
        assert 'context' in status


class TestContextAwareness:
    """Test ContextAwareness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.memory_manager = MockMemoryManager()
        self.knowledge_graph = MockKnowledgeGraph()
        self.context_awareness = ContextAwareness(
            self.memory_manager, 
            self.knowledge_graph
        )
    
    def test_get_relevant_context(self):
        """Test getting relevant context"""
        context = self.context_awareness.get_relevant_context("test query")
        
        assert 'query' in context
        assert context['query'] == "test query"
        assert 'related_memories' in context
    
    def test_build_context_window(self):
        """Test building context window"""
        window = self.context_awareness.build_context_window()
        
        assert 'timestamp' in window
        assert 'short_term' in window
        assert 'recent_discoveries' in window
    
    def test_target_summary(self):
        """Test target summary"""
        summary = self.context_awareness._get_target_summary()
        
        assert 'type' in summary
        assert 'risk_level' in summary
    
    def test_risk_calculation(self):
        """Test risk level calculation"""
        profile = {
            'vulnerabilities': [
                {'severity': 'critical'},
                {'severity': 'high'}
            ]
        }
        
        risk = self.context_awareness._calculate_risk_level(profile)
        
        assert risk in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']


class MockKnowledgeGraph:
    """Mock knowledge graph for testing"""
    def query(self, query_pattern):
        return []


class TestDecisionGuide:
    """Test DecisionGuide class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.knowledge_base = {}
        self.pattern_recognizer = MockPatternRecognizer()
        self.decision_guide = DecisionGuide(
            self.knowledge_base,
            self.pattern_recognizer
        )
    
    def test_generate_options(self):
        """Test generating decision options"""
        context = {'current_state': 'RECON'}
        
        options = self.decision_guide.generate_options(context)
        
        assert isinstance(options, list)
        assert len(options) > 0
    
    def test_evaluate_options(self):
        """Test evaluating options"""
        options = [
            {'action': 'test1', 'name': 'Test 1', 'confidence': 0.9},
            {'action': 'test2', 'name': 'Test 2', 'confidence': 0.7}
        ]
        criteria = {'risk_tolerance': 0.3}
        
        evaluations = self.decision_guide.evaluate_options(options, criteria)
        
        assert isinstance(evaluations, list)
        assert len(evaluations) == 2
    
    def test_calculate_score(self):
        """Test calculating option score"""
        option = {'confidence': 0.8}
        criteria = {'risk_tolerance': 0.3}
        
        score = self.decision_guide._calculate_score(option, criteria)
        
        assert 0 <= score <= 1
    
    def test_identify_risks(self):
        """Test identifying risks"""
        option = {'action': 'exploit'}
        
        risks = self.decision_guide._identify_risks(option)
        
        assert isinstance(risks, list)
    
    def test_identify_benefits(self):
        """Test identifying benefits"""
        option = {'action': 'exploit'}
        
        benefits = self.decision_guide._identify_benefits(option)
        
        assert isinstance(benefits, list)
    
    def test_make_recommendation(self):
        """Test making recommendation"""
        evaluations = [
            {'option': {'action': 'test', 'name': 'Test', 'confidence': 0.9}, 'score': 0.9}
        ]
        
        recommendation = self.decision_guide.make_recommendation(evaluations)
        
        assert 'action' in recommendation
        assert 'reasoning' in recommendation
    
    def test_assess_feasibility(self):
        """Test feasibility assessment"""
        option = {'confidence': 0.7}
        
        feasibility = self.decision_guide._assess_feasibility(option)
        
        assert 0 <= feasibility <= 1


class MockPatternRecognizer:
    """Mock pattern recognizer for testing"""
    def recognize(self, pattern):
        return None


class TestAwarenessIntegration:
    """Integration tests for awareness system"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.state_tracker = MockStateTracker()
        self.memory_manager = MockMemoryManager()
        self.awareness = AgentAwareness(self.state_tracker, self.memory_manager)
    
    def test_complete_self_assessment_flow(self):
        """Test complete self-assessment workflow"""
        status = self.awareness.get_self_status()
        
        assert status['current_state'] == "INITIALIZED"
        
        capabilities = self.awareness.get_capabilities()
        assert len(capabilities) > 0
        
        focus = self.awareness.get_current_focus()
        assert isinstance(focus, str)
    
    def test_missing_info_detection(self):
        """Test detection of missing information"""
        missing = self.awareness.identify_missing_info()
        
        assert isinstance(missing, list)
    
    def test_clarification_workflow(self):
        """Test clarification requirement workflow"""
        needs_clarification = self.awareness.should_ask_for_clarification()
        
        assert isinstance(needs_clarification, bool)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
