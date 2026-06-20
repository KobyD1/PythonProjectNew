import requests

class EspnNbaApi:

    def __init__(self):
        pass

    def clean_score(self,val):
        try:
            return int(val.get("value") if isinstance(val, dict) else val)
        except:
            return 0

    def get_basketball_team_stats(self, team_id: int, league='nba'):

        if (league=='wnba'):

            url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/teams/{team_id}/schedule"
        else:
            url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{team_id}/schedule"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        if (not resp.status_code == 200):
            print ("$$$$$$$$ Response Code to API site.api.espn.com is not 200 check for Team ID $$$$$$$$")

        team_info = data.get("team") or {}
        team_name = (
            team_info.get("displayName")
            or team_info.get("shortDisplayName")
            or team_info.get("name")
            or str(team_id)
        )

        total_offensive_points = 0
        total_defensive_points = 0
        games_count = 0
        games_list = []

        events = data.get("events") or []
        for event in events:
            competitions = event.get("competitions") or []
            if not competitions:
                continue

            comp = competitions[0]
            status = comp.get("status", {}).get("type", {})
            if not status.get("completed"):
                continue

            competitors = comp.get("competitors") or []
            if len(competitors) < 2:
                continue


            home = next(c for c in competitors if c.get("homeAway") == "home")
            away = next(c for c in competitors if c.get("homeAway") == "away")

            home_team = home.get("team", {})
            away_team = away.get("team", {})

            home_name = home_team.get("displayName") or home_team.get("name")
            away_name = away_team.get("displayName") or away_team.get("name")

            home_score = self.clean_score(home.get("score"))
            away_score = self.clean_score(away.get("score"))

            # does the team is home or away
            if home_name == team_name:
                offensive_points = home_score
                defensive_points = away_score
                opponent = away_name
                location = "בית"
            elif away_name == team_name:
                offensive_points = away_score
                defensive_points = home_score
                opponent = home_name
                location = "חוץ"
            else:
                continue

            games_count += 1
            total_offensive_points += offensive_points
            total_defensive_points += defensive_points

            games_list.append({
                "date": event.get("date", "")[:10],
                "opponent": opponent,
                "location": location,
                "offensive_points": offensive_points,
                "defensive_points": defensive_points
            })

        if games_count == 0:
            print ("לא נמצאו משחקים לקבוצה")
            return None

        avg_offensive_points = total_offensive_points / games_count
        avg_defensive_points = total_defensive_points / games_count
        avg_total_points = (total_offensive_points + total_defensive_points) / games_count
        avg_diff = (total_offensive_points - total_defensive_points) / games_count
        print (f"******* {team_name} Data Information *******")
        print("ממוצע קליעות:", round(avg_offensive_points, 2))
        print("ממוצע ספיגות:", round(avg_defensive_points, 2))
        print("ממוצע נקודות למשחק:", round(avg_total_points, 2))
        print("ממוצע הפרשים:", round(avg_diff, 2))
        for g in games_list:
            print(
                f"{g['date']} | {g['location']} | נגד {g['opponent']} | {g['offensive_points']} - {g['defensive_points']}")

        return {
            "team": team_name,
            "team_id": team_id,
            "games": games_count,
            "avg_offensive_points": avg_offensive_points,
            "avg_defensive_points": avg_defensive_points,
            "avg_total_points": avg_total_points,
            "avg_diff": avg_diff,
            "games_list": games_list

        }


