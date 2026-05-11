"""Tests for Workflow Engine functionality"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from agent.workflow.engine import StateTracker, State


class TestStateTracker:
    """Test state tracking functionality"""

    def setup_method(self):
        self.tracker = StateTracker()

    def test_initial_state(self):
        assert self.tracker.current_state == State.INITIALIZED

    def test_valid_transition(self):
        assert self.tracker.transition_to(State.REQUIREMENT_ANALYSIS) is True
        assert self.tracker.current_state == State.REQUIREMENT_ANALYSIS

    def test_invalid_transition(self):
        # Try to jump directly to COMPLETED from INITIALIZED
        result = self.tracker.transition_to(State.COMPLETED)
        assert result is False

    def test_state_history(self):
        self.tracker.transition_to(State.REQUIREMENT_ANALYSIS)
        self.tracker.transition_to(State.PLANNING)
        history = self.tracker.get_history()
        assert len(history) >= 3  # INITIALIZED + 2 transitions

    def test_full_workflow(self):
        """Test full penetration test workflow"""
        states = [
            State.INITIALIZED,
            State.REQUIREMENT_ANALYSIS,
            State.PLANNING,
            State.RECON,
            State.SCANNING,
            State.VULN_ASSESS,
            State.EXPLOITATION,
            State.POST_EXPLOIT,
            State.REPORTING,
            State.COMPLETED
        ]

        current = State.INITIALIZED
        for target in states[1:]:
            result = self.tracker.transition_to(target)
            assert result is True, f"Failed to transition from {current} to {target}"
            current = target

    def test_error_recovery(self):
        """Test recovery from error state"""
        self.tracker.transition_to(State.REQUIREMENT_ANALYSIS)
        self.tracker.transition_to(State.PLANNING)
        self.tracker.transition_to(State.ERROR)
        # Can recover to PLANNING
        assert self.tracker.transition_to(State.PLANNING) is True

    def test_get_current_state_info(self):
        """Test getting current state info"""
        self.tracker.transition_to(State.RECON)
        info = self.tracker.get_info()
        assert info is not None

    def test_pause_and_resume(self):
        """Test pause and resume workflow"""
        self.tracker.transition_to(State.RECON)
        self.tracker.transition_to(State.PAUSED)
        assert self.tracker.current_state == State.PAUSED
        # Resume to RECON
        assert self.tracker.transition_to(State.RECON) is True


class TestStateProperties:
    """Test state enum and properties"""

    def test_state_values(self):
        assert State.INITIALIZED == "INITIALIZED"
        assert State.COMPLETED == "COMPLETED"
        assert State.ERROR == "ERROR"

    def test_state_comparison(self):
        tracker = StateTracker()
        assert tracker.current_state == State.INITIALIZED
