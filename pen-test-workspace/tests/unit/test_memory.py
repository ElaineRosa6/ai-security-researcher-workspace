"""Tests for Agent Memory System"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.memory.memory_manager import (
    ShortTermMemory,
    MediumTermMemory,
    LongTermMemory,
    EpisodicMemory,
    SemanticMemory,
    MemoryManager
)


class TestShortTermMemory:
    """Test short-term memory functionality"""

    def setup_method(self):
        self.memory = ShortTermMemory()

    def test_store_retrieve_by_key(self):
        self.memory.store("test_value", key="test_key")
        assert self.memory.retrieve("test_key") == "test_value"

    def test_store_dict(self):
        self.memory.store({"key1": "value1", "key2": "value2"})
        assert self.memory.retrieve("key1") == "value1"
        assert self.memory.retrieve("key2") == "value2"

    def test_retrieve_all(self):
        self.memory.store("value1", key="key1")
        all_data = self.memory.retrieve()
        assert isinstance(all_data, dict)

    def test_add_action(self):
        action = {"type": "scan", "content": "nmap scan", "result": "ports found"}
        self.memory.add_action(action)
        actions = self.memory.data.get('recent_actions', [])
        assert len(actions) == 1
        assert actions[0]['action_type'] == 'scan'

    def test_clear(self):
        self.memory.store("value1", key="key1")
        self.memory.clear()
        assert self.memory.retrieve("key1") is None

    def test_max_size(self):
        for i in range(150):
            self.memory.add_action({"type": "test", "content": f"action_{i}"})
        assert len(self.memory.data['recent_actions']) <= 100


class TestMediumTermMemory:
    """Test medium-term memory functionality"""

    def setup_method(self):
        self.memory = MediumTermMemory()

    def test_store_discovery(self):
        discovery = {"type": "open_port", "port": 22, "service": "ssh"}
        self.memory.store(discovery, key="discovery_1")
        assert self.memory.retrieve("discovery_1") == discovery

    def test_store_target_profile(self):
        profile = {"target": "192.168.1.1", "os": "Linux"}
        self.memory.store(profile, key="target_profile")
        assert self.memory.retrieve("target_profile") == profile

    def test_store_decision(self):
        decision = {"action": "proceed", "reason": "vulnerability confirmed"}
        self.memory.store(decision, key="decision_1")
        assert self.memory.retrieve("decision_1") == decision


class TestLongTermMemory:
    """Test long-term memory functionality"""

    def setup_method(self):
        self.memory = LongTermMemory()

    def test_store_knowledge(self):
        knowledge = {"cve": "CVE-2024-001", "severity": "critical"}
        self.memory.store(knowledge, key="vuln_001")
        assert self.memory.retrieve("vuln_001") == knowledge

    def test_store_learning(self):
        learning = {"topic": "SQL injection", "finding": "Always parameterized"}
        self.memory.store(learning, key="learning_sql")
        assert self.memory.retrieve("learning_sql") == learning


class TestEpisodicMemory:
    """Test episodic memory functionality"""

    def setup_method(self):
        self.memory = EpisodicMemory()

    def test_store_episode(self):
        episode = {
            "phase": "recon",
            "action": "port_scan",
            "result": {"open_ports": [22, 80, 443]}
        }
        self.memory.store(episode, key="episode_recon_1")
        assert self.memory.retrieve("episode_recon_1") == episode

    def test_store_sequence(self):
        for i in range(5):
            self.memory.store({"step": i}, key=f"step_{i}")
        assert self.memory.retrieve("step_0") is not None
        assert self.memory.retrieve("step_4") is not None


class TestSemanticMemory:
    """Test semantic memory functionality"""

    def setup_method(self):
        self.memory = SemanticMemory()

    def test_store_concept(self):
        concept = {"term": "SQLi", "definition": "SQL Injection vulnerability"}
        self.memory.store(concept, key="concept_sqli")
        assert self.memory.retrieve("concept_sqli") == concept

    def test_store_relationship(self):
        relationship = {"from": "SQLi", "to": "Injection", "type": "is_a"}
        self.memory.store(relationship, key="rel_sql")
        assert self.memory.retrieve("rel_sql") == relationship


class TestMemoryManager:
    """Test memory manager integration"""

    def setup_method(self):
        self.manager = MemoryManager()

    def test_store_short_term(self):
        data = {"key": "value"}
        self.manager.store(data, key="test_data")
        retrieved = self.manager.retrieve("test_data")
        assert retrieved == data

    def test_store_medium_term(self):
        data = {"discovery": "open_port"}
        self.manager.store(data, key="discovery_1")
        retrieved = self.manager.retrieve("discovery_1")
        assert retrieved == data

    def test_multiple_stores(self):
        self.manager.store("value1", key="key1")
        self.manager.store("value2", key="key2")
        self.manager.store("value3", key="key3")
        assert self.manager.retrieve("key1") == "value1"
        assert self.manager.retrieve("key2") == "value2"
        assert self.manager.retrieve("key3") == "value3"

    def test_store_updates_existing(self):
        self.manager.store("old_value", key="key1")
        self.manager.store("new_value", key="key1")
        assert self.manager.retrieve("key1") == "new_value"
