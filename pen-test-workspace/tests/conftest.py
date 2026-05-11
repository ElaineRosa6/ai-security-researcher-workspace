"""Pytest configuration for test suite"""
import pytest
import sys
import os

# Add project root to Python path
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)


@pytest.fixture
def workspace_root():
    """Return the workspace root directory"""
    return os.path.join(os.path.dirname(__file__), '..')


@pytest.fixture
def config_dir(workspace_root):
    """Return the configuration directory"""
    return os.path.join(workspace_root, 'config')


@pytest.fixture
def workflow_dir(workspace_root):
    """Return the workflow directory"""
    return os.path.join(workspace_root, 'ai-agent', 'workflows')
