"""
Unit tests for Meta System
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.meta.meta_system import MetaSystem, Monitor, Learning, Improvement, Telemetry


class MockKnowledgeBase:
    """Mock knowledge base for testing"""
    def __init__(self):
        self.stored = []
    
    def store_knowledge(self, knowledge):
        self.stored.append(knowledge)
        return True
    
    def retrieve_knowledge(self, category=None, query=None):
        return self.stored


class TestMetaSystem:
    """Test MetaSystem class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.meta_system = MetaSystem()
    
    def test_initialization(self):
        """Test meta system initialization"""
        assert hasattr(self.meta_system, 'agent_telemetry')
        assert hasattr(self.meta_system, 'performance_metrics')
        assert hasattr(self.meta_system, 'best_practices')
    
    def test_monitor_agent(self):
        """Test monitoring agent"""
        agent_state = {
            'current_state': 'RECON',
            'open_tasks': 5,
            'discoveries': []
        }
        
        self.meta_system.monitor_agent(agent_state)
        
        assert len(self.meta_system.agent_telemetry) > 0
    
    def test_collect_metrics(self):
        """Test collecting metrics"""
        metrics = self.meta_system.collect_metrics()
        
        assert isinstance(metrics, dict)
        assert 'task_completion_rate' in metrics
        assert 'success_rate' in metrics
    
    def test_calculate_completion_rate(self):
        """Test completion rate calculation"""
        rate = self.meta_system._calculate_completion_rate()
        
        assert 0 <= rate <= 1
    
    def test_calculate_success_rate(self):
        """Test success rate calculation"""
        rate = self.meta_system._calculate_success_rate()
        
        assert 0 <= rate <= 1
    
    def test_count_self_corrections(self):
        """Test counting self-corrections"""
        count = self.meta_system._count_self_corrections()
        
        assert isinstance(count, int)
        assert count >= 0
    
    def test_estimate_memory_usage(self):
        """Test memory usage estimation"""
        usage = self.meta_system._estimate_memory_usage()
        
        assert isinstance(usage, dict)


class TestMonitor:
    """Test Monitor class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.monitor = Monitor()
    
    def test_initialization(self):
        """Test monitor initialization"""
        assert self.monitor.health_status == "healthy"
        assert isinstance(self.monitor.alerts, list)
    
    def test_check_health(self):
        """Test health check"""
        health = self.monitor.check_health()
        
        assert 'status' in health
        assert 'alerts_count' in health
        assert 'timestamp' in health
    
    def test_log_metric(self):
        """Test logging metric"""
        metric = {'completion': 0.8, 'accuracy': 0.9}
        
        self.monitor.log_metric(metric)
        
        assert len(self.monitor.metrics_history) > 0
    
    def test_check_anomalies(self):
        """Test anomaly detection"""
        for i in range(15):
            self.monitor.log_metric({'completion': 0.3})
        
        anomalies = self.monitor.check_anomalies()
        
        assert isinstance(anomalies, list)
    
    def test_health_status_update(self):
        """Test health status updates"""
        self.monitor.health_status = "warning"
        
        health = self.monitor.check_health()
        
        assert health['status'] == "warning"


class TestLearning:
    """Test Learning class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.knowledge_base = MockKnowledgeBase()
        self.learning = Learning(self.knowledge_base)
    
    def test_initialization(self):
        """Test learning initialization"""
        assert hasattr(self.learning, 'knowledge_base')
        assert hasattr(self.learning, 'learned_patterns')
    
    def test_learn_from_success(self):
        """Test learning from success"""
        success_record = {
            'context': {'target': 'test'},
            'actions': ['scan', 'exploit'],
            'outcome': 'success'
        }
        
        self.learning.learn_from_success(success_record)
        
        assert len(self.learning.learned_patterns) > 0
    
    def test_learn_from_failure(self):
        """Test learning from failure"""
        failure_record = {
            'context': {'target': 'test'},
            'error': 'Connection timeout',
            'actions': ['scan'],
            'outcome': 'failure'
        }
        
        self.learning.learn_from_failure(failure_record)
        
        assert len(self.learning.learned_patterns) > 0
    
    def test_extract_patterns(self):
        """Test extracting patterns"""
        self.learning.learn_from_success({
            'context': {},
            'actions': ['test'],
            'outcome': 'success'
        })
        
        patterns = self.learning.extract_patterns()
        
        assert 'successful_techniques' in patterns
        assert 'failed_techniques' in patterns
    
    def test_update_strategy(self):
        """Test updating strategy"""
        patterns = {
            'successful_techniques': [
                {'actions': ['scan']}
            ],
            'failed_techniques': [
                {'actions': ['exploit']}
            ]
        }
        
        strategy = self.learning.update_strategy(patterns)
        
        assert 'preferred_techniques' in strategy
        assert 'avoid_techniques' in strategy


