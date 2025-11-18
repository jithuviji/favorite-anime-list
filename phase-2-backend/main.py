from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId

# MongoDB
from database import players_collection

# Supabase
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# --------------------------
# MongoDB Player Model
# --------------------------
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

# --------------------------
# MongoDB CRUD
# --------------------------
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


# ==========================
#   SUPABASE RELATIONAL API
# ==========================

# Relational Models
class Team(BaseModel):
    name: str

class PlayerSQL(BaseModel):
    name: str
    team_id: int | None = None   # Foreign Key


# --------------------------
# Create a Team
# --------------------------
@app.post("/teams")
def create_team(team: Team):
    result = supabase.table("teams").insert({"name": team.name}).execute()
    return result.data


# --------------------------
# Get All Teams
# --------------------------
@app.get("/teams")
def get_teams():
    result = supabase.table("teams").select("*").execute()
    return result.data


# --------------------------
# Create Player (SQL)
# --------------------------
@app.post("/players-sql")
def create_player_sql(player: PlayerSQL):
    result = supabase.table("players").insert({
        "name": player.name,
        "team_id": player.team_id
    }).execute()
    return result.data


# --------------------------
# Get Players in a Team
# --------------------------
@app.get("/teams/{team_id}/players")
def get_players_by_team(team_id: int):
    result = supabase.table("players").select("*").eq("team_id", team_id).execute()
    return result.data


# --------------------------
# Assign Player to a Team
# --------------------------
@app.put("/players/{player_id}/assign/{team_id}")
def assign_player_to_team(player_id: int, team_id: int):
    result = supabase.table("players") \
        .update({"team_id": team_id}) \
        .eq("id", player_id) \
        .execute()

    return result.data
