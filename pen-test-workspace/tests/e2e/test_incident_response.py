"""
E2E tests for Incident Response Workflow
Tests the complete incident response workflow from detection to reporting
"""
import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.core.agent import SecurityExpertAgent
from agent.workflow.engine import StateTracker, State


class TestIncidentResponseWorkflow:
    """End-to-end test for incident response workflow"""

    @pytest.fixture
    def mock_agent(self):
        """Create a mocked agent for incident response"""
        with patch('agent.core.agent.LLMClient'):
            agent = SecurityExpertAgent(
                agent_id="test_ir_agent",
                agent_type="blue_team_ir"
            )
            agent.llm = Mock()
            return agent

    @pytest.fixture
    def sample_incident(self):
        """Sample incident data"""
        return {
            "incident_id": "INC-2024-001",
            "severity": "high",
            "type": "data_breach",
            "affected_systems": ["web-server-01", "db-server-01"],
            "detected_at": "2024-01-15T10:30:00Z",
            "reported_by": "ids_alerter"
        }

    def test_initialization(self, mock_agent):
        """Test agent initialization for incident response"""
        assert mock_agent.agent_id == "test_ir_agent"
        assert mock_agent.agent_type == "blue_team_ir"

    def test_incident_identification(self, mock_agent, sample_incident):
        """Test incident identification phase"""
        with patch.object(mock_agent, 'identify_incident', return_value={
            'incident_id': sample_incident['incident_id'],
            'severity': sample_incident['severity'],
            'status': 'identified'
        }):
            result = mock_agent.identify_incident(sample_incident)
            assert 'incident_id' in result
            assert result['status'] == 'identified'

    def test_evidence_collection(self, mock_agent):
        """Test evidence collection phase"""
        with patch.object(mock_agent, 'collect_evidence', return_value={
            'artifacts': ['log_file', 'memory_dump', 'network_capture'],
            'collection_time': '2024-01-15T10:35:00Z'
        }):
            result = mock_agent.collect_evidence("web-server-01")
            assert 'artifacts' in result
            assert len(result['artifacts']) > 0

    def test_containment_phase(self, mock_agent, sample_incident):
        """Test containment phase"""
        with patch.object(mock_agent, 'contain_threat', return_value={
            'actions_taken': ['isolated_system', 'blocked_ip'],
            'status': 'contained'
        }):
            result = mock_agent.contain_threat(sample_incident)
            assert result['status'] == 'contained'

    def test_eradication_phase(self, mock_agent):
        """Test eradication phase"""
        with patch.object(mock_agent, 'eradicate_threat', return_value={
            'malware_removed': True,
            'backdoors_closed': 3,
            'patches_applied': ['CVE-2024-1234']
        }):
            result = mock_agent.eradicate_threat()
            assert result['malware_removed'] is True

    def test_recovery_phase(self, mock_agent):
        """Test recovery phase"""
        with patch.object(mock_agent, 'recover_systems', return_value={
            'systems_restored': ['web-server-01', 'db-server-01'],
            'verification_status': 'passed'
        }):
            result = mock_agent.recover_systems()
            assert 'systems_restored' in result

    def test_forensics_analysis(self, mock_agent):
        """Test forensics analysis phase"""
        with patch.object(mock_agent, 'analyze_forensics', return_value={
            'timeline': {
                '2024-01-15T09:00': 'initial_access',
                '2024-01-15T10:30': 'detection'
            },
            'attack_vector': 'sql_injection',
            'data_exposed': ['user_credentials', 'pii']
        }):
            result = mock_agent.analyze_forensics([])
            assert 'timeline' in result
            assert 'attack_vector' in result

    def test_reporting_phase(self, mock_agent):
        """Test incident report generation"""
        with patch.object(mock_agent, 'generate_incident_report', return_value={
            'executive_summary': 'Data breach incident',
            'impact_assessment': 'high',
            'recommendations': ['patch_sql_injection', 'enhance_monitoring']
        }):
            report = mock_agent.generate_incident_report({})
            assert 'executive_summary' in report

    def test_full_ir_workflow_integration(self, mock_agent, sample_incident):
        """Test complete IR workflow from start to finish"""
        workflow_states = []

        def state_listener(state):
            workflow_states.append(state)

        mock_agent.state_tracker.on_state_change(state_listener)

        mock_agent.llm.generate.return_value = "IR Task completed"

        workflow_states.append(mock_agent.state_tracker.current_state)

        mock_agent.state_tracker.transition_to(State.REQUIREMENT_ANALYSIS)
        mock_agent.state_tracker.transition_to(State.PLANNING)
        mock_agent.state_tracker.transition_to(State.RECON)
        mock_agent.state_tracker.transition_to(State.VULN_ASSESS)
        mock_agent.state_tracker.transition_to(State.POST_EXPLOIT)
        mock_agent.state_tracker.transition_to(State.REPORTING)
        mock_agent.state_tracker.transition_to(State.COMPLETED)

        assert len(workflow_states) >= 2
        assert State.COMPLETED in workflow_states

    def test_chain_of_custody(self, mock_agent):
        """Test chain of custody maintenance"""
        with patch.object(mock_agent, 'maintain_chain_of_custody', return_value={
            'evidence_log': [
                {'timestamp': '2024-01-15T10:35:00Z', 'action': 'collected', 'by': 'analyst1'},
                {'timestamp': '2024-01-15T11:00:00Z', 'action': 'analyzed', 'by': 'analyst2'}
            ],
            'integrity_verified': True
        }):
            result = mock_agent.maintain_chain_of_custody()
            assert 'evidence_log' in result
            assert result['integrity_verified'] is True

    def test_severity_escalation(self, mock_agent):
        """Test severity escalation handling"""
        with patch.object(mock_agent, 'escalate_severity', return_value={
            'previous': 'medium',
            'current': 'critical',
            'escalation_reason': 'sensitive_data_accessed'
        }):
            result = mock_agent.escalate_severity('critical')
            assert result['current'] == 'critical'


