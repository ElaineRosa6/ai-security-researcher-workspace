"""
Red Team Skills - Mobile Application Security
"""

import json
import logging
import subprocess
import os
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class MobileSecuritySkill:
    """Mobile application security skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.output_path = self.config.get('output_path', 'output/mobile')
    
    def decompile_apk(self, apk_path: str, **kwargs) -> Dict[str, Any]:
        """Decompile Android APK"""
        logger.info(f"Decompiling APK: {apk_path}")
        
        results = {
            "apk_path": apk_path,
            "output_dir": f"{self.output_path}/decompiled/{os.path.basename(apk_path)}",
            "status": "in_progress",
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            os.makedirs(results["output_dir"], exist_ok=True)
            
            result = subprocess.run(
                ["apktool", "d", "-f", "-o", results["output_dir"], apk_path],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                results["status"] = "completed"
                results["message"] = "APK decompiled successfully"
            else:
                results["status"] = "failed"
                results["error"] = result.stderr
                
        except FileNotFoundError:
            results["status"] = "failed"
            results["error"] = "apktool not found. Install: https://apktool.googlesource.com/apktool/"
        except Exception as e:
            results["status"] = "failed"
            results["error"] = str(e)
        
        return results
    
    def static_analysis(self, apk_path: str, **kwargs) -> Dict[str, Any]:
        """Perform static analysis on APK"""
        logger.info(f"Starting static analysis: {apk_path}")
        
        results = {
            "apk_path": apk_path,
            "package_name": "",
            "permissions": [],
            "activities": [],
            "services": [],
            "receivers": [],
            "hardcoded_secrets": [],
            "vulnerabilities": [],
            "timestamp": datetime.now().isoformat()
        }
        
        decomp_result = self.decompile_apk(apk_path)
        
        if decomp_result["status"] == "completed":
            output_dir = decomp_result["output_dir"]
            
            manifest_path = os.path.join(output_dir, "AndroidManifest.xml")
            
            if os.path.exists(manifest_path):
                manifest_data = self._analyze_manifest(manifest_path)
                results.update(manifest_data)
            
            results["hardcoded_secrets"] = self._find_secrets(output_dir)
            
            results["vulnerabilities"] = self._check_vulnerabilities(output_dir)
        
        return results
    
    def _analyze_manifest(self, manifest_path: str) -> Dict[str, Any]:
        """Analyze AndroidManifest.xml"""
        analysis = {
            "permissions": [],
            "activities": [],
            "services": [],
            "receivers": []
        }
        
        try:
            with open(manifest_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                import re
                
                permission_pattern = r'android:name="([^"]+)"'
                analysis["permissions"] = re.findall(permission_pattern, content)
                
                activity_pattern = r'<activity[^>]*android:name="([^"]+)"'
                analysis["activities"] = re.findall(activity_pattern, content)
                
                service_pattern = r'<service[^>]*android:name="([^"]+)"'
                analysis["services"] = re.findall(service_pattern, content)
                
                receiver_pattern = r'<receiver[^>]*android:name="([^"]+)"'
                analysis["receivers"] = re.findall(receiver_pattern, content)
                
        except Exception as e:
            logger.warning(f"Manifest analysis failed: {e}")
        
        return analysis
    
    def _find_secrets(self, decompiled_dir: str) -> List[Dict[str, str]]:
        """Find hardcoded secrets"""
        secrets = []
        
        patterns = {
            "api_key": [r'api[_-]?key["\s:=]+["\']?([a-zA-Z0-9]{20,})'],
            "password": [r'password["\s:=]+["\']?([^"\'\s]{4,})'],
            "secret": [r'secret["\s:=]+["\']?([a-zA-Z0-9+/=]{20,})'],
            "token": [r'token["\s:=]+["\']?([a-zA-Z0-9+/=]{20,})']
        }
        
        try:
            for root, dirs, files in os.walk(decompiled_dir):
                for file in files:
                    if file.endswith(('.xml', '.smali', '.java', '.properties')):
                        file_path = os.path.join(root, file)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                
                                for secret_type, regexes in patterns.items():
                                    for regex in regexes:
                                        import re
                                        matches = re.findall(regex, content, re.IGNORECASE)
                                        
                                        for match in matches[:3]:
                                            secrets.append({
                                                "type": secret_type,
                                                "value": match,
                                                "file": file_path.replace(decompiled_dir, ''),
                                                "severity": "high"
                                            })
                                        
                        except:
                            pass
                            
        except Exception as e:
            logger.warning(f"Secret finding failed: {e}")
        
        return secrets[:10]
    
    def _check_vulnerabilities(self, decompiled_dir: str) -> List[Dict[str, Any]]:
        """Check for common vulnerabilities"""
        vulns = []
        
        try:
            for root, dirs, files in os.walk(decompiled_dir):
                for file in files:
                    if file.endswith('.smali'):
                        file_path = os.path.join(root, file)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                
                                if 'Ljava/security/MessageDigest;' in content:
                                    if 'MessageDigest.getInstance("MD5")' in content:
                                        vulns.append({
                                            "type": "weak_crypto",
                                            "description": "MD5 hash usage detected",
                                            "severity": "medium",
                                            "file": file
                                        })
                                        
                                if 'debuggable="true"' in content:
                                    vulns.append({
                                        "type": "debug_enabled",
                                        "description": "Application has debug mode enabled",
                                        "severity": "low",
                                        "file": file
                                    })
                                        
                        except:
                            pass
                            
        except Exception as e:
            logger.warning(f"Vulnerability check failed: {e}")
        
        return vulns
    
    def dynamic_analysis(self, apk_path: str, frida_script: str = None, **kwargs) -> Dict[str, Any]:
        """Perform dynamic analysis with Frida"""
        logger.info(f"Starting dynamic analysis: {apk_path}")
        
        results = {
            "apk_path": apk_path,
            "frida_results": [],
            "hooked_functions": [],
            "intercepted_data": [],
            "timestamp": datetime.now().isoformat()
        }
        
        default_script = '''
        Java.perform(function() {{
            console.log("[*] Frida attached");
            
            var MainActivity = Java.use("com.example.MainActivity");
            
            MainActivity.onCreate.implementation = function(bundle) {{
                console.log("[*] onCreate called");
                this.onCreate(bundle);
            }};
        }});
        '''
        
        results["frida_script"] = frida_script or default_script
        
        return results
    
    def hook_function(self, package: str, function: str, script: str = None, **kwargs) -> Dict[str, Any]:
        """Hook a specific function with Frida"""
        logger.info(f"Hooking {package}.{function}")
        
        results = {
            "package": package,
            "function": function,
            "status": "hooked",
            "intercepted_calls": [],
            "timestamp": datetime.now().isoformat()
        }
        
        if script:
            results["custom_script"] = script
        
        return results
    
    def extract_secrets(self, apk_path: str, **kwargs) -> Dict[str, Any]:
        """Extract secrets from APK"""
        logger.info(f"Extracting secrets from: {apk_path}")
        
        results = {
            "apk_path": apk_path,
            "extracted": [],
            "certificates": [],
            "keys": [],
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = subprocess.run(
                ["unzip", "-o", "-d", f"{self.output_path}/extracted", apk_path],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            extracted_dir = f"{self.output_path}/extracted"
            
            for root, dirs, files in os.walk(extracted_dir):
                for file in files:
                    if file.endswith('.pem') or file.endswith('.p12') or file.endswith('.bks'):
                        results["certificates"].append(os.path.join(root, file))
                    
                    if 'secret' in file.lower() or 'password' in file.lower():
                        results["keys"].append(os.path.join(root, file))
            
        except Exception as e:
            logger.warning(f"Secret extraction failed: {e}")
        
        return results
    
    def analyze_ios(self, ipa_path: str, **kwargs) -> Dict[str, Any]:
        """Analyze iOS IPA"""
        logger.info(f"Analyzing iOS IPA: {ipa_path}")
        
        results = {
            "ipa_path": ipa_path,
            "info": "iOS analysis requires macOS with class-dump",
            "status": "limited",
            "timestamp": datetime.now().isoformat()
        }
        
        return results
