
import pandas as pd
import requests
class FootballDataApi:

    def __init__(self):

        self.url = f"https://api.football-data.org/v4/competitions/"
        self.headers = {"X-Auth-Token": "6e8b3c65a58f4a05b874d72fe4170fd7"}

    # PL (England), PD (Spain), SA (Italy)
    def get_team_data(self,league,team=""):
        response = requests.get(f"{self.url}{league}/standings", headers=self.headers)
        data = response.json()

        teams_data = []

        for entry in data["standings"][0]["table"]:
            team_name = entry["team"]["name"]

            if team and team.lower() not in team_name.lower():
                continue

            played = entry["playedGames"]
            goals_for = entry["goalsFor"]
            goals_against = entry["goalsAgainst"]
            total_goals = goals_for + goals_against

            if played > 0:
                teams_data.append(
                    {
                        "Position": int(entry["position"]),
                        "Team": team_name,
                        "Points": int(entry["points"]),
                        "Avg Goals For": round(goals_for / played, 2),
                        "Avg Goals Against": round(goals_against / played, 2),
                        "Avg Total Goals": round(total_goals / played, 2),
                    }
                )

        df = pd.DataFrame(teams_data)

        if not df.empty:
            print(df.to_string(index=False))
        else:
            print("No team matching the search criteria was found.")
        return df

    def is_valid_data(self, data):
     if (data.get("team_a").count("(")+data.get("team_b").count("(")>0):
        return False
     if (data.get("team_a").count("(")+data.get("team_b").count("(")>0):
        return False
