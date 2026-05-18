"""
General Skills - Tools and Reporting
"""

import json
import logging
import subprocess
import sys
import os
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
harness_path = os.path.join(parent_dir, 'harness')
if harness_path not in sys.path:
    sys.path.insert(0, harness_path)

try:
    from tool_executor import ToolExecutorFactory
except ImportError:
    logger.warning("ToolExecutor not available, using fallback methods")
    ToolExecutorFactory = None


class GeneralSkill:
    """General skills including tools and reporting"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.output_path = self.config.get('output_path', 'output')
        self._init_executors()
    
    def _init_executors(self):
        """初始化工具执行器"""
        self.executors = {}
        if ToolExecutorFactory:
            try:
                self.executors["nmap"] = ToolExecutorFactory.create("nmap")
                self.executors["sqlmap"] = ToolExecutorFactory.create("sqlmap")
                self.executors["nuclei"] = ToolExecutorFactory.create("nuclei")
            except Exception as e:
                logger.warning(f"Failed to initialize tool executors: {e}")
    
    def nmap_scan(self, target: str, flags: str = "-sV -sC -p-", **kwargs) -> Dict[str, Any]:
        """Run Nmap scan using integrated tool executor"""
        logger.info(f"Running Nmap scan on {target}")
        
        if "nmap" in self.executors:
            try:
                executor = self.executors["nmap"]
                result = executor.execute_nmap(target, flags)
                
                # Convert to standard format
                findings = []
                if result.get("success") and result.get("parsed"):
                    ports = result["parsed"].get("ports", [])
                    for port in ports:
                        findings.append({
                            "type": "port_open",
                            "port": port.get("portid"),
                            "protocol": port.get("protocol"),
                            "state": port.get("state"),
                            "service": port.get("service", {}),
                            "discovered": True
                        })
                
                return {
                    "target": target,
                    "flags": flags,
                    "status": "completed" if result.get("success") else "error",
                    "scan_results": result,
                    "findings": findings,
                    "timestamp": datetime.now().isoformat()
                }
            except Exception as e:
                logger.error(f"Tool executor failed: {e}")
        
        # Fallback to original method
        return self._fallback_nmap_scan(target, flags)
    
    def _fallback_nmap_scan(self, target: str, flags: str = "-sV -sC -p-") -> Dict[str, Any]:
        """Fallback Nmap scan method"""
        results = {
            "target": target,
            "flags": flags,
            "scan_results": {},
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = subprocess.run(
                ["nmap", "-oX", "-"] + flags.split() + [target],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                results["scan_results"]["raw_xml"] = result.stdout[:5000]
                results["status"] = "completed"
            else:
                results["status"] = "error"
                results["error"] = result.stderr
                
        except FileNotFoundError:
            results["status"] = "error"
            results["error"] = "nmap not found"
        except Exception as e:
            results["status"] = "error"
            results["error"] = str(e)
        
        return results
    
    def osint(self, target: str, **kwargs) -> Dict[str, Any]:
        """Perform OSINT gathering"""
        logger.info(f"Performing OSINT on {target}")
        
        results = {
            "target": target,
            "emails": [],
            "domains": [],
            "subdomains": [],
            "data_breaches": [],
            "timestamp": datetime.now().isoformat()
        }
        
        return results
    
    def nuclei_scan(self, target: str, templates: str = None, **kwargs) -> Dict[str, Any]:
        """Run nuclei vulnerability scan using tool executor"""
        logger.info(f"Running nuclei scan on {target}")
        
        if "nuclei" in self.executors:
            try:
                executor = self.executors["nuclei"]
                result = executor.execute_nuclei(target, templates)
                
                findings = []
                if result.get("success") and result.get("parsed"):
                    for finding in result["parsed"].get("findings", []):
                        findings.append({
                            "type": finding.get("template", "unknown"),
                            "severity": finding.get("severity", "medium"),
                            "title": finding.get("template", ""),
                            "description": finding.get("info", {}),
                            "evidence": str(finding),
                            "discovered": True
                        })
                
                return {
                    "target": target,
                    "status": "completed" if result.get("success") else "error",
                    "scan_results": result,
                    "findings": findings,
                    "timestamp": datetime.now().isoformat()
                }
            except Exception as e:
                logger.error(f"Nuclei executor failed: {e}")
        
        # Fallback
        return {
            "target": target,
            "status": "info",
            "command": f"nuclei -u {target}",
            "findings": [],
            "timestamp": datetime.now().isoformat()
        }
    
    def sqlmap_scan(self, url: str, options: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        """Run SQLMap scan using tool executor"""
        logger.info(f"Running SQLMap on {url}")
        
        if "sqlmap" in self.executors:
            try:
                executor = self.executors["sqlmap"]
                result = executor.execute_sqlmap(url, options)
                
                findings = []
                if result.get("success") and result.get("parsed"):
                    vulns = result["parsed"].get("vulnerabilities", [])
                    for vuln in vulns:
                        findings.append({
                            "type": "sql_injection",
                            "vuln_type": vuln,
                            "severity": "critical",
                            "title": f"SQL Injection - {vuln}",
                            "description": f"Target {url} appears vulnerable to {vuln}",
                            "evidence": str(result.get("raw", {}).get("stdout", "")),
                            "discovered": True
                        })
                
                return {
                    "target": url,
                    "status": "completed" if result.get("success") else "error",
                    "scan_results": result,
                    "findings": findings,
                    "timestamp": datetime.now().isoformat()
                }
            except Exception as e:
                logger.error(f"SQLMap executor failed: {e}")
        
        # Fallback
        return {
            "target": url,
            "status": "info",
            "command": f"sqlmap -u {url}",
            "findings": [],
            "timestamp": datetime.now().isoformat()
        }
    
    def execute_command(self, command: str, timeout: int = 60, **kwargs) -> Dict[str, Any]:
        """Execute shell command"""
        logger.info(f"Executing command: {command}")
        
        results = {
            "command": command,
            "return_code": None,
            "stdout": "",
            "stderr": "",
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            results["return_code"] = result.returncode
            results["stdout"] = result.stdout[:10000]
            results["stderr"] = result.stderr[:5000]
            
        except subprocess.TimeoutExpired:
            results["error"] = "Command timeout"
        except Exception as e:
            results["error"] = str(e)
        
        return results
    
    def parse_tool_output(self, tool: str, output: str, **kwargs) -> Dict[str, Any]:
        """Parse tool output"""
        logger.info(f"Parsing {tool} output")
        
        results = {
            "tool": tool,
            "parsed": {},
            "timestamp": datetime.now().isoformat()
        }
        
        if tool == "nmap":
            results["parsed"] = self._parse_nmap_output(output)
        elif tool == "burp":
            results["parsed"] = self._parse_burp_output(output)
        elif tool == "sqlmap":
            results["parsed"] = self._parse_sqlmap_output(output)
        
        return results
    
    def _parse_nmap_output(self, output: str) -> Dict[str, Any]:
        """Parse Nmap output"""
        parsed = {
            "hosts": [],
            "services": []
        }
        
        return parsed
    
    def _parse_burp_output(self, output: str) -> Dict[str, Any]:
        """Parse Burp Suite output"""
        parsed = {
            "issues": []
        }
        
        return parsed
    
    def _parse_sqlmap_output(self, output: str) -> Dict[str, Any]:
        """Parse SQLMap output"""
        parsed = {
            "vulnerable": False,
            "injection_points": []
        }
        
        return parsed


class ReportingSkill:
    """Report generation skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.output_path = self.config.get('output_path', 'output/reports')
    
    def generate_pentest_report(self, findings: List[Dict], **kwargs) -> str:
        """Generate penetration test report"""
        logger.info(f"Generating pentest report with {len(findings)} findings")
        
        report = self._generate_markdown_report(findings)
        
        report_file = f"{self.output_path}/pentest_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        import os
        os.makedirs(self.output_path, exist_ok=True)
        
        with open(report_file, 'w') as f:
            f.write(report)
        
        return report_file
    
    def _generate_markdown_report(self, findings: List[Dict]) -> str:
        """Generate markdown report"""
        critical = [f for f in findings if f.get('severity') == 'critical']
        high = [f for f in findings if f.get('severity') == 'high']
        medium = [f for f in findings if f.get('severity') == 'medium']
        low = [f for f in findings if f.get('severity') == 'low']
        
        report = f"""# Penetration Test Report

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Executive Summary

This report presents the findings from a comprehensive penetration test conducted on the target environment. A total of **{len(findings)}** vulnerabilities were identified.

### Risk Summary

| Severity | Count |
|----------|-------|
| Critical | {len(critical)} |
| High | {len(high)} |
| Medium | {len(medium)} |
| Low | {len(low)} |

## Detailed Findings

"""
        
        severity_order = ['critical', 'high', 'medium', 'low']
        
        for severity in severity_order:
            vulns = [f for f in findings if f.get('severity') == severity]
            
            if vulns:
                report += f"\n### {severity.upper()} Severity\n\n"
                
                for vuln in vulns:
                    report += f"""#### {vuln.get('title', 'Untitled')}

**Type**: {vuln.get('type', 'Unknown')}

**Description**:
{vuln.get('description', 'No description provided')}

**Affected Component**: {vuln.get('affected', 'Unknown')}

**Evidence**:
```
{vuln.get('evidence', 'No evidence provided')}
```

**Impact**: {vuln.get('impact', 'Impact analysis pending')}

**Remediation**: {vuln.get('remediation', 'Remediation guidance pending')}

---

"""
        
        report += """
## Recommendations

1. Address all critical and high severity vulnerabilities immediately
2. Implement input validation and output encoding
3. Use parameterized queries for database operations
4. Implement proper authentication and session management
5. Regular security testing and vulnerability assessments

## Conclusion

The penetration test revealed several security vulnerabilities that require attention. Immediate remediation of critical and high severity issues is recommended.

---
*Report generated by Security Expert Agent*
"""
        
        return report
    
    def create_executive_summary(self, data: Dict[str, Any], **kwargs) -> str:
        """Create executive summary"""
        summary = f"""
# Executive Summary

**Assessment Date**: {datetime.now().strftime('%Y-%m-%d')}

## Overview

{data.get('overview', 'Security assessment conducted on target environment')}

## Key Findings

- Total Vulnerabilities: {data.get('total_findings', 0)}
- Critical Issues: {data.get('critical_count', 0)}
- High Priority Issues: {data.get('high_count', 0)}

## Business Impact

{data.get('business_impact', 'Assessment of security posture completed')}

## Recommended Next Steps

1. Remediate critical vulnerabilities within 24-48 hours
2. Schedule remediation of high priority issues within 7 days
3. Conduct follow-up assessment after remediation
4. Implement continuous security monitoring
"""
        
        return summary
    
    def export_findings(self, findings: List[Dict], format: str = "json", **kwargs) -> str:
        """Export findings in specified format"""
        logger.info(f"Exporting findings in {format} format")
        
        if format == "json":
            output = json.dumps(findings, indent=2)
            ext = "json"
        elif format == "csv":
            output = self._to_csv(findings)
            ext = "csv"
        else:
            output = str(findings)
            ext = "txt"
        
        output_file = f"{self.output_path}/findings_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
        
        import os
        os.makedirs(self.output_path, exist_ok=True)
        
        with open(output_file, 'w') as f:
            f.write(output)
        
        return output_file
    
    def _to_csv(self, findings: List[Dict]) -> str:
        """Convert findings to CSV"""
        if not findings:
            return ""
        
        headers = ["ID", "Title", "Type", "Severity", "Description"]
        
        csv = ",".join(headers) + "\n"
        
        for i, finding in enumerate(findings, 1):
            row = [
                str(i),
                finding.get('title', '').replace(',', ';'),
                finding.get('type', ''),
                finding.get('severity', ''),
                finding.get('description', '').replace(',', ';')[:100]
            ]
            csv += ",".join(row) + "\n"
        
        return csv
