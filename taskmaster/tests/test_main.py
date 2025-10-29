import pytest
from src.taskmaster.main import TaskMaster

def test_add_task():
    taskmaster = TaskMaster()
    taskmaster.add_task("Test task")
    assert len(taskmaster.tasks) == 1
    assert taskmaster.tasks[0].name == "Test task"

def test_list_tasks():
    taskmaster = TaskMaster()
    taskmaster.add_task("Test task 1")
    taskmaster.add_task("Test task 2")
    tasks = taskmaster.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].name == "Test task 1"
    assert tasks[1].name == "Test task 2"

def test_complete_task():
    taskmaster = TaskMaster()
    taskmaster.add_task("Test task")
    taskmaster.complete_task(0)
    assert taskmaster.tasks[0].completed is True

def test_delete_task():
    taskmaster = TaskMaster()
    taskmaster.add_task("Test task")
    taskmaster.delete_task(0)
    assert len(taskmaster.tasks) == 0

def test_task_storage():
    taskmaster = TaskMaster()
    taskmaster.add_task("Test task")
    taskmaster.save_tasks()
    taskmaster.load_tasks()
    assert len(taskmaster.tasks) == 1
    assert taskmaster.tasks[0].name == "Test task"