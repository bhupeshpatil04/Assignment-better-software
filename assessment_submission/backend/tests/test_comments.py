
import json
import pytest
from backend import app as flask_app
from backend.app import tasks

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        # clear tasks before each test
        tasks.clear()
        yield client

def test_add_list_edit_delete_comment(client):
    task_id = "task-1"
    # initially empty
    rv = client.get(f"/tasks/{task_id}/comments")
    assert rv.status_code == 200
    assert rv.get_json() == []

    # add comment (missing text -> 400)
    rv = client.post(f"/tasks/{task_id}/comments", json={})
    assert rv.status_code == 400

    # add valid comment
    rv = client.post(f"/tasks/{task_id}/comments", json={"text":"hello","author":"bhupesh"})
    assert rv.status_code == 201
    c = rv.get_json()
    assert c["text"] == "hello"
    cid = c["id"]

    # list comments
    rv = client.get(f"/tasks/{task_id}/comments")
    assert rv.status_code == 200
    arr = rv.get_json()
    assert len(arr) == 1

    # edit comment
    rv = client.put(f"/tasks/{task_id}/comments/{cid}", json={"text":"edited"})
    assert rv.status_code == 200
    assert rv.get_json()["text"] == "edited"

    # delete comment
    rv = client.delete(f"/tasks/{task_id}/comments/{cid}")
    assert rv.status_code == 200
    assert "deleted" in rv.get_json()

    # deleting again returns 404
    rv = client.delete(f"/tasks/{task_id}/comments/{cid}")
    assert rv.status_code == 404
