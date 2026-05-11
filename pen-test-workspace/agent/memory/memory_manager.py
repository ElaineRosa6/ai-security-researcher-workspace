"""
Memory Manager - Multi-layer Memory System
Handles short-term, medium-term, long-term, episodic, and semantic memory
"""

import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)


class ShortTermMemory:
    """Short-term memory - current session, recent actions"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.max_size = self.config.get('max_size', 100)
        self.retention_hours = self.config.get('retention_hours', 24)
        
        self.data = {
            "session_id": None,
            "timestamp": datetime.now().isoformat(),
            "current_task": None,
            "current_step": None,
            "recent_actions": [],
            "active_context": {},
            "working_memory": {}
        }
    
    def store(self, data: Any, key: str = None) -> None:
        """Store data in short-term memory"""
        if key:
            self.data[key] = data
        else:
            if isinstance(data, dict):
                self.data.update(data)
        
        if len(self.data.get('recent_actions', [])) >= self.max_size:
            self.data['recent_actions'].pop(0)
    
    def retrieve(self, key: str = None) -> Any:
        """Retrieve data from short-term memory"""
        if key:
            return self.data.get(key)
        return self.data
    
    def add_action(self, action: Dict[str, Any]) -> None:
        """Add an action to recent actions"""
        action_entry = {
            "action_id": self._generate_id(),
            "action_type": action.get('type'),
            "content": action.get('content'),
            "result": action.get('result'),
            "timestamp": datetime.now().isoformat()
        }
        self.data['recent_actions'].append(action_entry)
    
    def clear(self) -> None:
        """Clear short-term memory"""
        self.data = {
            "session_id": self.data.get('session_id'),
            "timestamp": datetime.now().isoformat(),
            "current_task": None,
            "current_step": None,
            "recent_actions": [],
            "active_context": {},
            "working_memory": {}
        }
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"action_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


class MediumTermMemory:
    """Medium-term memory - session data, discoveries, target profiles"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.max_sessions = self.config.get('max_sessions', 10)
        self.retention_days = self.config.get('retention_days', 30)
        
        self.storage_path = Path(self.config.get('storage_path', 'workspace-data/current-session'))
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.data = {
            "session_id": None,
            "discoveries": [],
            "attack_history": [],
            "target_profile": {},
            "decision_history": [],
            "failure_analysis": []
        }
    
    def store(self, data: Any, key: str = None) -> None:
        """Store data in medium-term memory"""
        if key:
            if isinstance(data, list):
                self.data[key] = self.data.get(key, []) + data
            else:
                self.data[key] = data
        
        self._persist()
    
    def retrieve(self, key: str = None) -> Any:
        """Retrieve data from medium-term memory"""
        self._load()
        
        if key:
            return self.data.get(key)
        return self.data
    
    def add_discovery(self, discovery: Dict[str, Any]) -> None:
        """Add a security finding"""
        discovery_entry = {
            "discovery_id": self._generate_id(),
            "type": discovery.get('type'),
            "severity": discovery.get('severity'),
            "content": discovery.get('content'),
            "evidence": discovery.get('evidence', []),
            "confidence": discovery.get('confidence', 0.8),
            "timestamp": datetime.now().isoformat(),
            "exploitable": discovery.get('exploitable', False)
        }
        self.data['discoveries'].append(discovery_entry)
        self._persist()
    
    def add_decision(self, decision: Dict[str, Any]) -> None:
        """Record a decision"""
        self.data['decision_history'].append({
            "decision_id": self._generate_id(),
            "context": decision.get('context'),
            "decision": decision.get('decision'),
            "reasoning": decision.get('reasoning'),
            "timestamp": datetime.now().isoformat()
        })
        self._persist()
    
    def update_target_profile(self, profile: Dict[str, Any]) -> None:
        """Update target profile"""
        self.data['target_profile'].update(profile)
        self._persist()
    
    def _persist(self) -> None:
        """Persist memory to disk"""
        if self.data.get('session_id'):
            file_path = self.storage_path / f"{self.data['session_id']}.json"
            with open(file_path, 'w') as f:
                json.dump(self.data, f, indent=2)
    
    def _load(self) -> None:
        """Load memory from disk"""
        if self.data.get('session_id'):
            file_path = self.storage_path / f"{self.data['session_id']}.json"
            if file_path.exists():
                with open(file_path, 'r') as f:
                    loaded = json.load(f)
                    for key, value in loaded.items():
                        if key not in self.data:
                            self.data[key] = value
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"disc_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    
    def consolidate_to_long_term(self, long_term_memory) -> None:
        """Consolidate important data to long-term memory"""
        for discovery in self.data.get('discoveries', []):
            if discovery.get('confidence', 0) > 0.9:
                long_term_memory.store_knowledge({
                    "type": "vulnerability",
                    "data": discovery
                })


