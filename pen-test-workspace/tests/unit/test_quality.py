"""Tests for Quality Control System"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.quality.quality_control import Validator, Auditor, SelfAssessment


class TestValidator:
    """Test validation functionality"""

    def setup_method(self):
        self.validator = Validator()

    def test_validator_initialization(self):
        assert self.validator is not None

    def test_store_validation_result(self):
        """Test storing validation results"""
        result = {"status": "pass", "check_type": "completeness"}
        self.validator.store(result, key="check_1")
        assert self.validator.retrieve("check_1") == result

    def test_valid_check(self):
        """Test validation with valid data"""
        finding = {
            "title": "SQL Injection",
            "severity": "high",
            "description": "Test description",
            "evidence": "PoC",
            "remediation": "Fix"
        }
        self.validator.store(finding, key="finding_1")
        retrieved = self.validator.retrieve("finding_1")
        assert retrieved["title"] == "SQL Injection"

    def test_multiple_validations(self):
        """Test multiple validation results"""
        self.validator.store({"status": "pass"}, key="v1")
        self.validator.store({"status": "fail"}, key="v2")
        assert self.validator.retrieve("v1")["status"] == "pass"
        assert self.validator.retrieve("v2")["status"] == "fail"


class TestAuditor:
    """Test auditing functionality"""

    def setup_method(self):
        self.auditor = Auditor()

    def test_auditor_initialization(self):
        assert self.auditor is not None

    def log_action(self):
        """Test logging audit action"""
        action = {
            "type": "scan",
            "tool": "nmap",
            "target": "192.168.1.1",
            "result": "success"
        }
        self.auditor.store(action, key="audit_1")
        assert self.auditor.retrieve("audit_1") == action

    def log_decision(self):
        """Test logging audit decision"""
        decision = {
            "type": "proceed",
            "reason": "Vulnerability confirmed"
        }
        self.auditor.store(decision, key="decision_1")
        assert self.auditor.retrieve("decision_1") == decision


class TestSelfAssessment:
    """Test self-assessment functionality"""

    def setup_method(self):
        self.assessment = SelfAssessment()

    def test_self_assessment_initialization(self):
        assert self.assessment is not None

    def test_store_metric(self):
        """Test storing performance metric"""
        metric = {"name": "scan_speed", "value": 100, "unit": "hosts/min"}
        self.assessment.store(metric, key="perf_1")
        assert self.assessment.retrieve("perf_1") == metric

    def test_multiple_metrics(self):
        """Test storing multiple metrics"""
        self.assessment.store({"name": "m1", "value": 1}, key="metric_1")
        self.assessment.store({"name": "m2", "value": 2}, key="metric_2")
        assert self.assessment.retrieve("metric_1")["name"] == "m1"
        assert self.assessment.retrieve("metric_2")["name"] == "m2"