class TestImprovement:
    """Test Improvement class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.improvement = Improvement()
    
    def test_initialization(self):
        """Test improvement initialization"""
        assert hasattr(self.improvement, 'improvement_history')
        assert hasattr(self.improvement, 'pending_improvements')
    
    def test_identify_improvements(self):
        """Test identifying improvements"""
        metrics = {'task_completion_rate': 0.5, 'success_rate': 0.6}
        patterns = {'patterns': []}
        
        improvements = self.improvement.identify_improvements(metrics, patterns)
        
        assert isinstance(improvements, list)
    
    def test_prioritize_improvements(self):
        """Test prioritizing improvements"""
        improvements = [
            {'area': 'test1', 'priority': 'low'},
            {'area': 'test2', 'priority': 'high'}
        ]
        
        prioritized = self.improvement.prioritize_improvements(improvements)
        
        assert prioritized[0]['priority'] == 'high'
    
    def test_apply_improvement(self):
        """Test applying improvement"""
        improvement = {'area': 'testing', 'suggestion': 'Add more tests'}
        
        self.improvement.apply_improvement(improvement)
        
        assert len(self.improvement.improvement_history) > 0
    
    def test_track_progress(self):
        """Test tracking progress"""
        progress = self.improvement.track_progress()
        
        assert 'total_improvements' in progress
        assert 'pending' in progress


class TestTelemetry:
    """Test Telemetry class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.telemetry = Telemetry()
    
    def test_initialization(self):
        """Test telemetry initialization"""
        assert hasattr(self.telemetry, 'telemetry_data')
        assert isinstance(self.telemetry.telemetry_data, list)
    
    def test_collect(self):
        """Test collecting telemetry data"""
        data = {'type': 'metric', 'value': 100}
        
        self.telemetry.collect(data)
        
        assert len(self.telemetry.telemetry_data) > 0
    
    def test_generate_summary(self):
        """Test generating summary"""
        self.telemetry.collect({'type': 'test'})
        
        summary = self.telemetry.generate_summary()
        
        assert 'total_records' in summary
        assert 'time_range' in summary
        assert 'record_types' in summary
    
    def test_count_types(self):
        """Test counting record types"""
        self.telemetry.collect({'type': 'test1'})
        self.telemetry.collect({'type': 'test2'})
        self.telemetry.collect({'type': 'test1'})
        
        counts = self.telemetry._count_types()
        
        assert counts['test1'] == 2
        assert counts['test2'] == 1


class TestMetaSystemIntegration:
    """Integration tests for meta system"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.meta_system = MetaSystem()
        self.knowledge_base = MockKnowledgeBase()
        self.learning = Learning(self.knowledge_base)
    
    def test_full_monitoring_flow(self):
        """Test complete monitoring flow"""
        agent_state = {
            'current_state': 'EXPLOITATION',
            'open_tasks': 3,
            'discoveries': [{'severity': 'high'}]
        }
        
        self.meta_system.monitor_agent(agent_state)
        
        metrics = self.meta_system.collect_metrics()
        
        assert 'task_completion_rate' in metrics
    
    def test_learning_and_improvement_flow(self):
        """Test learning and improvement flow"""
        success_record = {
            'context': {'phase': 'recon'},
            'actions': ['nmap_scan'],
            'outcome': 'success'
        }
        
        self.learning.learn_from_success(success_record)
        
        patterns = self.learning.extract_patterns()
        
        improvement = Improvement()
        improvements = improvement.identify_improvements(
            {'task_completion_rate': 0.7},
            patterns
        )
        
        assert isinstance(improvements, list)
    
    def test_telemetry_collection_flow(self):
        """Test telemetry collection flow"""
        telemetry = Telemetry()
        
        telemetry.collect({'type': 'action', 'data': 'test_action'})
        telemetry.collect({'type': 'metric', 'value': 100})
        
        summary = telemetry.generate_summary()
        
        assert summary['total_records'] == 2
        assert 'test_action' in summary['record_types']
        assert 'metric' in summary['record_types']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
