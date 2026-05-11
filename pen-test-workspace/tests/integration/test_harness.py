"""
Integration tests for Harness Framework
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from ai_agent.harness.harness import (
    WebSecurityHarness,
    BinaryHarness,
    DomainPentestHarness,
    IncidentResponseHarness,
    ForensicsHarness,
    AnonymityHarness,
    ComplianceHarness,
    SessionHarness,
    GenericHarness
)


class TestWebSecurityHarness:
    """Test WebSecurityHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = WebSecurityHarness({
            'target': 'https://example.com'
        })
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.target == 'https://example.com'
        assert isinstance(self.harness.results, list)
    
    def test_run_full_scan(self):
        """Test running full scan"""
        results = self.harness.run_full_scan()
        
        assert 'target' in results
        assert 'phases' in results
        assert results['target'] == 'https://example.com'
    
    def test_test_sqli(self):
        """Test SQL injection testing"""
        result = self.harness.test_sqli()
        
        assert 'test' in result
        assert result['test'] == 'sqli'
    
    def test_test_xss(self):
        """Test XSS testing"""
        result = self.harness.test_xss()
        
        assert 'test' in result
        assert result['test'] == 'xss'
    
    def test_get_results(self):
        """Test getting results"""
        results = self.harness.get_results()
        
        assert isinstance(results, list)


class TestBinaryHarness:
    """Test BinaryHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = BinaryHarness(
            '/tmp/test_binary',
            {'config': 'value'}
        )
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.binary_path == '/tmp/test_binary'
        assert isinstance(self.harness.crashes, list)
    
    def test_fuzz(self):
        """Test fuzzing"""
        result = self.harness.fuzz(iterations=10)
        
        assert 'iterations' in result
        assert result['iterations'] == 10
    
    def test_analyze_crash(self):
        """Test crash analysis"""
        result = self.harness.analyze_crash(b'test_input')
        
        assert 'crash' in result
        assert 'type' in result
    
    def test_generate_exploit_template(self):
        """Test exploit template generation"""
        crash_info = {'type': 'buffer_overflow'}
        template = self.harness.generate_exploit_template(crash_info)
        
        assert isinstance(template, str)
    
    def test_verify_exploit(self):
        """Test exploit verification"""
        result = self.harness.verify_exploit("# exploit code")
        
        assert 'verified' in result


class TestDomainPentestHarness:
    """Test DomainPentestHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = DomainPentestHarness({
            'domain': 'test.local',
            'username': 'admin',
            'password': 'password'
        })
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.domain == 'test.local'
        assert hasattr(self.harness, 'loot')
    
    def test_reconnaissance(self):
        """Test reconnaissance phase"""
        result = self.harness.reconnaissance()
        
        assert 'phase' in result
        assert result['phase'] == 'recon'
    
    def test_initial_access(self):
        """Test initial access phase"""
        result = self.harness.initial_access()
        
        assert 'phase' in result
    
    def test_privilege_escalation(self):
        """Test privilege escalation"""
        result = self.harness.privilege_escalation()
        
        assert 'phase' in result
    
    def test_lateral_movement(self):
        """Test lateral movement"""
        result = self.harness.lateral_movement()
        
        assert 'phase' in result
    
    def test_persistence(self):
        """Test persistence establishment"""
        result = self.harness.persistence()
        
        assert 'phase' in result
    
    def test_collection(self):
        """Test data collection"""
        result = self.harness.collection()
        
        assert 'phase' in result


class TestIncidentResponseHarness:
    """Test IncidentResponseHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = IncidentResponseHarness({
            'incident_id': 'INC-001'
        })
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.incident_id == 'INC-001'
        assert isinstance(self.harness.evidence, list)
    
    def test_preparation(self):
        """Test preparation phase"""
        result = self.harness.preparation()
        
        assert 'phase' in result
    
    def test_identification(self):
        """Test identification phase"""
        result = self.harness.identification()
        
        assert 'phase' in result
    
    def test_containment(self):
        """Test containment phase"""
        result = self.harness.containment()
        
        assert 'phase' in result
    
    def test_eradication(self):
        """Test eradication phase"""
        result = self.harness.eradication()
        
        assert 'phase' in result
    
    def test_recovery(self):
        """Test recovery phase"""
        result = self.harness.recovery()
        
        assert 'phase' in result
    
    def test_lessons_learned(self):
        """Test lessons learned phase"""
        result = self.harness.lessons_learned()
        
        assert 'phase' in result


class TestForensicsHarness:
    """Test ForensicsHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = ForensicsHarness({
            'case_id': 'CASE-001'
        })
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.case_id == 'CASE-001'
    
    def test_acquire_evidence(self):
        """Test evidence acquisition"""
        result = self.harness.acquire_evidence('/dev/sda', 'disk')
        
        assert 'source' in result
        assert 'type' in result
    
    def test_validate_integrity(self):
        """Test integrity validation"""
        result = self.harness.validate_integrity('/path/to/evidence')
        
        assert 'evidence' in result
        assert 'valid' in result
    
    def test_process_artifacts(self):
        """Test artifact processing"""
        result = self.harness.process_artifacts()
        
        assert 'artifacts_processed' in result
    
    def test_build_timeline(self):
        """Test timeline building"""
        result = self.harness.build_timeline()
        
        assert 'events' in result
    
    def test_correlate_events(self):
        """Test event correlation"""
        result = self.harness.correlate_events()
        
        assert 'correlations' in result
    
    def test_generate_report(self):
        """Test report generation"""
        report = self.harness.generate_report()
        
        assert isinstance(report, str)


