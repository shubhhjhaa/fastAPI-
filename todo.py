from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = [] #empty list

class todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:todo):
    todos.append(todo)
    return{
        'message':"todo created successfuuly",
        'data':todo
    }

@app.get("/showTodos")
def getTodos():
    return todos

#  path params

@app.get("/get_todos/{id}")
def get_todo(id:int):
    for todo in todos:
        if todo.id == id:
            return todo
        return {"error":"todo not found"}

#  update todo

@app.put("/todos/{id}")
def update_todo(id:int,updated_todo:todo):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todos[index]= updated_todo
            return{
                "message":"data updated successfully",
                "data":updated_todo
            }

# delete todo

@app.delete("/todos/{id}")
def delete_todo(id:int):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todos.pop(index)
    return{
        "message":"todo deleted successfully"
    }