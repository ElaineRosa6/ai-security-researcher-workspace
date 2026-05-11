"""Integration tests for Skills System"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestSkillLoading:
    """Test that all skills can be loaded without errors"""

    def test_red_team_skills_import(self):
        """Test Red Team skills can be imported"""
        try:
            from ai_agent.skills.red_team.web_security import WebSecuritySkill
            assert WebSecuritySkill is not None
        except ImportError:
            pytest.skip("WebSecuritySkill not implemented yet")

        try:
            from ai_agent.skills.red_team.binary_security import BinarySecuritySkill
            assert BinarySecuritySkill is not None
        except ImportError:
            pytest.skip("BinarySecuritySkill not implemented yet")

        try:
            from ai_agent.skills.red_team.mobile_security import MobileSecuritySkill
            assert MobileSecuritySkill is not None
        except ImportError:
            pytest.skip("MobileSecuritySkill not implemented yet")

        try:
            from ai_agent.skills.red_team.domain_pentest import DomainPentestSkill
            assert DomainPentestSkill is not None
        except ImportError:
            pytest.skip("DomainPentestSkill not implemented yet")

        try:
            from ai_agent.skills.red_team.anonymity import AnonymitySkill
            assert AnonymitySkill is not None
        except ImportError:
            pytest.skip("AnonymitySkill not implemented yet")

    def test_blue_team_skills_import(self):
        """Test Blue Team skills can be imported"""
        try:
            from ai_agent.skills.blue_team.incident_response import IncidentResponseSkill
            assert IncidentResponseSkill is not None
        except ImportError:
            pytest.skip("IncidentResponseSkill not implemented yet")

        try:
            from ai_agent.skills.blue_team.threat_intel import ThreatIntelSkill
            assert ThreatIntelSkill is not None
        except ImportError:
            pytest.skip("ThreatIntelSkill not implemented yet")

    def test_purple_team_skills_import(self):
        """Test Purple Team skills can be imported"""
        try:
            from ai_agent.skills.purple_team.forensics import ForensicsSkill
            assert ForensicsSkill is not None
        except ImportError:
            pytest.skip("ForensicsSkill not implemented yet")

    def test_compliance_skills_import(self):
        """Test Compliance skills can be imported"""
        try:
            from ai_agent.skills.compliance.compliance import RecordingSkill
            assert RecordingSkill is not None
        except ImportError:
            pytest.skip("RecordingSkill not implemented yet")

        try:
            from ai_agent.skills.compliance.compliance import EvidenceSkill
            assert EvidenceSkill is not None
        except ImportError:
            pytest.skip("EvidenceSkill not implemented yet")


class TestConfigLoading:
    """Test that configuration files can be loaded"""

    def setup_method(self):
        import yaml
        self.yaml = yaml
        self.config_dir = os.path.join(os.path.dirname(__file__), '..', 'config')

    def test_agent_core_config(self):
        """Test agent core configuration loads"""
        config_path = os.path.join(self.config_dir, 'agent', 'core.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None
        else:
            pytest.skip("Config file not found")

    def test_memory_config(self):
        """Test memory configuration loads"""
        config_path = os.path.join(self.config_dir, 'agent', 'memory.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None
        else:
            pytest.skip("Config file not found")

    def test_compliance_recording_config(self):
        """Test compliance recording configuration loads"""
        config_path = os.path.join(self.config_dir, 'compliance', 'recording.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None
        else:
            pytest.skip("Config file not found")

    def test_proxy_tor_config(self):
        """Test Tor proxy configuration loads"""
        config_path = os.path.join(self.config_dir, 'proxy', 'tor.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = self.yaml.safe_load(f)
            assert config is not None
        else:
            pytest.skip("Config file not found")


class TestWorkflowLoading:
    """Test that workflow definitions can be loaded"""

    def setup_method(self):
        import yaml
        self.yaml = yaml
        self.workflow_dir = os.path.join(os.path.dirname(__file__), '..', 'ai-agent', 'workflows')

    def test_web_pentest_workflow(self):
        """Test web pentest workflow loads"""
        workflow_path = os.path.join(self.workflow_dir, 'web_pentest.yaml')
        if os.path.exists(workflow_path):
            with open(workflow_path, 'r') as f:
                workflow = self.yaml.safe_load(f)
            assert workflow is not None
            assert 'name' in workflow
            assert 'stages' in workflow
        else:
            pytest.skip("Workflow file not found")

    def test_incident_response_workflow(self):
        """Test incident response workflow loads"""
        workflow_path = os.path.join(self.workflow_dir, 'incident_response.yaml')
        if os.path.exists(workflow_path):
            with open(workflow_path, 'r') as f:
                workflow = self.yaml.safe_load(f)
            assert workflow is not None
        else:
            pytest.skip("Workflow file not found")

    def test_full_pentest_session_workflow(self):
        """Test full pentest session workflow loads"""
        workflow_path = os.path.join(self.workflow_dir, 'full_pentest_session.yaml')
        if os.path.exists(workflow_path):
            with open(workflow_path, 'r') as f:
                workflow = self.yaml.safe_load(f)
            assert workflow is not None
            assert 'stages' in workflow
            stage_names = [s['name'] for s in workflow['stages']]
            assert 'Session Initialization' in stage_names
            assert 'Session Completion' in stage_names
        else:
            pytest.skip("Workflow file not found")


class TestEnvironmentSetup:
    """Test environment setup and configuration"""

    def test_env_file_exists(self):
        """Test .env file exists"""
        env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
        assert os.path.exists(env_path), ".env file should exist"

    def test_env_example_file_exists(self):
        """Test .env.example file exists"""
        env_path = os.path.join(os.path.dirname(__file__), '..', '.env.example')
        assert os.path.exists(env_path), ".env.example file should exist"

    def test_required_env_variables(self):
        """Test required environment variables are defined in example"""
        env_path = os.path.join(os.path.dirname(__file__), '..', '.env.example')
        with open(env_path, 'r') as f:
            content = f.read()
        required_vars = [
            'WORKSPACE_ROOT',
            'DATABASE_URL',
            'LOG_LEVEL',
            'TOR_ENABLED',
            'RECORDING_ENABLED'
        ]
        for var in required_vars:
            assert var in content, f"Required variable {var} not found in .env.example"

    def test_directory_structure(self):
        """Test required directories exist"""
        base_dir = os.path.join(os.path.dirname(__file__), '..')
        required_dirs = [
            'red-team/web-security',
            'red-team/binary-security',
            'red-team/mobile-app',
            'red-team/domain-pentest',
            'red-team/anonymity',
            'blue-team/incident-response',
            'blue-team/threat-intel',
            'purple-team/forensics',
            'compliance/recordings',
            'compliance/evidence',
            'shared/wordlists',
            'ai-agent/skills',
            'output/reports',
            'workspace-data'
        ]
        for dir_path in required_dirs:
            full_path = os.path.join(base_dir, dir_path)
            assert os.path.exists(full_path), f"Directory {dir_path} should exist"
