"""
Test fixtures package
Provides sample data and target configurations for testing
"""
from .sample_targets import (
    WEB_PENTEST_TARGETS,
    NETWORK_PENTEST_TARGETS,
    INCIDENT_RESPONSE_TARGETS,
    MOBILE_PENTEST_TARGETS,
    get_target,
    get_all_targets,
    validate_target
)

from .mock_data import (
    MOCK_NMAP_OUTPUT,
    MOCK_BURP_SCAN_RESULTS,
    MOCK_SQLMAP_OUTPUT,
    MOCK_MEMORY_DUMP,
    MOCK_LOG_DATA,
    MOCK_VULNERABILITY_DB,
    MOCK_THREAT_INTEL,
    MOCK_COMPLIANCE_DATA,
    generate_mock_scan_result,
    generate_mock_incident_timeline,
    get_mock_tool_output
)

__all__ = [
    'WEB_PENTEST_TARGETS',
    'NETWORK_PENTEST_TARGETS',
    'INCIDENT_RESPONSE_TARGETS',
    'MOBILE_PENTEST_TARGETS',
    'get_target',
    'get_all_targets',
    'validate_target',
    'MOCK_NMAP_OUTPUT',
    'MOCK_BURP_SCAN_RESULTS',
    'MOCK_SQLMAP_OUTPUT',
    'MOCK_MEMORY_DUMP',
    'MOCK_LOG_DATA',
    'MOCK_VULNERABILITY_DB',
    'MOCK_THREAT_INTEL',
    'MOCK_COMPLIANCE_DATA',
    'generate_mock_scan_result',
    'generate_mock_incident_timeline',
    'get_mock_tool_output'
]
