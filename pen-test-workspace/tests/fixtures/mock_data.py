"""
Test fixtures for mock data
Provides mock data for various security testing scenarios
"""
from datetime import datetime, timedelta
import json


MOCK_NMAP_OUTPUT = """
Starting Nmap 7.94 ( https://nmap.org ) at 2024-01-15 10:00 UTC
Nmap scan report for test.example.com (192.0.2.1)
Host is up (0.0010s latency).

PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https
3306/tcp open   mysql

Nmap done: 1 IP address (1 host up) scanned in 0.50 seconds
"""


MOCK_BURP_SCAN_RESULTS = {
    "issue": [
        {
            "name": "SQL injection",
            "severity": "high",
            "confidence": "certain",
            "issueDetail": "The parameter 'id' appears to be vulnerable to SQL injection attacks",
            "url": "http://test.example.com/product?id=1",
            "remedy": "Sanitize user input and use parameterized queries"
        },
        {
            "name": "Cross-site scripting (reflected)",
            "severity": "medium",
            "confidence": "firm",
            "issueDetail": "The 'search' parameter appears to reflect user input without sanitization",
            "url": "http://test.example.com/search?q=test",
            "remedy": "Encode output and implement Content Security Policy"
        }
    ]
}


MOCK_SQLMAP_OUTPUT = """
[INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable
[INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable
[INFO] heuristic (parsing) test shows that backend DBMS might be MySQL
[CRITICAL] all parameters appear to be injectable
[INFO] confirming MySQL
[INFO] the back-end DBMS is MySQL >= 5.0
[CRITICAL] sqlmap identified the following injection point(s) with a total of 103 HTTP(s) requests:

Payload: id=1 AND 1234=1234

Database: users
Table: users
[2 entries]
+----+----------+------------------+
| id | username | password         |
+----+----------+------------------+
| 1  | admin    | admin123         |
| 2  | testuser | test456          |
+----+----------+------------------+
"""


MOCK_MEMORY_DUMP = {
    "processes": [
        {
            "pid": 1234,
            "name": "suspicious.exe",
            "path": "C:\\Windows\\Temp\\suspicious.exe",
            "md5": "d41d8cd98f00b204e9800998ecf8427e"
        },
        {
            "pid": 5678,
            "name": "notepad.exe",
            "path": "C:\\Windows\\System32\\notepad.exe",
            "md5": "098f6bcd4621d373cade4e832627b4f6"
        }
    ],
    "network_connections": [
        {
            "local_addr": "192.168.1.100",
            "local_port": 49152,
            "remote_addr": "192.0.2.1",
            "remote_port": 443,
            "state": "ESTABLISHED"
        }
    ]
}


MOCK_LOG_DATA = {
    "auth_log": [
        {
            "timestamp": "2024-01-15T09:00:00Z",
            "event": "ssh_login",
            "user": "root",
            "ip": "192.0.2.100",
            "status": "success"
        },
        {
            "timestamp": "2024-01-15T09:01:00Z",
            "event": "ssh_login",
            "user": "admin",
            "ip": "10.0.0.50",
            "status": "failed"
        }
    ],
    "web_access_log": [
        {
            "timestamp": "2024-01-15T10:30:00Z",
            "method": "GET",
            "path": "/admin/config",
            "status": 200,
            "ip": "192.0.2.50"
        },
        {
            "timestamp": "2024-01-15T10:31:00Z",
            "method": "POST",
            "path": "/login",
            "status": 302,
            "ip": "192.0.2.50"
        }
    ]
}


MOCK_VULNERABILITY_DB = [
    {
        "cve_id": "CVE-2024-1234",
        "description": "SQL Injection in /search endpoint",
        "cvss_score": 9.1,
        "affected_component": "web_application",
        "remediation": "Use parameterized queries",
        "references": ["https://nvd.nist.gov/vuln/detail/CVE-2024-1234"]
    },
    {
        "cve_id": "CVE-2024-5678",
        "description": "XSS in comment field",
        "cvss_score": 6.1,
        "affected_component": "web_application",
        "remediation": "Encode user input in output",
        "references": ["https://nvd.nist.gov/vuln/detail/CVE-2024-5678"]
    },
    {
        "cve_id": "CVE-2024-9012",
        "description": "Outdated OpenSSL version (1.0.2k)",
        "cvss_score": 7.5,
        "affected_component": "openssl",
        "remediation": "Upgrade to OpenSSL 1.1.1 or later",
        "references": ["https://nvd.nist.gov/vuln/detail/CVE-2024-9012"]
    }
]


