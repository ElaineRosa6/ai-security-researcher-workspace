#!/bin/bash
# Test runner script
set -e

WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "========================================"
echo "  AI Security Researcher Workspace"
echo "  Test Runner"
echo "========================================"
echo ""

# Activate virtual environment
source "$WORKSPACE_ROOT/.venv/bin/activate"

# Add project root to Python path
export PYTHONPATH="$WORKSPACE_ROOT:$PYTHONPATH"

# Run tests
echo "Running unit tests..."
python -m pytest tests/unit -v --tb=short 2>&1 | tail -20

echo ""
echo "Running integration tests..."
python -m pytest tests/integration -v --tb=short 2>&1 | tail -20

echo ""
echo "Running end-to-end tests..."
python -m pytest tests/e2e -v --tb=short 2>&1 | tail -20

echo ""
echo "========================================"
echo "  Test Run Complete"
echo "========================================"
