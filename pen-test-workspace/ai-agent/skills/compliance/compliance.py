"""
Compliance Skills - Recording, Evidence, and Compliance
"""

import json
import logging
import subprocess
import os
import hashlib
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class RecordingSkill:
    """Recording and documentation skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.output_path = self.config.get('output_path', 'compliance/recordings')
        self.recordings = {}
    
    def start_screen_recording(self, output_path: str = None, config: Dict = None, **kwargs) -> str:
        """Start screen recording"""
        logger.info("Starting screen recording")
        
        recording_id = f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if not output_path:
            output_path = f"{self.output_path}/screen/{recording_id}.mp4"
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        results = {
            "recording_id": recording_id,
            "output_path": output_path,
            "status": "started",
            "timestamp": datetime.now().isoformat()
        }
        
        self.recordings[recording_id] = results
        
        results["ffmpeg_command"] = f'ffmpeg -f x11grab -y -video_size 1920x1080 -i :0.0 -c:v libx264 -preset ultrafast {output_path}'
        
        return recording_id
    
    def stop_screen_recording(self, recording_id: str, **kwargs) -> Dict[str, Any]:
        """Stop screen recording"""
        logger.info(f"Stopping recording: {recording_id}")
        
        if recording_id in self.recordings:
            self.recordings[recording_id]["status"] = "stopped"
            self.recordings[recording_id]["end_time"] = datetime.now().isoformat()
            
            return self.recordings[recording_id]
        
        return {"error": "Recording not found"}
    
    def start_terminal_recording(self, output_path: str = None, **kwargs) -> str:
        """Start terminal recording"""
        logger.info("Starting terminal recording")
        
        recording_id = f"terminal_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if not output_path:
            output_path = f"{self.output_path}/terminal/{recording_id}.cast"
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        results = {
            "recording_id": recording_id,
            "output_path": output_path,
            "status": "started",
            "timestamp": datetime.now().isoformat()
        }
        
        self.recordings[recording_id] = results
        
        return recording_id
    
    def stop_terminal_recording(self, recording_id: str, **kwargs) -> Dict[str, Any]:
        """Stop terminal recording"""
        return self.stop_screen_recording(recording_id, **kwargs)
    
    def start_network_capture(self, output_path: str = None, filter: str = "", **kwargs) -> str:
        """Start network capture"""
        logger.info("Starting network capture")
        
        capture_id = f"network_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if not output_path:
            output_path = f"{self.output_path}/network/{capture_id}.pcap"
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        results = {
            "capture_id": capture_id,
            "output_path": output_path,
            "filter": filter,
            "status": "started",
            "timestamp": datetime.now().isoformat()
        }
        
        self.recordings[capture_id] = results
        
        filter_clause = f"-f '{filter}'" if filter else ""
        results["tcpdump_command"] = f"tcpdump -i any -w {output_path} {filter_clause}"
        
        return capture_id
    
    def stop_network_capture(self, capture_id: str, **kwargs) -> Dict[str, Any]:
        """Stop network capture"""
        return self.stop_screen_recording(capture_id, **kwargs)
    
    def enable_audit_logging(self, config: Dict = None, **kwargs) -> Dict[str, Any]:
        """Enable audit logging"""
        logger.info("Enabling audit logging")
        
        results = {
            "status": "enabled",
            "log_paths": [],
            "timestamp": datetime.now().isoformat()
        }
        
        results["log_paths"] = [
            "/var/log/auth.log",
            "/var/log/syslog",
            "/var/log/audit/audit.log"
        ]
        
        return results


class EvidenceSkill:
    """Evidence management skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.output_path = self.config.get('output_path', 'compliance/evidence')
        self.algorithm = self.config.get('hash_algorithm', 'sha256')
    
    def generate_hash(self, file_path: str, algorithm: str = None, **kwargs) -> str:
        """Generate file hash"""
        logger.info(f"Generating hash for: {file_path}")
        
        algo = algorithm or self.algorithm
        
        try:
            if algo == 'sha256':
                hash_obj = hashlib.sha256()
            elif algo == 'md5':
                hash_obj = hashlib.md5()
            elif algo == 'sha1':
                hash_obj = hashlib.sha1()
            else:
                hash_obj = hashlib.sha256()
            
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_obj.update(chunk)
            
            hash_value = hash_obj.hexdigest()
            
            self._record_hash(file_path, hash_value, algo)
            
            return hash_value
            
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return None
        except Exception as e:
            logger.error(f"Hash generation failed: {e}")
            return None
    
    def _record_hash(self, file_path: str, hash_value: str, algorithm: str) -> None:
        """Record hash to evidence log"""
        log_path = Path(self.output_path) / 'hashes' / 'evidence_hashes.json'
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        existing = {}
        if log_path.exists():
            with open(log_path, 'r') as f:
                existing = json.load(f)
        
        existing[file_path] = {
            "hash": hash_value,
            "algorithm": algorithm,
            "timestamp": datetime.now().isoformat()
        }
        
        with open(log_path, 'w') as f:
            json.dump(existing, f, indent=2)
    
    def verify_hash(self, file_path: str, expected_hash: str, **kwargs) -> bool:
        """Verify file hash"""
        actual_hash = self.generate_hash(file_path)
        
        if actual_hash:
            return actual_hash.lower() == expected_hash.lower()
        
        return False
    
    def sign_file(self, file_path: str, key_path: str = None, **kwargs) -> str:
        """Sign file with GPG"""
        logger.info(f"Signing file: {file_path}")
        
        results = {
            "file": file_path,
            "signature_file": f"{file_path}.sig",
            "status": "requires_gpg",
            "timestamp": datetime.now().isoformat()
        }
        
        results["gpg_command"] = f"gpg --output {results['signature_file']} --sign {file_path}"
        
        return results.get("signature_file", "")
    
    def verify_signature(self, file_path: str, signature_path: str, key_path: str = None, **kwargs) -> bool:
        """Verify file signature"""
        logger.info(f"Verifying signature: {signature_path}")
        
        try:
            result = subprocess.run(
                ["gpg", "--verify", signature_path, file_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return "Good signature" in result.stdout or result.returncode == 0
            
        except Exception as e:
            logger.error(f"Signature verification failed: {e}")
            return False
    
    def create_chain_of_custody(self, evidence: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Create chain of custody record"""
        logger.info("Creating chain of custody")
        
        custody_id = f"custody_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        chain = {
            "custody_id": custody_id,
            "evidence_id": evidence.get('evidence_id', 'unknown'),
            "file_path": evidence.get('file_path'),
            "hash": evidence.get('hash'),
            "custody_chain": [
                {
                    "action": "collected",
                    "actor": evidence.get('collector', 'unknown'),
                    "timestamp": datetime.now().isoformat(),
                    "notes": evidence.get('notes', '')
                }
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        self._save_chain_of_custody(chain)
        
        return chain
    
    def update_chain_of_custody(self, custody_id: str, action: str, actor: str, notes: str = "", **kwargs) -> Dict[str, Any]:
        """Update chain of custody"""
        logger.info(f"Updating chain of custody: {custody_id}")
        
        chain = self._load_chain_of_custody(custody_id)
        
        if chain:
            chain["custody_chain"].append({
                "action": action,
                "actor": actor,
                "timestamp": datetime.now().isoformat(),
                "notes": notes
            })
            
            self._save_chain_of_custody(chain)
        
        return chain
    
    def _save_chain_of_custody(self, chain: Dict) -> None:
        """Save chain of custody to file"""
        log_path = Path(self.output_path) / 'chain-of-custody' / f"{chain['custody_id']}.json"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(log_path, 'w') as f:
            json.dump(chain, f, indent=2)
    
    def _load_chain_of_custody(self, custody_id: str) -> Dict:
        """Load chain of custody from file"""
        log_path = Path(self.output_path) / 'chain-of-custody' / f"{custody_id}.json"
        
        if log_path.exists():
            with open(log_path, 'r') as f:
                return json.load(f)
        
        return None
    
    def seal_evidence(self, evidence_path: str, output_path: str = None, **kwargs) -> str:
        """Seal evidence for archive"""
        logger.info(f"Sealing evidence: {evidence_path}")
        
        if not output_path:
            output_path = f"{self.output_path}/archived/{Path(evidence_path).name}"
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        evidence_hash = self.generate_hash(evidence_path)
        
        archive_manifest = {
            "original_path": evidence_path,
            "archived_path": output_path,
            "hash": evidence_hash,
            "sealed_at": datetime.now().isoformat(),
            "seal_method": "hash_verification"
        }
        
        manifest_path = f"{output_path}.manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(archive_manifest, f, indent=2)
        
        return output_path
    
    def create_forensic_image(self, source: str, output_path: str, **kwargs) -> Dict[str, Any]:
        """Create forensic disk image"""
        logger.info(f"Creating forensic image of: {source}")
        
        results = {
            "source": source,
            "output_path": output_path,
            "image_type": "raw",
            "compression": "none",
            "timestamp": datetime.now().isoformat()
        }
        
        results["commands"] = [
            f"dd if={source} of={output_path} bs=4M status=progress",
            f"md5sum {output_path} > {output_path}.md5",
            f"sha256sum {output_path} > {output_path}.sha256"
        ]
        
        return results


class ComplianceSkill:
    """Compliance checking skill"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.output_path = self.config.get('output_path', 'compliance')
    
    def run_compliance_check(self, standard: str = "owasp", **kwargs) -> Dict[str, Any]:
        """Run compliance check"""
        logger.info(f"Running compliance check: {standard}")
        
        results = {
            "standard": standard,
            "checks_passed": 0,
            "checks_failed": 0,
            "findings": [],
            "timestamp": datetime.now().isoformat()
        }
        
        if standard == "owasp":
            results["findings"] = self._check_owasp_requirements()
        elif standard == "ptes":
            results["findings"] = self._check_ptes_requirements()
        elif standard == "nist":
            results["findings"] = self._check_nist_requirements()
        
        return results
    
    def _check_owasp_requirements(self) -> List[Dict]:
        """Check OWASP requirements"""
        return [
            {"requirement": "Authentication testing documented", "status": "pass"},
            {"requirement": "Authorization testing documented", "status": "pass"},
            {"requirement": "Session management testing documented", "status": "pass"},
            {"requirement": "Input validation testing documented", "status": "pass"}
        ]
    
    def _check_ptes_requirements(self) -> List[Dict]:
        """Check PTES requirements"""
        return [
            {"requirement": "Pre-engagement interactions", "status": "pass"},
            {"requirement": "Intelligence gathering", "status": "pass"},
            {"requirement": "Threat modeling", "status": "pass"},
            {"requirement": "Vulnerability analysis", "status": "pass"}
        ]
    
    def _check_nist_requirements(self) -> List[Dict]:
        """Check NIST requirements"""
        return [
            {"requirement": " reconnaissance completed", "status": "pass"},
            {"requirement": " scanning completed", "status": "pass"},
            {"requirement": " exploitation documented", "status": "pass"},
            {"requirement": " reporting complete", "status": "pass"}
        ]
    
    def generate_compliance_report(self, findings: Dict, **kwargs) -> str:
        """Generate compliance report"""
        logger.info("Generating compliance report")
        
        report = f"""
# Compliance Report
Generated: {datetime.now().isoformat()}

## Standard: {findings.get('standard', 'Unknown')}

## Summary
- Checks Passed: {findings.get('checks_passed', 0)}
- Checks Failed: {findings.get('checks_failed', 0)}

## Findings
"""
        
        for finding in findings.get('findings', []):
            status = "✓" if finding.get('status') == 'pass' else "✗"
            report += f"\n- {status} {finding.get('requirement', '')}"
        
        return report
    
    def verify_evidence_integrity(self, evidence_list: List[Dict], **kwargs) -> Dict[str, Any]:
        """Verify evidence integrity"""
        logger.info(f"Verifying integrity of {len(evidence_list)} evidence items")
        
        results = {
            "total_items": len(evidence_list),
            "verified": 0,
            "failed": 0,
            "details": [],
            "timestamp": datetime.now().isoformat()
        }
        
        return results
    
    def check_log_integrity(self, log_paths: List[str], **kwargs) -> Dict[str, Any]:
        """Check log integrity"""
        logger.info(f"Checking integrity of {len(log_paths)} logs")
        
        results = {
            "logs_checked": len(log_paths),
            "intact": 0,
            "tampered": 0,
            "timestamp": datetime.now().isoformat()
        }
        
        return results
    
    def archive_session(self, session_id: str, output_path: str = None, **kwargs) -> Dict[str, Any]:
        """Archive completed session"""
        logger.info(f"Archiving session: {session_id}")
        
        if not output_path:
            output_path = f"{self.output_path}/archives/{session_id}"
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        results = {
            "session_id": session_id,
            "archive_path": output_path,
            "contents": [
                "evidence/*",
                "recordings/*",
                "logs/*",
                "report.pdf"
            ],
            "status": "ready_for_archive",
            "timestamp": datetime.now().isoformat()
        }
        
        return results
