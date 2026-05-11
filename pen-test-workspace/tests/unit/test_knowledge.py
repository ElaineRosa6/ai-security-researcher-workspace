"""Tests for Knowledge Graph functionality"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.knowledge.graph import KnowledgeGraph


class TestKnowledgeGraph:
    """Test knowledge graph operations"""

    def setup_method(self):
        self.graph = KnowledgeGraph()

    def test_graph_initialization(self):
        """Test graph can be initialized"""
        assert self.graph is not None

    def test_store_knowledge(self):
        """Test storing knowledge entries"""
        entry = {"type": "vulnerability", "cve": "CVE-2024-001"}
        self.graph.store(entry, key="vuln_001")
        assert self.graph.retrieve("vuln_001") == entry

    def test_retrieve_nonexistent(self):
        """Test retrieving non-existent entry"""
        assert self.graph.retrieve("nonexistent") is None

    def test_store_multiple(self):
        """Test storing multiple entries"""
        self.graph.store({"name": "SQLi"}, key="vuln_001")
        self.graph.store({"name": "XSS"}, key="vuln_002")
        assert self.graph.retrieve("vuln_001") is not None
        assert self.graph.retrieve("vuln_002") is not None

    def test_get_knowledge_list(self):
        """Test getting all knowledge entries"""
        self.graph.store({"data": 1}, key="k1")
        self.graph.store({"data": 2}, key="k2")
        knowledge_list = self.graph.retrieve()
        assert isinstance(knowledge_list, dict) or hasattr(knowledge_list, '__iter__')
