#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

from fastapi import FastAPI, HTTPException

from model import exerciseSchema, userSchema

from database import (
    fetch_one_exercises,
    fetch_one_users,
    fetch_all_exercises,
    fetch_all_users,
    create_exercises,
    create_users,
    update_exercise,
    update_user,
    remove_exercise,
    remove_user,
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

# what is a middleware?
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/exercises")
async def get_exercises():
    response = await fetch_all_exercises()
    return response

@app.get("/users")
async def get_users():
    response = await fetch_all_users()
    return response

@app.post("/users/add", response_model=userSchema)
async def post_users(user:userSchema):
    response = await create_users(user.dict())
    if response:
        return response
    raise HTTPException(400, "fail to add user")

@app.delete("/exercises")
async def delete_exercises(id):
    response = await remove_exercise(id)
    if response:
        return response
    raise HTTPException(400, "fail to add exercise")

@app.post("/exercises/add", response_model=exerciseSchema)
async def post_exercises(exercises:exerciseSchema):
    response = await create_exercises(exercises.dict())
    if response:
        return response
    raise HTTPException(400, "fail to add exercises")

@app.get("/exercises/{id}", response_model=exerciseSchema)
async def delete_exercises():
    return

@app.post("/exercises/update/{id}", response_model=exerciseSchema)
async def delete_exercises():
    return

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/api/todo")
# async def get_todo():
#     response = await fetch_all_todos()
#     return response


# @app.get("/api/todo/{title}", response_model=Todo)
# async def get_todo_by_title(title):
#     response = await fetch_one_todo(title)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {title}")


# @app.post("/api/todo/", response_model=Todo)
# async def post_todo(todo: Todo):
#     response = await create_todo(todo.dict())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong")


# @app.put("/api/todo/{title}/", response_model=Todo)
# async def put_todo(title: str, desc: str):
#     response = await update_todo(title, desc)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {title}")


# @app.delete("/api/todo/{title}")
# async def delete_todo(title):
#     response = await remove_todo(title)
#     if response:
#         return "Successfully deleted todo"
#     raise HTTPException(404, f"There is no todo with the title {title}")
