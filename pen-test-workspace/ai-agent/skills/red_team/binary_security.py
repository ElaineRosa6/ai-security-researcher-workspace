"""
Red Team Skills - Binary/PWN Security
"""

import json
import logging
import subprocess
import os
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class BinarySecuritySkill:
    """Binary security analysis skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.binary_path = self.config.get('binary_path', 'shared/tools/binaries')
        self.output_path = self.config.get('output_path', 'output')
    
    def analyze_binary(self, binary_path: str, **kwargs) -> Dict[str, Any]:
        """Analyze binary file"""
        logger.info(f"Analyzing binary: {binary_path}")
        
        results = {
            "binary_path": binary_path,
            "file_info": {},
            "security_features": {},
            "functions": [],
            "strings": [],
            "timestamp": datetime.now().isoformat()
        }
        
        results["file_info"] = self._get_file_info(binary_path)
        
        results["security_features"] = self._check_security_features(binary_path)
        
        results["strings"] = self._extract_strings(binary_path)
        
        return results
    
    def _get_file_info(self, binary_path: str) -> Dict[str, Any]:
        """Get file information"""
        info = {}
        
        try:
            result = subprocess.run(
                ["file", binary_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            info["file_type"] = result.stdout.strip()
        except Exception as e:
            logger.warning(f"Failed to get file info: {e}")
            info["file_type"] = "unknown"
        
        try:
            stat = os.stat(binary_path)
            info["size"] = stat.st_size
            info["permissions"] = oct(stat.st_mode)[-3:]
        except:
            pass
        
        return info
    
    def _check_security_features(self, binary_path: str) -> Dict[str, Any]:
        """Check security features using checksec"""
        features = {
            "nx": False,
            "pie": False,
            "relro": "unknown",
            "canary": False,
            "rpath": False,
            "runpath": False
        }
        
        try:
            result = subprocess.run(
                ["checksec", "--file=" + binary_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            output = result.stdout.lower()
            
            features["nx"] = "nx enabled" in output or "nx: yes" in output
            features["pie"] = "pie enabled" in output or "pie: yes" in output
            features["canary"] = "canary" in output and "no" not in output.split("canary")[1][:10] if "canary" in output else False
            
        except Exception as e:
            logger.warning(f"Checksec not available: {e}")
        
        return features
    
    def _extract_strings(self, binary_path: str, min_length: int = 4) -> List[str]:
        """Extract strings from binary"""
        strings = []
        
        try:
            result = subprocess.run(
                ["strings", "-n", str(min_length), binary_path],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            strings = result.stdout.strip().split('\n')[:100]
            
        except Exception as e:
            logger.warning(f"Strings extraction failed: {e}")
        
        return strings
    
    def fuzz_binary(self, binary_path: str, iterations: int = 100, **kwargs) -> Dict[str, Any]:
        """Fuzz binary for crashes"""
        logger.info(f"Starting fuzzing: {binary_path}, iterations: {iterations}")
        
        results = {
            "binary_path": binary_path,
            "iterations": iterations,
            "crashes": [],
            "crash_count": 0,
            "status": "in_progress",
            "timestamp": datetime.now().isoformat()
        }
        
        crashes = []
        
        for i in range(min(iterations, 10)):
            crash = self._test_crash(binary_path, f"input_{i}")
            if crash:
                crashes.append(crash)
        
        results["crashes"] = crashes
        results["crash_count"] = len(crashes)
        results["status"] = "completed"
        
        return results
    
    def _test_crash(self, binary_path: str, input_data: str) -> Optional[Dict]:
        """Test for crash with specific input"""
        try:
            result = subprocess.run(
                [binary_path],
                input=input_data,
                capture_output=True,
                timeout=5
            )
            
            if result.returncode < 0:
                return {
                    "input": input_data,
                    "signal": abs(result.returncode),
                    "type": "signal_crash"
                }
            
        except subprocess.TimeoutExpired:
            return {
                "input": input_data,
                "type": "timeout"
            }
        except Exception as e:
            return {
                "input": input_data,
                "type": "error",
                "error": str(e)
            }
        
        return None
    
    def find_rop_gadgets(self, binary_path: str, **kwargs) -> Dict[str, Any]:
        """Find ROP gadgets in binary"""
        logger.info(f"Finding ROP gadgets: {binary_path}")
        
        results = {
            "binary_path": binary_path,
            "gadgets": [],
            "gadget_count": 0,
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = subprocess.run(
                ["ROPGadget", "--binary", binary_path],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                
                for line in lines[2:][:50]:
                    if line.strip():
                        parts = line.split(':')
                        if len(parts) >= 2:
                            results["gadgets"].append({
                                "address": parts[0].strip(),
                                "instruction": ':'.join(parts[1:]).strip()
                            })
                
                results["gadget_count"] = len(results["gadgets"])
                
        except Exception as e:
            logger.warning(f"ROPGadget failed: {e}")
        
        return results
    
    def generate_exploit(self, binary_path: str, exploit_type: str = "buffer_overflow", **kwargs) -> Dict[str, Any]:
        """Generate exploit template"""
        logger.info(f"Generating {exploit_type} exploit for {binary_path}")
        
        results = {
            "binary_path": binary_path,
            "exploit_type": exploit_type,
            "template": "",
            "notes": [],
            "timestamp": datetime.now().isoformat()
        }
        
        if exploit_type == "buffer_overflow":
            results["template"] = self._generate_bof_exploit(binary_path)
            results["notes"] = [
                "Find offset using pattern_create and pattern_offset",
                "Identify correct EIP overwrite",
                "Find exploit space for shellcode",
                "Test for bad characters"
            ]
        
        return results
    
    def _generate_bof_exploit(self, binary_path: str) -> str:
        """Generate buffer overflow exploit template"""
        template = '''#!/usr/bin/env python3
"""Buffer Overflow Exploit Template"""

import struct
from pwn import *

context.update(arch='i386', os='linux')

BINARY = "{binary_path}"
TARGET = ("127.0.0.1", 4444)

def exploit():
    """Exploit buffer overflow"""
    
    # Find offset
    offset = 0
    
    # Build payload
    payload = b"A" * offset          # Padding
    payload += p32(0xdeadbeef)       # EIP overwrite (address to jump)
    payload += b"BBBB"                # Additional space
    payload += b"CCCCCCCC"            # Shellcode placeholder
    
    return payload

if __name__ == "__main__":
    io = remote(TARGET[0], TARGET[1])
    io.sendline(exploit())
    io.interactive()
'''.format(binary_path=binary_path)
        
        return template
    
    def debug_session(self, binary_path: str, commands: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Start debug session"""
        logger.info(f"Starting debug session: {binary_path}")
        
        results = {
            "binary_path": binary_path,
            "commands": commands or [],
            "output": [],
            "status": "started",
            "timestamp": datetime.now().isoformat()
        }
        
        for cmd in commands or []:
            try:
                result = subprocess.run(
                    ["gdb", "-q", "-ex", cmd, binary_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                results["output"].append({
                    "command": cmd,
                    "result": result.stdout
                })
                
            except Exception as e:
                results["output"].append({
                    "command": cmd,
                    "error": str(e)
                })
        
        return results
    
    def analyze_elf(self, binary_path: str, **kwargs) -> Dict[str, Any]:
        """Analyze ELF binary"""
        logger.info(f"Analyzing ELF: {binary_path}")
        
        results = {
            "binary_path": binary_path,
            "elf_header": {},
            "sections": [],
            "symbols": [],
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = subprocess.run(
                ["readelf", "-h", binary_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                results["elf_header"] = self._parse_elf_header(result.stdout)
                
        except Exception as e:
            logger.warning(f"ELF analysis failed: {e}")
        
        return results
    
    def _parse_elf_header(self, output: str) -> Dict[str, str]:
        """Parse ELF header output"""
        header = {}
        
        for line in output.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                header[key.strip()] = value.strip()
        
        return header
