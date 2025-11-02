# football_squad.py
# Step 9: The Blueprint (Advanced Object-Oriented Python)

class Player:
    def __init__(self, name, position, goals, assists):
        self.name = name
        self.position = position
        self.stats = {"goals": goals, "assists": assists}

    def display_summary(self):
        print(f"Player: {self.name}, Position: {self.position}, Goals: {self.stats['goals']}")


class Goalkeeper(Player):
    def __init__(self, name, position, goals, assists, saves):
        super().__init__(name, position, goals, assists)
        self.saves = saves

    def display_summary(self):
        print(
            f"Goalkeeper: {self.name}, Position: {self.position}, "
            f"Goals: {self.stats['goals']}, Saves: {self.saves}"
        )


class Team:
    def __init__(self, name):
        self.name = name
        self.roster = []

    def add_player(self, player):
        self.roster.append(player)

    def get_top_scorer(self):
        return max(self.roster, key=lambda p: p.stats["goals"])

    def display_roster(self):
        print(f"Team: {self.name}")
        for player in self.roster:
            player.display_summary()


# --- Example Usage ---
if __name__ == "__main__":
    team = Team("Dream XI")

    team.add_player(Player("Messi", "Forward", 30, 12))
    team.add_player(Player("Ronaldo", "Forward", 28, 10))
    team.add_player(Player("Modric", "Midfielder", 8, 15))
    team.add_player(Goalkeeper("Neuer", "Goalkeeper", 0, 1, 120))

    team.display_roster()

    top_scorer = team.get_top_scorer()
    print(f"\n🏆 Top Scorer: {top_scorer.name} with {top_scorer.stats['goals']} goals!")
