from os import path
from pmgr.project import Project, TaskException
import pytest

name = "test"
proj = Project(name)
task = "test task"
fn = "./.projects/" + name + ".txt"

def test_add():
    proj.add_task(task)
    with open(fn, 'r') as f:
        assert f.read() == task + "\n"

def test_fail_add():
    with pytest.raises(Exception):
        proj.add_task(task)

def test_show():
    ret = proj.get_tasks()
    assert ret[0] == task

def test_remove():
    proj.remove_task(task)
    with open(fn, 'r') as f:
        assert f.read() != task

def test_fail_remove():
    with pytest.raises(Exception):
        proj.remove_task(task)

'''
def test_delete():
    proj.delete()
    assert !path.exists(fn)
'''
