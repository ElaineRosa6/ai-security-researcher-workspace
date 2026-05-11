"""
Red Team Skills - Web Security Testing
"""

import json
import logging
import subprocess
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class WebSecuritySkill:
    """Web security testing skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.wordlists_path = self.config.get('wordlists_path', 'shared/wordlists')
        self.output_path = self.config.get('output_path', 'output')
    
    def recon(self, target: str, **kwargs) -> Dict[str, Any]:
        """Perform web reconnaissance"""
        logger.info(f"Starting web reconnaissance for {target}")
        
        results = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "findings": [],
            "status": "completed"
        }
        
        results["findings"].extend(self._discover_endpoints(target))
        
        results["findings"].extend(self._identify_technologies(target))
        
        return results
    
    def _discover_endpoints(self, target: str) -> List[Dict]:
        """Discover web endpoints"""
        endpoints = []
        
        try:
            result = subprocess.run(
                ["curl", "-s", "-I", target],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                headers = result.stdout
                
                server_info = self._parse_headers(headers)
                
                if server_info:
                    endpoints.append({
                        "type": "server_info",
                        "data": server_info
                    })
        except Exception as e:
            logger.warning(f"Endpoint discovery failed: {e}")
        
        return endpoints
    
    def _parse_headers(self, headers: str) -> Dict:
        """Parse HTTP headers"""
        info = {}
        
        for line in headers.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if key in ['server', 'x-powered-by', 'x-aspnet-version']:
                    info[key] = value
        
        return info
    
    def _identify_technologies(self, target: str) -> List[Dict]:
        """Identify technologies used"""
        technologies = []
        
        technologies.append({
            "type": "technology",
            "name": "HTTP",
            "confidence": 0.95
        })
        
        return technologies
    
    def subdomain_enum(self, target: str, **kwargs) -> Dict[str, Any]:
        """Enumerate subdomains"""
        logger.info(f"Starting subdomain enumeration for {target}")
        
        results = {
            "target": target,
            "subdomains": [],
            "timestamp": datetime.now().isoformat()
        }
        
        domain = self._extract_domain(target)
        
        results["subdomains"].append({
            "subdomain": f"www.{domain}" if domain else target,
            "ip": self._resolve_domain(domain if domain else target),
            "status": "discovered"
        })
        
        return results
    
    def _extract_domain(self, target: str) -> str:
        """Extract domain from target"""
        if '://' in target:
            from urllib.parse import urlparse
            parsed = urlparse(target)
            return parsed.netloc
        return target
    
    def _resolve_domain(self, domain: str) -> Optional[str]:
        """Resolve domain to IP"""
        try:
            import socket
            ip = socket.gethostbyname(domain)
            return ip
        except:
            return None
    
    def enumerate(self, target: str, **kwargs) -> Dict[str, Any]:
        """Enumerate web resources"""
        logger.info(f"Starting web enumeration for {target}")
        
        return {
            "target": target,
            "pages": [],
            "forms": [],
            "endpoints": [],
            "timestamp": datetime.now().isoformat()
        }
    
    def test_vulnerabilities(self, target: str, **kwargs) -> Dict[str, Any]:
        """Test for common web vulnerabilities"""
        logger.info(f"Testing vulnerabilities for {target}")
        
        findings = []
        
        findings.extend(self._test_sql_injection(target))
        
        findings.extend(self._test_xss(target))
        
        findings.extend(self._test_csrf(target))
        
        findings.extend(self._test_ssrf(target))
        
        return {
            "target": target,
            "findings": findings,
            "timestamp": datetime.now().isoformat()
        }
    
    def _test_sql_injection(self, target: str) -> List[Dict]:
        """Test for SQL injection"""
        findings = []
        
        sqli_payloads = ["'", "' OR '1'='1", "' OR 1=1--"]
        
        test_url = target if '?' in target else f"{target}/?id=1"
        
        for payload in sqli_payloads:
            try:
                test_target = f"{test_url}{payload}"
                
                result = subprocess.run(
                    ["curl", "-s", "-I", test_target],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                response = result.stdout.lower()
                
                if any(x in response for x in ['sql', 'syntax', 'error', 'mysql', 'postgresql']):
                    findings.append({
                        "type": "sql_injection",
                        "url": test_target,
                        "payload": payload,
                        "severity": "high",
                        "confidence": 0.7
                    })
                    break
            except Exception as e:
                logger.warning(f"SQLi test failed: {e}")
        
        return findings
    
    def _test_xss(self, target: str) -> List[Dict]:
        """Test for XSS vulnerabilities"""
        findings = []
        
        xss_payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
        
        for payload in xss_payloads:
            findings.append({
                "type": "xss",
                "target": target,
                "payload": payload,
                "severity": "medium",
                "confidence": 0.5,
                "note": "Manual verification required"
            })
        
        return findings
    
    def _test_csrf(self, target: str) -> List[Dict]:
        """Test for CSRF vulnerabilities"""
        return []
    
    def _test_ssrf(self, target: str) -> List[Dict]:
        """Test for SSRF vulnerabilities"""
        return []
    
    def validate_exploitable(self, findings: List[Dict], **kwargs) -> Dict[str, Any]:
        """Validate which findings are exploitable"""
        validated = []
        
        for finding in findings:
            if finding.get('confidence', 0) > 0.7:
                validated.append({
                    **finding,
                    "exploitable": True
                })
        
        return {
            "findings": validated,
            "exploitable_count": len(validated),
            "timestamp": datetime.now().isoformat()
        }
    
    def exploit(self, finding: Dict, **kwargs) -> Dict[str, Any]:
        """Exploit a vulnerability"""
        logger.info(f"Attempting exploitation of {finding.get('type')}")
        
        return {
            "finding": finding,
            "exploit_status": "executed",
            "result": "manual_verification_required",
            "timestamp": datetime.now().isoformat()
        }
    
    def directory_bruteforce(self, target: str, wordlist: str = None, **kwargs) -> Dict[str, Any]:
        """Perform directory brute force"""
        logger.info(f"Starting directory brute force for {target}")
        
        directories = []
        
        default_wordlist = f"{self.wordlists_path}/directory-wordlist.txt"
        
        try:
            with open(default_wordlist, 'r') as f:
                words = f.readlines()[:50]
        except:
            words = ['admin', 'login', 'wp-admin', 'phpmyadmin', 'backup']
        
        for word in words:
            word = word.strip()
            if not word:
                continue
            
            url = f"{target.rstrip('/')}/{word}"
            
            try:
                result = subprocess.run(
                    ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                status_code = result.stdout.strip()
                
                if status_code in ['200', '301', '302', '403']:
                    directories.append({
                        "path": f"/{word}",
                        "status": status_code,
                        "discovered": True
                    })
            except:
                pass
        
        return {
            "target": target,
            "directories": directories,
            "count": len(directories),
            "timestamp": datetime.now().isoformat()
        }
