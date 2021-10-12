from os import path
from pmgr.project import Project, TaskException
import pytest

name = "test"
proj = Project(name)
task = "test task"
fn = name + ".txt"

def test_add():
    proj.add_task(task)
    with open(fn, 'r') as f:
        assert f.read() == task

def test_fail_add():
    with pytest.raise(Exception):
        proj.add_task(task)

def test_show():
    ret = proj.get_tasks()
    assert ret == task

def test_remove():
    proj.remove_task(task)
    fileN =  name + ".txt"
    with open(fileN, 'r') as f:
        assert f.read() != task

def test_fail_remove():
    with pytest.raise(Exception):
        proj.remove_task(task)

'''
def test_delete():
    proj.delete()
    assert !path.exists(fn)
'''