class LongTermMemory:
    """Long-term memory - persistent knowledge base"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.storage_path = Path(self.config.get('storage_path', 'workspace-data/knowledge-base'))
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.knowledge_base = self._load_knowledge_base()
    
    def store_knowledge(self, knowledge: Dict[str, Any]) -> None:
        """Store knowledge in long-term memory"""
        category = knowledge.get('type', 'general')
        
        if category not in self.knowledge_base:
            self.knowledge_base[category] = []
        
        knowledge_entry = {
            "id": self._generate_id(),
            "data": knowledge,
            "timestamp": datetime.now().isoformat(),
            "access_count": 0,
            "last_accessed": datetime.now().isoformat()
        }
        
        self.knowledge_base[category].append(knowledge_entry)
        self._persist()
    
    def retrieve_knowledge(self, category: str = None, query: str = None) -> List[Dict[str, Any]]:
        """Retrieve knowledge from long-term memory"""
        if category:
            results = self.knowledge_base.get(category, [])
        else:
            results = []
            for cat_data in self.knowledge_base.values():
                results.extend(cat_data)
        
        if query:
            results = [r for r in results if query.lower() in str(r.get('data', {})).lower()]
        
        for result in results:
            result['access_count'] += 1
            result['last_accessed'] = datetime.now().isoformat()
        
        return results
    
    def get_patterns(self) -> Dict[str, Any]:
        """Get recognized patterns"""
        return {
            "common_attack_paths": self.knowledge_base.get('attack_patterns', []),
            "typical_configurations": self.knowledge_base.get('configurations', []),
            "vulnerability_patterns": self.knowledge_base.get('vulnerability_patterns', [])
        }
    
    def store_experience(self, experience: Dict[str, Any]) -> None:
        """Store an experience"""
        if 'experiences' not in self.knowledge_base:
            self.knowledge_base['experiences'] = []
        
        self.knowledge_base['experiences'].append({
            "id": self._generate_id(),
            "experience": experience,
            "timestamp": datetime.now().isoformat()
        })
        self._persist()
    
    def _load_knowledge_base(self) -> Dict[str, List]:
        """Load knowledge base from disk"""
        kb_file = self.storage_path / 'knowledge_base.json'
        if kb_file.exists():
            with open(kb_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _persist(self) -> None:
        """Persist knowledge base to disk"""
        kb_file = self.storage_path / 'knowledge_base.json'
        with open(kb_file, 'w') as f:
            json.dump(self.knowledge_base, f, indent=2)
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"kb_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


class EpisodicMemory:
    """Episodic memory - stores complete episodes/scenarios"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.storage_path = Path(self.config.get('storage_path', 'workspace-data/knowledge-base/episodes'))
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.episodes = []
        self.episode_timeline = []
    
    def store_episode(self, episode: Dict[str, Any]) -> str:
        """Store a complete episode"""
        episode_id = self._generate_id()
        
        episode_entry = {
            "episode_id": episode_id,
            "type": episode.get('type'),
            "description": episode.get('description'),
            "context": episode.get('context'),
            "actions": episode.get('actions', []),
            "outcomes": episode.get('outcomes', []),
            "timestamp": datetime.now().isoformat(),
            "related_episodes": []
        }
        
        self.episodes.append(episode_entry)
        self.episode_timeline.append(episode_entry)
        
        self._persist()
        
        return episode_id
    
    def retrieve_episodes(self, query: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Retrieve episodes based on query"""
        results = self.episodes
        
        if query:
            if 'type' in query:
                results = [e for e in results if e.get('type') == query['type']]
            if 'time_range' in query:
                start = query['time_range'].get('start')
                end = query['time_range'].get('end')
                results = [e for e in results 
                          if start <= e.get('timestamp') <= end]
        
        return results
    
    def get_timeline(self) -> List[Dict[str, Any]]:
        """Get chronological episode timeline"""
        return sorted(self.episode_timeline, 
                     key=lambda x: x.get('timestamp', ''))
    
    def _persist(self) -> None:
        """Persist episodes to disk"""
        file_path = self.storage_path / 'episodes.json'
        with open(file_path, 'w') as f:
            json.dump({
                'episodes': self.episodes,
                'timeline': self.episode_timeline
            }, f, indent=2)
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"ep_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


class SemanticMemory:
    """Semantic memory - concepts, relationships, domain knowledge"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.storage_path = Path(self.config.get('storage_path', 'workspace-data/knowledge-base/semantic'))
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.concepts = {}
        self.relationships = {}
        self.categories = self._load_taxonomy()
    
    def store_concept(self, concept: Dict[str, Any]) -> None:
        """Store a concept"""
        concept_id = concept.get('id', self._generate_id())
        self.concepts[concept_id] = {
            "id": concept_id,
            "name": concept.get('name'),
            "definition": concept.get('definition'),
            "properties": concept.get('properties', {}),
            "examples": concept.get('examples', []),
            "timestamp": datetime.now().isoformat()
        }
        self._persist()
    
    def store_relationship(self, from_concept: str, to_concept: str, 
                          relation_type: str, properties: Dict = None) -> None:
        """Store a relationship between concepts"""
        if from_concept not in self.relationships:
            self.relationships[from_concept] = []
        
        self.relationships[from_concept].append({
            "to": to_concept,
            "type": relation_type,
            "properties": properties or {},
            "timestamp": datetime.now().isoformat()
        })
        self._persist()
    
    def query_concepts(self, query: str) -> List[Dict[str, Any]]:
        """Query concepts"""
        query_lower = query.lower()
        results = []
        
        for concept in self.concepts.values():
            if (query_lower in concept.get('name', '').lower() or
                query_lower in concept.get('definition', '').lower()):
                results.append(concept)
        
        return results
    
    def get_related_concepts(self, concept_id: str) -> List[Dict[str, Any]]:
        """Get concepts related to a given concept"""
        related = []
        
        for rel in self.relationships.get(concept_id, []):
            to_id = rel.get('to')
            if to_id in self.concepts:
                related.append({
                    "concept": self.concepts[to_id],
                    "relationship": rel
                })
        
        return related
    
    def _load_taxonomy(self) -> Dict[str, Any]:
        """Load taxonomy from disk"""
        file_path = self.storage_path / 'taxonomy.json'
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        
        return {
            "vulnerability_types": [],
            "attack_techniques": [],
            "tools": [],
            "methodologies": []
        }
    
    def _persist(self) -> None:
        """Persist semantic memory to disk"""
        file_path = self.storage_path / 'semantic.json'
        with open(file_path, 'w') as f:
            json.dump({
                'concepts': self.concepts,
                'relationships': self.relationships,
                'categories': self.categories
            }, f, indent=2)
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        return f"sem_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


class MemoryManager:
    """Central manager for all memory systems"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        
        self.short_term = ShortTermMemory(self.config.get('short_term'))
        self.medium_term = MediumTermMemory(self.config.get('medium_term'))
        self.long_term = LongTermMemory(self.config.get('long_term'))
        self.episodic = EpisodicMemory(self.config.get('episodic'))
        self.semantic = SemanticMemory(self.config.get('semantic'))
        
        self._init_session()
    
    def _init_session(self) -> None:
        """Initialize new session"""
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.short_term.store('session_id', session_id)
        self.medium_term.data['session_id'] = session_id
    
    def store(self, data: Any, memory_type: str) -> None:
        """Store data in specified memory layer"""
        if memory_type == 'short_term':
            self.short_term.store(data)
        elif memory_type == 'medium_term':
            self.medium_term.store(data)
        elif memory_type == 'long_term':
            self.long_term.store_knowledge(data)
        elif memory_type == 'episodic':
            self.episodic.store_episode(data)
        elif memory_type == 'semantic':
            self.semantic.store_concept(data)
    
    def retrieve(self, memory_type: str = None, query: str = None) -> Any:
        """Retrieve data from memory"""
        if memory_type == 'short_term':
            return self.short_term.retrieve(query)
        elif memory_type == 'medium_term':
            return self.medium_term.retrieve(query)
        elif memory_type == 'long_term':
            return self.long_term.retrieve_knowledge(query=query)
        elif memory_type == 'episodic':
            return self.episodic.retrieve_episodes(query)
        elif memory_type == 'semantic':
            return self.semantic.query_concepts(query) if query else self.semantic.concepts
        else:
            return {
                'short_term': self.short_term.retrieve(),
                'medium_term': self.medium_term.retrieve(),
                'long_term': self.long_term.retrieve_knowledge(),
                'episodic': self.episodic.episodes,
                'semantic': self.semantic.concepts
            }
    
    def consolidate(self) -> None:
        """Consolidate memories - move short-term to long-term"""
        medium_data = self.medium_term.retrieve()
        
        for discovery in medium_data.get('discoveries', []):
            if discovery.get('confidence', 0) > 0.9:
                self.long_term.store_knowledge({
                    "type": "vulnerability",
                    "data": discovery
                })
        
        if medium_data.get('target_profile'):
            self.long_term.store_knowledge({
                "type": "target_profile",
                "data": medium_data['target_profile']
            })
    
    def forget(self, criteria: Dict[str, Any]) -> int:
        """Selective forgetting based on criteria"""
        forgotten = 0
        
        if criteria.get('type') == 'age':
            max_age_days = criteria.get('max_age_days', 30)
            cutoff = datetime.now() - timedelta(days=max_age_days)
            
            for episode in self.episodic.episodes[:]:
                episode_time = datetime.fromisoformat(episode['timestamp'])
                if episode_time < cutoff:
                    self.episodic.episodes.remove(episode)
                    forgotten += 1
        
        return forgotten
    
    def get_context(self) -> Dict[str, Any]:
        """Get current context from all memory layers"""
        return {
            "current_task": self.short_term.retrieve('current_task'),
            "recent_actions": self.short_term.retrieve('recent_actions')[-5:],
            "active_context": self.short_term.retrieve('active_context'),
            "discoveries": self.medium_term.retrieve('discoveries'),
            "target_profile": self.medium_term.retrieve('target_profile'),
            "session_id": self.short_term.retrieve('session_id')
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """Get memory summary"""
        return {
            "short_term_size": len(self.short_term.retrieve('recent_actions', [])),
            "medium_term_discoveries": len(self.medium_term.retrieve('discoveries', [])),
            "long_term_items": sum(len(v) for v in self.long_term.knowledge_base.values()),
            "episodic_count": len(self.episodic.episodes),
            "semantic_concepts": len(self.semantic.concepts)
        }