MOCK_THREAT_INTEL = {
    "malicious_ips": [
        {"ip": "192.0.2.1", "score": 90, "source": "alienvault_otx"},
        {"ip": "192.0.2.2", "score": 85, "source": "abuseipdb"}
    ],
    "malicious_domains": [
        {"domain": "evil.com", "score": 95, "source": "threatfox"},
        {"domain": "malware-download.com", "score": 88, "source": "malware Bazaar"}
    ],
    "malware_hashes": [
        {"hash": "abc123def456", "type": "md5", "name": "Trojan.Generic", "source": "virustotal"},
        {"hash": "789ghi012jkl", "type": "sha256", "name": "Ransomware.Crypto", "source": "hybrid_analysis"}
    ]
}


MOCK_COMPLIANCE_DATA = {
    "gdpr": {
        "data_controller": "Example Corp",
        "data_processor": "Example Processing Ltd",
        "dpo_registered": True,
        "data_retention_policy": "90_days",
        "consent_mechanism": "explicit_opt_in"
    },
    "hipaa": {
        "covered_entity": "Healthcare Example Inc",
        "business_associates": 3,
        "phi_systems": ["EHR", "Billing", "Lab"],
        "risk_assessment_current": True
    },
    "pci_dss": {
        "merchant_level": 2,
        "last_audit": "2024-01-01",
        "cardholder_data_environment": "segmented",
        "encryption_standard": "AES-256"
    }
}


MOCK_REPORT_TEMPLATE = {
    "executive_summary": {
        "project_name": "Security Assessment Report",
        "date": "2024-01-15",
        "prepared_for": "Example Organization",
        "prepared_by": "Security Team",
        "overall_risk": "Medium"
    },
    "methodology": [
        "Information Gathering",
        "Threat Modeling",
        "Vulnerability Analysis",
        "Exploitation",
        "Post-Exploitation",
        "Reporting"
    ],
    "finding_template": {
        "title": "Finding Title",
        "severity": "Critical/High/Medium/Low/Informational",
        "cvss_score": 0.0,
        "description": "Detailed description of the finding",
        "impact": "Business impact analysis",
        "remediation": "Recommended fix",
        "evidence": [],
        "references": []
    }
}


def generate_mock_scan_result(host, open_ports=None):
    """Generate mock scan result for a host"""
    if open_ports is None:
        open_ports = [22, 80, 443]

    return {
        "host": host,
        "scan_time": datetime.now().isoformat(),
        "open_ports": [
            {"port": port, "state": "open", "service": "http" if port == 80 else "ssh" if port == 22 else "https"}
            for port in open_ports
        ]
    }


def generate_mock_incident_timeline(events=None):
    """Generate mock incident timeline"""
    if events is None:
        events = [
            {"time": "2024-01-15T09:00:00Z", "event": "initial_access", "description": "First intrusion detected"},
            {"time": "2024-01-15T09:30:00Z", "event": "lateral_movement", "description": "Attacker moved to internal systems"},
            {"time": "2024-01-15T10:00:00Z", "event": "data_exfiltration", "description": "Sensitive data accessed"},
            {"time": "2024-01-15T10:30:00Z", "event": "detection", "description": "Security team notified"}
        ]

    return {
        "incident_id": "INC-2024-001",
        "timeline": events,
        "total_duration": "1h 30m"
    }


def get_mock_tool_output(tool_name):
    """Get mock output for a specific tool"""
    tool_outputs = {
        "nmap": MOCK_NMAP_OUTPUT,
        "burp": MOCK_BURP_SCAN_RESULTS,
        "sqlmap": MOCK_SQLMAP_OUTPUT,
        "memory_dump": MOCK_MEMORY_DUMP,
        "logs": MOCK_LOG_DATA,
        "vuln_db": MOCK_VULNERABILITY_DB,
        "threat_intel": MOCK_THREAT_INTEL
    }

    return tool_outputs.get(tool_name, {})
