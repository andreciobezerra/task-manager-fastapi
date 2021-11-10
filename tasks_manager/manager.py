from fastapi import FastAPI

TASKS = [
    {
        "id": "1",
        "title": "shopping",
        "description": "buy milk and eggs",
        "state": "not finished",
    },
    {
        "id": "2",
        "title": "study FMC2",
        "description": "study FMC2, section 6 for the Epp Book",
        "state": "not finished",
    },
    {
        "id": "3",
        "title": "washing",
        "description": "clouds are dirty, need washing",
        "state": "not finished",
    },
]


app = FastAPI()

@app.get('/tasks')
def list():
  return TASKS
