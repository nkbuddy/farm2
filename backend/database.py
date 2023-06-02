#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import exerciseSchema, userSchema

USERS_DB_URI='mongodb+srv://admin-alan:test123@cluster0.gibibte.mongodb.net/?retryWrites=true&w=majority/'

client = motor.motor_asyncio.AsyncIOMotorClient(USERS_DB_URI)
database = client.test
exercises_collection = database.exercises
users_collection = database.users

async def fetch_one_exercises(id):
    document = await exercises_collection.find_one({"_id": id})
    return document

async def fetch_one_users(id):
    document = await users_collection.find_one({"_id": id})
    return document

async def fetch_all_exercises():
    exercises = []
    cursor = exercises_collection.find({})
    async for document in cursor:
        exercises.append(exerciseSchema(**document))
    return exercises

async def fetch_all_users():
    users = []
    cursor = users_collection.find({})
    async for document in cursor:
        users.append(userSchema(**document))
    return users

async def create_exercises(exercises):
    document = exercises
    result = await exercises_collection.insert_one(document)
    return result

async def create_users(users):
    document = users
    result = await users_collection.insert_one(document)
    return result

async def update_exercise(id,username,description,duration):
    await exercises_collection.update_one({"_id":id},{"$set":{"username":username,"description":description,"duration":duration}})
    document = await exercises_collection.find_one({"_id":id})
    return document

async def update_user(id,username):
    await users_collection.update_one({"_id":id},{"$set":{"username":username}})
    return

async def remove_exercise(id):
    await exercises_collection.delete_one({"_id":id})
    return True

async def remove_user(id):
    await users_collection.delete_one({"_id":id})
    return True

# async def fetch_one_todo(title):
#     document = await collection.find_one({"title": title})
#     return document
#
# async def fetch_all_todos():
#     todos = []
#     cursor = collection.find({})
#     async for document in cursor:
#         todos.append(Todo(**document))
#     return todos

# async def create_todo(todo):
#     document = todo
#     result = await collection.insert_one(document)
#     return document

# async def update_todo(title, desc):
#     await collection.update_one({"title": title}, {"$set": {"description": desc}})
#     document = await collection.find_one({"title": title})
#     return document

# async def remove_todo(title):
#     await collection.delete_one({"title": title})
#     return True