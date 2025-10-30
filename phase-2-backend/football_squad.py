# football_squad.py

# Create a list of player dictionaries
squad = [
    {"name": "Messi", "position": "Forward", "goals": 30},
    {"name": "Ronaldo", "position": "Forward", "goals": 28},
    {"name": "Modric", "position": "Midfielder", "goals": 8},
    {"name": "Salah", "position": "Forward", "goals": 25},
    {"name": "Van Dijk", "position": "Defender", "goals": 5},
]

# Define a function to find the top scorer
def find_top_scorer(squad):
    top_player = squad[0]
    for player in squad:
        if player["goals"] > top_player["goals"]:
            top_player = player
    return top_player

# Find and print the top scorer
top_scorer = find_top_scorer(squad)
print(f"🏆 The top scorer is {top_scorer['name']} with {top_scorer['goals']} goals!")
