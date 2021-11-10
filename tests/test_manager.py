from fastapi import responses, status
from fastapi.testclient import TestClient
from tasks_manager.manager import TASKS, app


def test_when_listing_tasks_should_return_status_code_200():
  client = TestClient(app)
  response = client.get('/tasks')
  assert response.status_code == status.HTTP_200_OK

def test_when_listing_tasks_return_in_json():
  client = TestClient(app)
  response = client.get('/tasks')
  assert response.headers['Content-Type'] == 'application/json'

def test_when_listing_tasks_should_return_a_list():
  client = TestClient(app)
  response = client.get('/tasks')
  assert isinstance(response.json(), list)

def test_when_listing_tasks_the_tasks_should_has_an_id():
  TASKS.append({'id':1})
  client = TestClient(app)
  response = client.get('/tasks')
  assert 'id' in response.json().pop()
  TASKS.clear()

def test_when_listing_tasks_the_tasks_should_has_a_title():
    TASKS.append({"title": "title 1"})
    cliente = TestClient(app)
    resposta = cliente.get("/tasks")
    assert "title" in resposta.json().pop()
    TASKS.clear()


def test_when_listing_tasks_the_tasks_should_has_a_description():
    TASKS.append({"description": "description 1"})
    client = TestClient(app)
    response = client.get("/tasks")
    assert "description" in response.json().pop()
    TASKS.clear()


def test_when_listing_tasks_the_tasks_should_has_a_state():
    TASKS.append({"state": "finished"})
    cliente = TestClient(app)
    resposta = cliente.get("/tasks")
    assert "state" in resposta.json().pop()
    TASKS.clear()
