import requests

def get_wnba_team_stats(team_id: int,league='nba'):

    if (league=='wnba'):

        url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/teams/{team_id}/schedule"
    else:
        url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{team_id}/schedule"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    team_info = data.get("team") or {}
    team_name = (
        team_info.get("displayName")
        or team_info.get("shortDisplayName")
        or team_info.get("name")
        or str(team_id)
    )

    total_scored = 0
    total_defensive_points = 0
    games_count = 0
    games_list = []   # ← נוסיף רשימה לשמירת המשחקים

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

        # זיהוי בית/חוץ אמיתי
        home = next(c for c in competitors if c.get("homeAway") == "home")
        away = next(c for c in competitors if c.get("homeAway") == "away")

        home_team = home.get("team", {})
        away_team = away.get("team", {})

        home_name = home_team.get("displayName") or home_team.get("name")
        away_name = away_team.get("displayName") or away_team.get("name")

        def clean_score(val):
            try:
                return int(val.get("value") if isinstance(val, dict) else val)
            except:
                return 0

        home_score = clean_score(home.get("score"))
        away_score = clean_score(away.get("score"))

        # האם הקבוצה היא בית או חוץ?
        if home_name == team_name:
            scored = home_score
            defensive_points = away_score
            opponent = away_name
            location = "בית"
        elif away_name == team_name:
            scored = away_score
            defensive_points = home_score
            opponent = home_name
            location = "חוץ"
        else:
            continue

        games_count += 1
        total_scored += scored
        total_defensive_points += defensive_points

        # שמירת המשחק ברשימה
        games_list.append({
            "date": event.get("date", "")[:10],
            "opponent": opponent,
            "location": location,
            "scored": scored,
            "defensive_points": defensive_points
        })

    if games_count == 0:
        return None

    avg_scored = total_scored / games_count
    avg_defensive_points = total_defensive_points / games_count
    avg_total_points = (total_scored + total_defensive_points) / games_count
    avg_diff = (total_scored - total_defensive_points) / games_count

    return {
        "team": team_name,
        "games": games_count,
        "avg_scored": avg_scored,
        "avg_defensive_points": avg_defensive_points,
        "avg_total_points": avg_total_points,
        "avg_diff": avg_diff,
        "games_list": games_list   # ← מחזירים גם את רשימת המשחקים
    }


# שימוש בפונקציה
team_id = 18  # Las Vegas Aces
stats = get_wnba_team_stats(team_id)

if stats:
    print("קבוצה:", stats["team"])
    print("משחקים:", stats["games"])
    print("ממוצע קליעות:", round(stats["avg_scored"], 2))
    print("ממוצע ספיגות:", round(stats["avg_defensive_points"], 2))
    print("ממוצע נקודות למשחק:", round(stats["avg_total_points"], 2))
    print("ממוצע הפרשים:", round(stats["avg_diff"], 2))

    print("\n--- כל המשחקים ---")
    for g in stats["games_list"]:
        print(f"{g['date']} | {g['location']} | נגד {g['opponent']} | {g['scored']} - {g['defensive_points']}")

else:
    print("לא נמצאו משחקים לקבוצה")
