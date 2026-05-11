"""
Knowledge Graph - Vulnerability Database, Attack Patterns, Tool Knowledge
"""

import json
import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class KnowledgeGraph:
    """Knowledge graph for security knowledge management"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.graph = {
            "nodes": [],
            "edges": [],
            "node_index": {},
            "edge_index": {}
        }
        
        self.base_path = Path(self.config.get('base_path', 'agent/knowledge'))
        self._load_knowledge()
    
    def _load_knowledge(self) -> None:
        """Load knowledge from disk"""
        vulnerability_db = self.base_path / 'vulnerability_db'
        if vulnerability_db.exists():
            self._load_vulnerability_db(vulnerability_db)
        
        attack_patterns = self.base_path / 'attack_patterns'
        if attack_patterns.exists():
            self._load_attack_patterns(attack_patterns)
        
        tool_knowledge = self.base_path / 'tool_knowledge'
        if tool_knowledge.exists():
            self._load_tool_knowledge(tool_knowledge)
    
    def _load_vulnerability_db(self, path: Path) -> None:
        """Load vulnerability database"""
        for file in path.glob('*.json'):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    
                    if isinstance(data, list):
                        for vuln in data:
                            self.add_vulnerability(vuln)
                    elif isinstance(data, dict):
                        if 'vulnerabilities' in data:
                            for vuln in data['vulnerabilities']:
                                self.add_vulnerability(vuln)
            except Exception as e:
                logger.warning(f"Failed to load {file}: {e}")
    
    def _load_attack_patterns(self, path: Path) -> None:
        """Load attack patterns"""
        for file in path.glob('*.json'):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    
                    if isinstance(data, list):
                        for pattern in data:
                            self.add_attack_pattern(pattern)
                    elif isinstance(data, dict):
                        if 'patterns' in data:
                            for pattern in data['patterns']:
                                self.add_attack_pattern(pattern)
            except Exception as e:
                logger.warning(f"Failed to load {file}: {e}")
    
    def _load_tool_knowledge(self, path: Path) -> None:
        """Load tool knowledge"""
        for file in path.glob('*.json'):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.add_tool_knowledge(data)
            except Exception as e:
                logger.warning(f"Failed to load {file}: {e}")
    
    def add_node(self, node_id: str, node_type: str, properties: Dict[str, Any]) -> None:
        """Add a node to the graph"""
        node = {
            "id": node_id,
            "type": node_type,
            "properties": properties,
            "created_at": datetime.now().isoformat()
        }
        
        if node_id not in self.graph['node_index']:
            self.graph['nodes'].append(node)
            self.graph['node_index'][node_id] = node
        else:
            self.graph['node_index'][node_id].update(properties)
    
    def add_edge(self, from_node: str, to_node: str, 
                 relation_type: str, properties: Dict = None) -> None:
        """Add an edge to the graph"""
        edge_id = f"{from_node}__{relation_type}__{to_node}"
        
        edge = {
            "id": edge_id,
            "from": from_node,
            "to": to_node,
            "type": relation_type,
            "properties": properties or {},
            "created_at": datetime.now().isoformat()
        }
        
        if edge_id not in self.graph['edge_index']:
            self.graph['edges'].append(edge)
            self.graph['edge_index'][edge_id] = edge
    
    def add_vulnerability(self, vulnerability: Dict[str, Any]) -> None:
        """Add a vulnerability to the knowledge base"""
        vuln_id = vulnerability.get('id', vulnerability.get('cve_id', self._generate_id()))
        
        self.add_node(vuln_id, 'vulnerability', vulnerability)
        
        for related_id in vulnerability.get('related', []):
            self.add_edge(vuln_id, related_id, 'related_to')
        
        for technique in vulnerability.get('techniques', []):
            self.add_edge(vuln_id, technique, 'can_be_exploited_with')
    
    def add_attack_pattern(self, pattern: Dict[str, Any]) -> None:
        """Add an attack pattern"""
        pattern_id = pattern.get('id', self._generate_id())
        
        self.add_node(pattern_id, 'attack_pattern', pattern)
        
        for prereq in pattern.get('prerequisites', []):
            self.add_edge(pattern_id, prereq, 'requires')
        
        for target in pattern.get('target_technologies', []):
            self.add_edge(pattern_id, target, 'targets')
    
    def add_tool_knowledge(self, tool_info: Dict[str, Any]) -> None:
        """Add tool knowledge"""
        tool_id = tool_info.get('id', tool_info.get('name', self._generate_id()))
        
        self.add_node(tool_id, 'tool', tool_info)
        
        for vuln in tool_info.get('detects', []):
            self.add_edge(tool_id, vuln, 'detects')
    
    def query(self, query_pattern: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Query the graph"""
        results = []
        
        node_type = query_pattern.get('type')
        if node_type:
            for node in self.graph['nodes']:
                if node.get('type') == node_type:
                    match = True
                    
                    for key, value in query_pattern.get('properties', {}).items():
                        if node.get('properties', {}).get(key) != value:
                            match = False
                            break
                    
                    if match:
                        results.append(node)
        
        return results
    
    def find_path(self, start_node: str, end_node: str, 
                  max_depth: int = 5) -> List[List[str]]:
        """Find paths between two nodes"""
        paths = []
        
        def dfs(current: str, target: str, path: List[str], visited: Set[str]):
            if len(path) > max_depth:
                return
            
            if current == target:
                paths.append(path.copy())
                return
            
            visited.add(current)
            
            for edge in self.graph['edges']:
                if edge['from'] == current and edge['to'] not in visited:
                    path.append(edge['to'])
                    dfs(edge['to'], target, path, visited)
                    path.pop()
            
            visited.remove(current)
        
        dfs(start_node, end_node, [start_node], set())
        
        return paths
    
    def get_subgraph(self, center_node: str, radius: int = 2) -> Dict[str, Any]:
        """Get subgraph centered on a node"""
        nodes_in_subgraph = {center_node}
        edges_in_subgraph = []
        
        current_layer = {center_node}
        
        for _ in range(radius):
            next_layer = set()
            
            for node in current_layer:
                for edge in self.graph['edges']:
                    if edge['from'] == node:
                        next_layer.add(edge['to'])
                        edges_in_subgraph.append(edge)
                    elif edge['to'] == node:
                        next_layer.add(edge['from'])
                        edges_in_subgraph.append(edge)
            
            nodes_in_subgraph.update(next_layer)
            current_layer = next_layer
        
        return {
            "nodes": [n for n in self.graph['nodes'] if n['id'] in nodes_in_subgraph],
            "edges": edges_in_subgraph
        }
    
    def get_target_profile(self, target_id: str) -> Dict[str, Any]:
        """Get or create target profile"""
        target = self.graph['node_index'].get(target_id)
        
        if not target:
            target = {
                "id": target_id,
                "type": "target",
                "properties": {
                    "basic_info": {},
                    "services": [],
                    "technologies": [],
                    "vulnerabilities": [],
                    "attack_surface": {
                        "attack_paths": [],
                        "entry_points": [],
                        "critical_assets": []
                    }
                }
            }
            self.add_node(target_id, 'target', target['properties'])
        
        return target
    
    def update_target_profile(self, target_id: str, profile_data: Dict[str, Any]) -> None:
        """Update target profile"""
        target = self.get_target_profile(target_id)
        
        for key, value in profile_data.items():
            target['properties'][key] = value
        
        self.graph['node_index'][target_id] = target
    
    def get_vulnerabilities_for_service(self, service: str) -> List[Dict[str, Any]]:
        """Get known vulnerabilities for a service"""
        vulnerabilities = []
        
        for node in self.graph['nodes']:
            if node['type'] == 'vulnerability':
                if service.lower() in str(node['properties']).lower():
                    vulnerabilities.append(node)
        
        return vulnerabilities
    
    def get_attack_chain(self, target_type: str) -> List[Dict[str, Any]]:
        """Get attack chain for a target type"""
        chain = []
        
        for pattern in self.query({'type': 'attack_pattern'}):
            if target_type.lower() in str(pattern.get('properties', {}).get('target_technologies', [])).lower():
                chain.append(pattern)
        
        return chain
    
    def save_knowledge(self) -> None:
        """Save knowledge to disk"""
        knowledge_path = self.base_path / 'graph_export.json'
        with open(knowledge_path, 'w') as f:
            json.dump(self.graph, f, indent=2)
        
        logger.info(f"Knowledge graph saved to {knowledge_path}")
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"kg_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
