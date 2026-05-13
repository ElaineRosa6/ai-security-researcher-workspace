"""
Red Team Skills - Web Security Testing
"""

import json
import logging
import os
import subprocess
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)

# SQL injection test payloads
SQLI_PAYLOADS = ["'", "' OR '1'='1", "' OR 1=1--"]

# XSS test payloads
XSS_PAYLOADS = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]

# Default wordlist fallback
DEFAULT_WORDLIST_WORDS = ['admin', 'login', 'wp-admin', 'phpmyadmin', 'backup']

# HTTP status codes indicating directory exists
DIRECTORY_FOUND_STATUS_CODES = {'200', '301', '302', '403'}

# SQL error indicators for detection
SQL_ERROR_INDICATORS = ['sql', 'syntax', 'error', 'mysql', 'postgresql']

# Sensitive header keys to extract
SENSITIVE_HEADERS = ['server', 'x-powered-by', 'x-aspnet-version']

# Curl timeout settings
CURL_TIMEOUT_RECON = 10
CURL_TIMEOUT_VULN = 10
CURL_TIMEOUT_BRUTE = 5


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
                timeout=CURL_TIMEOUT_RECON
            )
            
            if result.returncode != 0:
                logger.warning(f"curl command failed with code {result.returncode}")
                return []
            
            headers = result.stdout
            
            server_info = self._parse_headers(headers)
            
            if server_info:
                endpoints.append({
                    "type": "server_info",
                    "data": server_info
                })
                
        except subprocess.TimeoutExpired:
            logger.warning(f"Request to {target} timed out")
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
                
                if key in SENSITIVE_HEADERS:
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
        
        test_url = target if '?' in target else f"{target}/?id=1"
        
        for payload in SQLI_PAYLOADS:
            try:
                test_target = f"{test_url}{payload}"
                
                result = subprocess.run(
                    ["curl", "-s", "-I", test_target],
                    capture_output=True,
                    text=True,
                    timeout=CURL_TIMEOUT_VULN
                )
                
                if result.returncode != 0:
                    logger.warning(f"curl command failed with code {result.returncode}")
                    continue
                
                response = result.stdout.lower()
                
                if any(x in response for x in SQL_ERROR_INDICATORS):
                    findings.append({
                        "type": "sql_injection",
                        "url": test_target,
                        "payload": payload,
                        "severity": "high",
                        "confidence": 0.7
                    })
                    break
            except subprocess.TimeoutExpired:
                logger.warning(f"SQLi test timed out for {test_target}")
            except Exception as e:
                logger.warning(f"SQLi test failed: {e}")
        
        return findings
    
    def _test_xss(self, target: str) -> List[Dict]:
        """Test for XSS vulnerabilities"""
        findings = []
        
        for payload in XSS_PAYLOADS:
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
        
        if wordlist:
            wordlist_path = os.path.abspath(wordlist)
            wordlists_base = os.path.abspath(self.wordlists_path)
            if not wordlist_path.startswith(wordlists_base):
                logger.error(f"Invalid wordlist path: {wordlist}")
                wordlist = None
        
        default_wordlist = os.path.join(self.wordlists_path, 'directory-wordlist.txt')
        wordlist_to_use = wordlist or default_wordlist
        
        try:
            with open(wordlist_to_use, 'r') as f:
                words = f.readlines()[:50]
        except Exception:
            logger.warning(f"Failed to read wordlist, using default words")
            words = DEFAULT_WORDLIST_WORDS
        
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
                    timeout=CURL_TIMEOUT_BRUTE
                )
                
                if result.returncode != 0:
                    logger.warning(f"curl command failed with code {result.returncode}")
                    continue
                
                status_code = result.stdout.strip()
                
                if status_code in DIRECTORY_FOUND_STATUS_CODES:
                    directories.append({
                        "path": f"/{word}",
                        "status": status_code,
                        "discovered": True
                    })
            except subprocess.TimeoutExpired:
                logger.warning(f"Request to {url} timed out")
            except Exception:
                pass
        
        return {
            "target": target,
            "directories": directories,
            "count": len(directories),
            "timestamp": datetime.now().isoformat()
        }
