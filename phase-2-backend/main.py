from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId
from database import players_collection

app = FastAPI()

class Player(BaseModel):
    name: str
    age: int
    country: str

def serialize_player(player):
    return {
        "id": str(player["_id"]),
        "name": player["name"],
        "age": player["age"],
        "country": player["country"],
    }

@app.get("/players")
def get_players():
    players = list(players_collection.find())
    return [serialize_player(p) for p in players]

@app.post("/players")
def create_player(player: Player):
    new_player = player.dict()
    result = players_collection.insert_one(new_player)
    created = players_collection.find_one({"_id": result.inserted_id})
    return serialize_player(created)

@app.put("/players/{player_id}")
def update_player(player_id: str, player: Player):
    players_collection.update_one(
        {"_id": ObjectId(player_id)},
        {"$set": player.dict()}
    )
    updated = players_collection.find_one({"_id": ObjectId(player_id)})
    return serialize_player(updated)

@app.delete("/players/{player_id}")
def delete_player(player_id: str):
    players_collection.delete_one({"_id": ObjectId(player_id)})
    return {"status": "deleted"}
