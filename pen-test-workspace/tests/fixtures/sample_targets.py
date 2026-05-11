"""
Test fixtures for sample targets
Provides sample target configurations for various security testing scenarios
"""
import os


WEB_PENTEST_TARGETS = {
    "simple_target": {
        "name": "Simple Web Application",
        "target_url": "http://test.example.com",
        "scope": ["test.example.com"],
        "test_type": "web_pentest",
        "auth_required": False,
        "technologies": ["Apache", "PHP", "MySQL"]
    },
    "authenticated_target": {
        "name": "Authenticated Web Application",
        "target_url": "https://secure.example.com",
        "scope": ["secure.example.com"],
        "test_type": "web_pentest",
        "auth_required": True,
        "auth_type": "form",
        "login_url": "https://secure.example.com/login",
        "username_field": "email",
        "password_field": "password",
        "technologies": ["Nginx", "Django", "PostgreSQL"]
    },
    "api_target": {
        "name": "REST API",
        "target_url": "https://api.example.com",
        "scope": ["api.example.com"],
        "test_type": "api_pentest",
        "auth_required": True,
        "auth_type": "bearer_token",
        "endpoints": [
            "/api/v1/users",
            "/api/v1/orders",
            "/api/v1/products"
        ],
        "technologies": ["Node.js", "Express", "MongoDB"]
    }
}


NETWORK_PENTEST_TARGETS = {
    "internal_network": {
        "name": "Internal Network",
        "scope": ["192.168.1.0/24"],
        "test_type": "network_pentest",
        "targets": [
            "192.168.1.1",
            "192.168.1.10",
            "192.168.1.100"
        ]
    },
    "external_network": {
        "name": "External Infrastructure",
        "scope": ["203.0.113.0/28"],
        "test_type": "network_pentest",
        "targets": [
            "203.0.113.1",
            "203.0.113.14"
        ]
    }
}


INCIDENT_RESPONSE_TARGETS = {
    "data_breach": {
        "incident_id": "INC-2024-001",
        "severity": "high",
        "type": "data_breach",
        "affected_systems": ["web-server-01", "db-server-01"],
        "detected_at": "2024-01-15T10:30:00Z",
        "reported_by": "ids_alerter"
    },
    "malware_infection": {
        "incident_id": "INC-2024-002",
        "severity": "medium",
        "type": "malware_infection",
        "affected_systems": ["workstation-05"],
        "detected_at": "2024-01-16T14:20:00Z",
        "reported_by": "antivirus"
    },
    "phishing_attack": {
        "incident_id": "INC-2024-003",
        "severity": "low",
        "type": "phishing",
        "affected_systems": ["email_server"],
        "detected_at": "2024-01-17T09:00:00Z",
        "reported_by": "user_report"
    }
}


MOBILE_PENTEST_TARGETS = {
    "android_app": {
        "name": "Android Banking App",
        "platform": "android",
        "package_name": "com.example.banking",
        "test_type": "mobile_pentest",
        "apk_path": "/testapps/android-banking.apk",
        "testing_mode": "static"
    },
    "ios_app": {
        "name": "iOS Commerce App",
        "platform": "ios",
        "bundle_id": "com.example.commerce",
        "test_type": "mobile_pentest",
        "ipa_path": "/testapps/ios-commerce.ipa",
        "testing_mode": "dynamic"
    }
}


def get_target(target_type, target_name):
    """Get a specific target configuration"""
    targets_map = {
        'web': WEB_PENTEST_TARGETS,
        'network': NETWORK_PENTEST_TARGETS,
        'incident': INCIDENT_RESPONSE_TARGETS,
        'mobile': MOBILE_PENTEST_TARGETS
    }

    target_category = targets_map.get(target_type, {})
    return target_category.get(target_name)


def get_all_targets():
    """Get all available targets"""
    return {
        'web': WEB_PENTEST_TARGETS,
        'network': NETWORK_PENTEST_TARGETS,
        'incident': INCIDENT_RESPONSE_TARGETS,
        'mobile': MOBILE_PENTEST_TARGETS
    }


def validate_target(target):
    """Validate a target configuration"""
    required_fields = ['name', 'scope', 'test_type']

    for field in required_fields:
        if field not in target:
            return False, f"Missing required field: {field}"

    return True, "Valid target"
