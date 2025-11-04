from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Football Squad API", version="1.0")

# ----- Data Models -----
class Player(BaseModel):
    name: str
    position: str
    goals: int
    assists: int

# In-memory "database"
players_db: List[Player] = [
    Player(name="Lionel Messi", position="Forward", goals=30, assists=12),
    Player(name="Cristiano Ronaldo", position="Forward", goals=25, assists=8),
    Player(name="Kevin De Bruyne", position="Midfielder", goals=10, assists=18),
    Player(name="Virgil van Dijk", position="Defender", goals=4, assists=2),
]

# ----- Basic Routes -----
@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the Football Squad API!"}

@app.get("/anime/{title}")
def get_anime(title: str):
    return {"message": f"Anime '{title}' sounds awesome!"}

# ----- Query Parameters -----
@app.get("/players", response_model=List[Player])
def get_players(position: Optional[str] = Query(None, description="Filter by player position")):
    if position:
        filtered = [p for p in players_db if p.position.lower() == position.lower()]
        return filtered
    return players_db

# ----- Create -----
@app.post("/players", response_model=Player)
def add_player(player: Player):
    players_db.append(player)
    return player

# ----- Read -----
@app.get("/players/{name}", response_model=Player)
def get_player(name: str):
    for player in players_db:
        if player.name.lower() == name.lower():
            return player
    raise HTTPException(status_code=404, detail="Player not found")

# ----- Update -----
@app.put("/players/{name}", response_model=Player)
def update_player(name: str, updated_player: Player):
    for i, player in enumerate(players_db):
        if player.name.lower() == name.lower():
            players_db[i] = updated_player
            return updated_player
    raise HTTPException(status_code=404, detail="Player not found")

# ----- Delete -----
@app.delete("/players/{name}")
def delete_player(name: str):
    for i, player in enumerate(players_db):
        if player.name.lower() == name.lower():
            del players_db[i]
            return {"message": f"Player '{name}' removed successfully"}
    raise HTTPException(status_code=404, detail="Player not found")
