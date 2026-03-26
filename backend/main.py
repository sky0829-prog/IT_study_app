from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# データ保存（仮）
todos = []

class Todo(BaseModel):
    task: str

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo.task)
    return {"message": "追加成功"}

@app.delete("/todos/{index}")
def delete_todo(index: int):
    todos.pop(index)
    return {"message": "削除成功"}