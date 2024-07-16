from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is my first route")
async def get_root():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": " hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}

@app.get("/users")
async def list_users():
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user():
    return {"Message": "This is the current user"}

@app.get("users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


#will be deviating from the main idea


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "you are healthy but sweeter"}



fake_items_db = [{"items_name": "Foo"}, {"items_name": "bar"}, {"items_name": "Foo"} ]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, sample_query_parameters: str , q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_parameters": sample_query_parameters}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"})
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"items_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"})
    return item