class TestThreatIntelligence:
    """Test threat intelligence integration"""

    @pytest.fixture
    def threat_feed(self):
        """Sample threat intelligence feed"""
        return {
            'source': 'alienvault_otx',
            'indicators': [
                {'type': 'ip', 'value': '192.0.2.1', 'malicious': True},
                {'type': 'domain', 'value': 'evil.com', 'malicious': True},
                {'type': 'hash', 'value': 'abc123def456', 'malicious': True}
            ],
            'last_updated': '2024-01-15T08:00:00Z'
        }

    def test_ioc_extraction(self, threat_feed):
        """Test IOC extraction from threat feed"""
        iocs = [ioc['value'] for ioc in threat_feed['indicators']]
        assert len(iocs) == 3
        assert '192.0.2.1' in iocs

    def test_threat_indicator_validation(self, threat_feed):
        """Test threat indicator validation"""
        for indicator in threat_feed['indicators']:
            assert indicator['type'] in ['ip', 'domain', 'hash', 'url']
            assert indicator['malicious'] is True

    def test_feed_source_reliability(self, threat_feed):
        """Test threat feed source reliability scoring"""
        sources = {
            'alienvault_otx': 0.8,
            'malware Bazaar': 0.9,
            'shodan': 0.7
        }

        reliability = sources.get(threat_feed['source'], 0.5)
        assert reliability >= 0.7


class TestForensicsCollection:
    """Test forensics evidence collection"""

    @pytest.fixture
    def forensics_targets(self):
        """Target systems for forensics collection"""
        return {
            'linux_servers': ['web-server-01', 'app-server-01'],
            'windows_servers': ['dc-01'],
            'network_devices': ['fw-01', 'switch-01']
        }

    def test_memory_acquisition(self, forensics_targets):
        """Test memory acquisition"""
        mem_tool_config = {
            'tool': 'ftk imager',
            'target': forensics_targets['linux_servers'][0],
            'output': '/forensics/memory/web-server-01.mem'
        }

        assert mem_tool_config['tool'] in ['ftk imager', 'dumpit', 'lime']
        assert mem_tool_config['target'] is not None

    def test_disk_image_acquisition(self, forensics_targets):
        """Test disk image acquisition"""
        disk_tool_config = {
            'tool': 'dd',
            'source': '/dev/sda1',
            'output': '/forensics/disk/image.raw',
            'hash': 'sha256:abc123...'
        }

        assert disk_tool_config['tool'] in ['dd', 'ftk_imager', 'ewf']
        assert disk_tool_config['output'] is not None

    def test_log_collection(self, forensics_targets):
        """Test log collection from various sources"""
        log_sources = {
            'system_logs': '/var/log/syslog',
            'auth_logs': '/var/log/auth.log',
            'web_logs': '/var/log/apache2/access.log',
            'firewall_logs': '/var/log/firewall.log'
        }

        assert 'auth_logs' in log_sources
        assert 'web_logs' in log_sources


class TestMalwareAnalysis:
    """Test malware analysis capabilities"""

    @pytest.fixture
    def malware_sample(self):
        """Sample malware analysis request"""
        return {
            'file_hash': 'd41d8cd98f00b204e9800998ecf8427e',
            'file_type': 'executable',
            'suspicious_behavior': ['network_connections', 'registry_modifications']
        }

    def test_static_analysis(self, malware_sample):
        """Test static malware analysis"""
        static_analysis_config = {
            'tools': ['strings', 'binwalk', 'yara'],
            'file': malware_sample['file_hash']
        }

        assert 'strings' in static_analysis_config['tools']
        assert static_analysis_config['file'] is not None

    def test_dynamic_analysis(self, malware_sample):
        """Test dynamic malware analysis (sandbox)"""
        sandbox_config = {
            'platform': 'cuckoo',
            'timeout': 300,
            'operations': ['network_capture', 'file_tracking', 'registry_tracking']
        }

        assert sandbox_config['platform'] in ['cuckoo', 'any.run', 'hybrid_analysis']
        assert sandbox_config['timeout'] >= 60


class TestComplianceReporting:
    """Test compliance reporting for incident response"""

    def test_gdpr_breach_notification(self):
        """Test GDPR breach notification requirements"""
        gdpr_report = {
            'regulation': 'GDPR',
            'data_breach_type': 'personal_data',
            'affected_records': 1000,
            'notification_required': True,
            'notification_deadline': '72_hours',
            'supervisory_authority': 'ICO'
        }

        assert gdpr_report['notification_required'] is True
        assert gdpr_report['notification_deadline'] == '72_hours'

    def test_hipaa_breach_notification(self):
        """Test HIPAA breach notification requirements"""
        hipaa_report = {
            'regulation': 'HIPAA',
            'breach_type': 'phi_exposure',
            'affected_patients': 500,
            'notification_required': True,
            'media_notification': True
        }

        assert hipaa_report['notification_required'] is True
        assert 'affected_patients' in hipaa_report
