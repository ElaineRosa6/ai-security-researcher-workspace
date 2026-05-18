"""
Tool Executor - 安全工具执行引擎
安全执行各种渗透测试工具，并解析输出结果
"""
import logging
import subprocess
import shlex
import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class ToolExecutionError(Exception):
    """工具执行错误"""
    pass


class ToolExecutor:
    """工具执行器基类"""
    
    def __init__(self, timeout: int = 300, output_dir: str = None):
        self.timeout = timeout
        self.output_dir = Path(output_dir) if output_dir else Path("output/tools")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def execute_command(self, command: List[str], timeout: int = None) -> Dict[str, Any]:
        """
        安全执行命令
        
        Args:
            command: 命令和参数列表
            timeout: 超时时间（秒）
            
        Returns:
            执行结果
        """
        timeout = timeout or self.timeout
        cmd_str = ' '.join(shlex.quote(part) for part in command)
        
        logger.info(f"Executing command: {cmd_str}")
        
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            return {
                "command": cmd_str,
                "return_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "success": result.returncode == 0,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.TimeoutExpired as e:
            logger.error(f"Command timed out after {timeout} seconds")
            raise ToolExecutionError(f"Command timed out: {cmd_str}")
        except Exception as e:
            logger.error(f"Command execution failed: {e}")
            raise ToolExecutionError(f"Command failed: {cmd_str}, error: {str(e)}")


class NmapExecutor(ToolExecutor):
    """Nmap 扫描器执行器"""
    
    def __init__(self, timeout: int = 300, output_dir: str = None):
        super().__init__(timeout, output_dir)
        self.xml_parser = NmapXMLParser()
    
    def execute_nmap(self, target: str, flags: str = "-sV -sC") -> Dict[str, Any]:
        """
        执行 Nmap 扫描
        
        Args:
            target: 目标 IP 或域名
            flags: Nmap 标志参数
            
        Returns:
            扫描结果
        """
        output_file = self.output_dir / f"nmap_{target.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml"
        
        command = ["nmap", "-oX", str(output_file)] + flags.split() + [target]
        
        try:
            execution_result = self.execute_command(command)
            
            if execution_result["success"]:
                parsed_result = self.parse_xml_output(str(output_file))
                return {
                    "tool": "nmap",
                    "target": target,
                    "success": True,
                    "output_file": str(output_file),
                    "raw": execution_result,
                    "parsed": parsed_result,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "tool": "nmap",
                    "target": target,
                    "success": False,
                    "raw": execution_result,
                    "error": execution_result["stderr"],
                    "timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"Nmap execution failed: {e}")
            return {
                "tool": "nmap",
                "target": target,
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def parse_xml_output(self, xml_path: str) -> Dict[str, Any]:
        """解析 Nmap XML 输出"""
        try:
            return self.xml_parser.parse(xml_path)
        except Exception as e:
            logger.error(f"Failed to parse Nmap XML: {e}")
            return {"error": str(e)}


class NmapXMLParser:
    """Nmap XML 输出解析器"""
    
    def parse(self, xml_path: str) -> Dict[str, Any]:
        """解析 Nmap XML 文件"""
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        result = {
            "scan_info": self._parse_scan_info(root),
            "hosts": self._parse_hosts(root),
            "ports": self._parse_ports(root)
        }
        
        return result
    
    def _parse_scan_info(self, root):
        scan_info = {}
        
        for scaninfo in root.findall(".//scaninfo"):
            scan_info["type"] = scaninfo.attrib.get("type")
            scan_info["protocol"] = scaninfo.attrib.get("protocol")
            scan_info["services"] = scaninfo.attrib.get("services")
        
        runstats = root.find(".//runstats")
        if runstats is not None:
            finished = runstats.find("finished")
            if finished is not None:
                scan_info["time"] = finished.attrib.get("time")
                scan_info["elapsed"] = finished.attrib.get("elapsed")
        
        return scan_info
    
    def _parse_hosts(self, root):
        hosts = []
        
        for host in root.findall(".//host"):
            host_info = {}
            
            status = host.find("status")
            if status is not None:
                host_info["status"] = status.attrib.get("state", "unknown")
            
            addresses = host.findall("address")
            for addr in addresses:
                addr_type = addr.attrib.get("addrtype")
                host_info[addr_type] = addr.attrib.get("addr")
            
            hostname = host.find(".//hostname")
            if hostname is not None:
                host_info["hostname"] = hostname.attrib.get("name", "")
            
            os_info = host.find(".//os/osmatch")
            if os_info is not None:
                host_info["os"] = os_info.attrib.get("name", "")
            
            hosts.append(host_info)
        
        return hosts
    
    def _parse_ports(self, root):
        ports = []
        
        for port in root.findall(".//port"):
            port_info = {
                "protocol": port.attrib.get("protocol", "tcp"),
                "portid": int(port.attrib.get("portid", 0))
            }
            
            state = port.find("state")
            if state is not None:
                port_info["state"] = state.attrib.get("state", "unknown")
            
            service = port.find("service")
            if service is not None:
                port_info["service"] = {
                    "name": service.attrib.get("name", ""),
                    "product": service.attrib.get("product", ""),
                    "version": service.attrib.get("version", ""),
                    "extrainfo": service.attrib.get("extrainfo", "")
                }
            
            scripts = port.findall("script")
            port_info["scripts"] = []
            for script in scripts:
                port_info["scripts"].append({
                    "id": script.attrib.get("id"),
                    "output": script.attrib.get("output", "")
                })
            
            ports.append(port_info)
        
        return ports


class SQLMapExecutor(ToolExecutor):
    """SQLMap 扫描器执行器"""
    
    def __init__(self, timeout: int = 600, output_dir: str = None):
        super().__init__(timeout, output_dir)
    
    def execute_sqlmap(self, url: str, options: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        执行 SQLMap 扫描
        
        Args:
            url: 目标 URL
            options: SQLMap 选项
            
        Returns:
            扫描结果
        """
        options = options or {}
        
        command = ["sqlmap", "-u", url]
        
        # 添加常见选项
        if options.get("batch", True):
            command.append("--batch")
        if options.get("risk"):
            command.extend(["--risk", str(options["risk"])])
        if options.get("level"):
            command.extend(["--level", str(options["level"])])
        if options.get("threads"):
            command.extend(["--threads", str(options["threads"])])
        if options.get("dump"):
            command.append("--dump")
        if options.get("dbs"):
            command.append("--dbs")
        if options.get("tables"):
            command.append("--tables")
        
        # 输出目录
        output_session = self.output_dir / f"sqlmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        command.extend(["--output-dir", str(output_session)])
        
        try:
            execution_result = self.execute_command(command)
            
            parsed_result = self._parse_sqlmap_output(execution_result["stdout"])
            
            return {
                "tool": "sqlmap",
                "target": url,
                "success": execution_result["success"],
                "raw": execution_result,
                "parsed": parsed_result,
                "output_dir": str(output_session),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"SQLMap execution failed: {e}")
            return {
                "tool": "sqlmap",
                "target": url,
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def _parse_sqlmap_output(self, output: str) -> Dict[str, Any]:
        """解析 SQLMap 输出"""
        parsed = {
            "vulnerabilities": [],
            "databases": [],
            "tables": [],
            "info": []
        }
        
        # 查找 SQL 注入漏洞
        if "sql injection" in output.lower():
            parsed["vulnerabilities"].append("SQL Injection")
        if "boolean-based blind" in output.lower():
            parsed["vulnerabilities"].append("Boolean-based Blind SQL Injection")
        if "time-based blind" in output.lower():
            parsed["vulnerabilities"].append("Time-based Blind SQL Injection")
        if "error-based" in output.lower():
            parsed["vulnerabilities"].append("Error-based SQL Injection")
        if "union query" in output.lower():
            parsed["vulnerabilities"].append("UNION Query SQL Injection")
        
        # 简单解析数据库和表（实际项目需要更复杂的解析）
        return parsed


class NucleiExecutor(ToolExecutor):
    """Nuclei 漏洞扫描器执行器"""
    
    def __init__(self, timeout: int = 600, output_dir: str = None):
        super().__init__(timeout, output_dir)
    
    def execute_nuclei(self, target: str, templates: str = None) -> Dict[str, Any]:
        """
        执行 Nuclei 扫描
        
        Args:
            target: 目标 URL
            templates: 模板路径
            
        Returns:
            扫描结果
        """
        output_file = self.output_dir / f"nuclei_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        command = ["nuclei", "-u", target, "-j", "-o", str(output_file)]
        
        if templates:
            command.extend(["-t", templates])
        
        try:
            execution_result = self.execute_command(command)
            
            parsed_result = self._parse_nuclei_output(str(output_file))
            
            return {
                "tool": "nuclei",
                "target": target,
                "success": execution_result["success"],
                "raw": execution_result,
                "parsed": parsed_result,
                "output_file": str(output_file),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Nuclei execution failed: {e}")
            return {
                "tool": "nuclei",
                "target": target,
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def _parse_nuclei_output(self, output_file: str) -> Dict[str, Any]:
        """解析 Nuclei JSON 输出"""
        findings = []
        
        try:
            with open(output_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            finding = json.loads(line)
                            findings.append(finding)
                        except json.JSONDecodeError:
                            pass
        except FileNotFoundError:
            logger.warning(f"Nuclei output file not found: {output_file}")
        
        return {"findings": findings}


class BurpSuiteExecutor(ToolExecutor):
    """Burp Suite API 执行器（需要 Burp Suite 开启 API 服务器）"""
    
    def __init__(self, api_url: str = "http://127.0.0.1:1337", api_key: str = None):
        super().__init__(timeout=600)
        self.api_url = api_url
        self.api_key = api_key
    
    def start_scan(self, target_url: str) -> Dict[str, Any]:
        """启动 Burp Suite 扫描"""
        logger.info("Burp Suite API integration requires additional setup")
        return {
            "tool": "burp",
            "target": target_url,
            "success": False,
            "error": "Burp Suite API integration requires additional configuration",
            "note": "Please refer to Burp Suite documentation for API setup",
            "timestamp": datetime.now().isoformat()
        }


# 工厂类
class ToolExecutorFactory:
    """工具执行器工厂"""
    
    @staticmethod
    def create(tool_name: str, **kwargs):
        """创建工具执行器实例"""
        executors = {
            "nmap": NmapExecutor,
            "sqlmap": SQLMapExecutor,
            "nuclei": NucleiExecutor,
            "burp": BurpSuiteExecutor
        }
        
        executor_class = executors.get(tool_name.lower())
        if executor_class:
            return executor_class(**kwargs)
        
        raise ValueError(f"Unknown tool: {tool_name}")