class TestAnonymityHarness:
    """Test AnonymityHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = AnonymityHarness({'config': 'value'})
    
    def test_initialization(self):
        """Test harness initialization"""
        assert isinstance(self.harness.active_proxies, list)
        assert self.harness.anonymity_level == 0
    
    def test_setup_tor_network(self):
        """Test Tor network setup"""
        result = self.harness.setup_tor_network()
        
        assert 'tor' in result
    
    def test_setup_proxy_chain(self):
        """Test proxy chain setup"""
        proxies = [{'host': '127.0.0.1', 'port': 9050}]
        result = self.harness.setup_proxy_chain(proxies)
        
        assert 'proxies' in result
    
    def test_connect_vpn(self):
        """Test VPN connection"""
        result = self.harness.connect_vpn({'config': 'value'})
        
        assert 'vpn' in result
    
    def test_disconnect_vpn(self):
        """Test VPN disconnection"""
        result = self.harness.disconnect_vpn()
        
        assert 'vpn' in result
    
    def test_anonymize_system(self):
        """Test system anonymization"""
        result = self.harness.anonymize_system()
        
        assert 'system' in result
    
    def test_check_ip_leak(self):
        """Test IP leak check"""
        result = self.harness.check_ip_leak()
        
        assert 'leak_detected' in result
    
    def test_check_dns_leak(self):
        """Test DNS leak check"""
        result = self.harness.check_dns_leak()
        
        assert 'dns_leak' in result
    
    def test_cleanup(self):
        """Test cleanup"""
        result = self.harness.cleanup()
        
        assert 'status' in result


class TestComplianceHarness:
    """Test ComplianceHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = ComplianceHarness({
            'session_id': 'SESSION-001'
        })
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.session_id == 'SESSION-001'
    
    def test_start_session(self):
        """Test starting session"""
        result = self.harness.start_session()
        
        assert 'session_id' in result
        assert result['started'] is True
    
    def test_start_all_recordings(self):
        """Test starting all recordings"""
        result = self.harness.start_all_recordings()
        
        assert 'recordings' in result
    
    def test_stop_all_recordings(self):
        """Test stopping all recordings"""
        self.harness.start_all_recordings()
        result = self.harness.stop_all_recordings()
        
        assert 'recordings' in result
    
    def test_collect_evidence(self):
        """Test evidence collection"""
        result = self.harness.collect_evidence('/path', 'file')
        
        assert 'evidence_id' in result
    
    def test_verify_evidence_integrity(self):
        """Test evidence integrity verification"""
        result = self.harness.verify_evidence_integrity()
        
        assert 'verified' in result
    
    def test_end_session(self):
        """Test ending session"""
        result = self.harness.end_session()
        
        assert 'session_id' in result
        assert result['ended'] is True


class TestSessionHarness:
    """Test SessionHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = SessionHarness({'config': 'value'})
    
    def test_initialization(self):
        """Test harness initialization"""
        assert hasattr(self.harness, 'session_id')
    
    def test_initialize(self):
        """Test initialization"""
        result = self.harness.initialize()
        
        assert 'session_id' in result
        assert 'initialized' in result
    
    def test_setup_anonymity(self):
        """Test anonymity setup"""
        result = self.harness.setup_anonymity({})
        
        assert 'anonymity' in result
    
    def test_start_compliance_recording(self):
        """Test starting compliance recording"""
        result = self.harness.start_compliance_recording()
        
        assert 'recording' in result
    
    def test_complete_test(self):
        """Test completing test"""
        result = self.harness.complete_test()
        
        assert 'test' in result
    
    def test_finalize_session(self):
        """Test finalizing session"""
        result = self.harness.finalize_session()
        
        assert 'session_id' in result
    
    def test_generate_final_report(self):
        """Test generating final report"""
        report = self.harness.generate_final_report()
        
        assert isinstance(report, str)


class TestGenericHarness:
    """Test GenericHarness class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.harness = GenericHarness({'config': 'value'})
    
    def test_initialization(self):
        """Test harness initialization"""
        assert self.harness.state == 'initialized'
        assert isinstance(self.harness.logs, list)
    
    def test_setup(self):
        """Test setup"""
        result = self.harness.setup()
        
        assert 'state' in result
    
    def test_execute(self):
        """Test execution"""
        result = self.harness.execute()
        
        assert 'state' in result
    
    def test_teardown(self):
        """Test teardown"""
        result = self.harness.teardown()
        
        assert 'state' in result
    
    def test_validate(self):
        """Test validation"""
        result = self.harness.validate()
        
        assert 'valid' in result
    
    def test_run_workflow(self):
        """Test workflow execution"""
        workflow = [
            {'step': 1},
            {'step': 2}
        ]
        result = self.harness.run_workflow(workflow)
        
        assert 'results' in result


class TestHarnessIntegration:
    """Integration tests for harness system"""
    
    def test_web_pentest_flow(self):
        """Test web pentest flow"""
        harness = WebSecurityHarness({'target': 'https://test.com'})
        
        scan_results = harness.run_full_scan()
        assert scan_results['target'] == 'https://test.com'
    
    def test_incident_response_flow(self):
        """Test incident response flow"""
        harness = IncidentResponseHarness({'incident_id': 'INC-001'})
        
        prep = harness.preparation()
        ident = harness.identification()
        
        assert prep['phase'] == 'preparation'
        assert ident['phase'] == 'identification'
    
    def test_session_with_compliance_flow(self):
        """Test session with compliance flow"""
        harness = SessionHarness({})
        
        init = harness.initialize()
        harness.start_compliance_recording()
        complete = harness.complete_test()
        finalize = harness.finalize_session()
        
        assert init['initialized'] is True
        assert complete['test'] == 'completed'
        assert finalize['finalized'] is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
