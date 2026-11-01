import requests


class RenderApi:

    def __init__(self, league_code="PL"):
        self.render_url = "https://pythonprojectnew-ps0h.onrender.com"
        self.league_code = league_code

    import requests



    def calc_football_under(self,team_a,team_b,desc="2 Teams Under/Over 2-3 Range"):

        payload = {
            "team_a": team_a,
            "team_b": team_b,
            "desc": desc
        }

        response = requests.post(f"{self.render_url}/football-under",json=payload)


        return response.json()

    def get_teams(self):

        data = requests.get(
            f"{self.render_url}/{self.league_code}/teams"
        ).json()

        return data["teams"]

    def get_all_football_league_data(self):

        print("getting all data from server , can take 30 sec.")

        standings_response = requests.get(
            f"{self.render_url}/{self.league_code}/standings"
        ).json()

        matches_response = requests.get(
            f"{self.render_url}/{self.league_code}/results"
        ).json()

        standings = standings_response["standings"]
        matches = matches_response["results"]

        return matches, standings

    def get_teams_data(self, team_name, matches, standings):

        team_table_data = None

        for team in standings:

            if team["team"] == team_name:
                team_table_data = team
                break

        if team_table_data is None:
            print("הקבוצה לא נמצאה")
            return None

        games = 0
        total_goals_sum = 0

        count_0_1 = 0
        count_2_3 = 0
        count_4_plus = 0

        for match in matches:

            home_team = match["home_team"]
            away_team = match["away_team"]

            if team_name not in [home_team, away_team]:
                continue

            home_goals = match["home_goals"]
            away_goals = match["away_goals"]

            if home_goals is None or away_goals is None:
                continue

            total_goals = home_goals + away_goals

            games += 1
            total_goals_sum += total_goals

            if total_goals <= 1:
                count_0_1 += 1

            elif 2 <= total_goals <= 3:
                count_2_3 += 1

            else:
                count_4_plus += 1

        avg_goals = (
            total_goals_sum / games
            if games > 0 else 0
        )

        pct_0_1 = (
            count_0_1 / games * 100
            if games > 0 else 0
        )

        pct_2_3 = (
            count_2_3 / games * 100
            if games > 0 else 0
        )

        pct_4_plus = (
            count_4_plus / games * 100
            if games > 0 else 0
        )

        team_data = {
            "Position": int(team_table_data["position"]),
            "Team": team_name,
            "Points": int(team_table_data["points"]),
            "avgGoals": round(avg_goals, 2),
            "count_0_1": round(pct_0_1, 2),
            "count_2_3": round(pct_2_3, 2),
            "count_4_plus": round(pct_4_plus, 2),
        }

        print(f"Team data for {team_name}: {team_data}")
        return team_data