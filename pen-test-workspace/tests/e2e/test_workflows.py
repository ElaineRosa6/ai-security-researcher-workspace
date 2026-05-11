"""Basic smoke tests for the workspace - verifies imports and basic functionality"""
import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class TestCoreImports:
    """Test that all core modules can be imported"""

    def test_import_short_term_memory(self):
        from agent.memory.memory_manager import ShortTermMemory
        assert ShortTermMemory is not None

    def test_import_memory_manager(self):
        from agent.memory.memory_manager import MemoryManager
        assert MemoryManager is not None

    def test_import_knowledge_graph(self):
        from agent.knowledge.graph import KnowledgeGraph
        assert KnowledgeGraph is not None

    def test_import_state_tracker(self):
        from agent.workflow.engine import StateTracker, State
        assert StateTracker is not None
        assert State is not None

    def test_import_quality_control(self):
        from agent.quality.quality_control import Validator, Auditor, SelfAssessment
        assert Validator is not None
        assert Auditor is not None
        assert SelfAssessment is not None

    def test_import_awareness(self):
        from agent.awareness.awareness import AgentAwareness
        assert AgentAwareness is not None

    def test_import_meta_system(self):
        from agent.meta.meta_system import MetaSystem
        assert MetaSystem is not None

    def test_import_agent(self):
        from agent.core.agent import SecurityExpertAgent
        assert SecurityExpertAgent is not None


class TestStateTransitions:
    """Test valid state machine transitions"""

    def test_full_pentest_workflow(self):
        from agent.workflow.engine import StateTracker, State

        tracker = StateTracker()
        assert tracker.current_state == State.INITIALIZED

        # Valid transitions
        assert tracker.transition_to(State.REQUIREMENT_ANALYSIS) is True
        assert tracker.transition_to(State.PLANNING) is True
        assert tracker.transition_to(State.RECON) is True
        assert tracker.transition_to(State.SCANNING) is True
        assert tracker.transition_to(State.VULN_ASSESS) is True
        assert tracker.transition_to(State.EXPLOITATION) is True
        assert tracker.transition_to(State.POST_EXPLOIT) is True
        assert tracker.transition_to(State.REPORTING) is True
        assert tracker.transition_to(State.COMPLETED) is True

    def test_error_recovery(self):
        from agent.workflow.engine import StateTracker, State

        tracker = StateTracker()
        tracker.transition_to(State.REQUIREMENT_ANALYSIS)
        tracker.transition_to(State.PLANNING)

        # Simulate error
        tracker.transition_to(State.ERROR)

        # Recovery
        assert tracker.transition_to(State.PLANNING) is True


class TestConfigurationFiles:
    """Test that all YAML configuration files load correctly"""

    def setup_method(self):
        import yaml
        self.yaml = yaml
        self.config_dir = os.path.join(os.path.dirname(__file__), '../..', 'config')

    def test_agent_core_config(self):
        config_path = os.path.join(self.config_dir, 'agent', 'core.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None

    def test_compliance_recording_config(self):
        config_path = os.path.join(self.config_dir, 'compliance', 'recording.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None

    def test_tor_config(self):
        config_path = os.path.join(self.config_dir, 'proxy', 'tor.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None

    def test_proxychains_config(self):
        config_path = os.path.join(self.config_dir, 'proxy', 'proxychains.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None


class TestWorkflowFiles:
    """Test that workflow definitions are valid YAML"""

    def setup_method(self):
        import yaml
        self.yaml = yaml
        self.workflow_dir = os.path.join(os.path.dirname(__file__), '../..', 'ai-agent', 'workflows')

    def test_web_pentest_workflow(self):
        path = os.path.join(self.workflow_dir, 'web_pentest.yaml')
        if os.path.exists(path):
            with open(path, 'r') as f:
                wf = self.yaml.safe_load(f)
            assert 'name' in wf
            assert 'stages' in wf or 'phases' in wf

    def test_full_pentest_session_workflow(self):
        path = os.path.join(self.workflow_dir, 'full_pentest_session.yaml')
        if os.path.exists(path):
            with open(path, 'r') as f:
                wf = self.yaml.safe_load(f)
            assert 'name' in wf


class TestDirectoryStructure:
    """Test that required directories exist"""

    def setup_method(self):
        self.base = os.path.join(os.path.dirname(__file__), '../..')

    def test_red_team_dirs(self):
        assert os.path.exists(os.path.join(self.base, 'red-team', 'web-security'))
        assert os.path.exists(os.path.join(self.base, 'red-team', 'anonymity'))

    def test_blue_team_dirs(self):
        assert os.path.exists(os.path.join(self.base, 'blue-team', 'incident-response'))
        assert os.path.exists(os.path.join(self.base, 'blue-team', 'threat-intel'))

    def test_purple_team_dirs(self):
        assert os.path.exists(os.path.join(self.base, 'purple-team', 'forensics'))

    def test_compliance_dirs(self):
        assert os.path.exists(os.path.join(self.base, 'compliance', 'recordings'))
        assert os.path.exists(os.path.join(self.base, 'compliance', 'evidence'))

    def test_output_dirs(self):
        assert os.path.exists(os.path.join(self.base, 'output', 'reports'))
        assert os.path.exists(os.path.join(self.base, 'output', 'logs'))


class TestEnvironmentSetup:
    """Test environment files"""

    def setup_method(self):
        self.base = os.path.join(os.path.dirname(__file__), '../..')

    def test_env_exists(self):
        assert os.path.exists(os.path.join(self.base, '.env'))

    def test_env_example_exists(self):
        assert os.path.exists(os.path.join(self.base, '.env.example'))

    def test_requirements_exists(self):
        assert os.path.exists(os.path.join(self.base, 'requirements.txt'))

    def test_readme_exists(self):
        assert os.path.exists(os.path.join(self.base, 'README.md'))
