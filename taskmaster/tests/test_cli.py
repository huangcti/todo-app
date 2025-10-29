import subprocess
import sys
import json
import os
import pytest

# Assuming the main.py file has a function called `run_cli` that handles the CLI commands
from src.taskmaster.main import run_cli

def test_help_command(capfd):
    """Test that the help command displays the correct information."""
    run_cli(['help'])
    captured = capfd.readouterr()
    assert "Usage:" in captured.out
    assert "Commands:" in captured.out

def test_add_task():
    """Test adding a task."""
    run_cli(['add', 'Test task'])
    # Assuming there's a function to get tasks from the JSON storage
    tasks = get_tasks_from_storage()
    assert any(task['name'] == 'Test task' for task in tasks)

def test_list_tasks(capfd):
    """Test listing tasks."""
    run_cli(['list'])
    captured = capfd.readouterr()
    assert "Test task" in captured.out

def test_complete_task():
    """Test completing a task."""
    run_cli(['complete', 'Test task'])
    tasks = get_tasks_from_storage()
    assert all(task['name'] != 'Test task' for task in tasks)

def test_delete_task():
    """Test deleting a task."""
    run_cli(['delete', 'Test task'])
    tasks = get_tasks_from_storage()
    assert all(task['name'] != 'Test task' for task in tasks)

def get_tasks_from_storage():
    """Helper function to retrieve tasks from JSON storage."""
    storage_path = os.path.expanduser('~/.taskmaster.json')
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            return json.load(f)
    return []