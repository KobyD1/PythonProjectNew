import requests

API_KEY = "6e8b3c65a58f4a05b874d72fe4170fd7"
TEAM_ID = 66  # מנצ'סטר יונייטד

# משתני בקרה:
ONLY_PREMIER_LEAGUE = True  # True = רק פרמייר ליג, False = כל המסגרות
NUM_MATCHES = 8  # מספר המשחקים האחרונים שתרצה לחשב

URL = f"https://api.football-data.org/v4/teams/{TEAM_ID}/matches?status=FINISHED"

headers = {"X-Auth-Token": API_KEY}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    matches = data.get("matches", [])

    # סינון לפי ליגה אם הוגדר True
    if ONLY_PREMIER_LEAGUE:
        matches = [m for m in matches if m.get("competition", {}).get("code") == "PL"]

    # מיון המשחקים לפי תאריך מהחדש לישן וחיתך לפי הכמות המבוקשת
    matches = sorted(matches, key=lambda x: x.get("utcDate", ""), reverse=True)
    matches = matches[:NUM_MATCHES]

    count_1_goal = 0
    count_2_3_goals = 0
    count_over_3_goals = 0
    count_0_goals = 0
    total_matches = 0
    total_goals_sum = 0  # צבירת סך השערים לצורך חישוב ממוצע

    league_title = "בפרמייר ליג" if ONLY_PREMIER_LEAGUE else "בכל המסגרות"
    print(f"=== רשימת {len(matches)} המשחקים האחרונים {league_title} ===\n")

    for match in matches:
        score_data = match.get("score", {})
        full_time = score_data.get("fullTime", {})

        home_team = match.get("homeTeam", {}).get("name", "Unknown")
        away_team = match.get("awayTeam", {}).get("name", "Unknown")

        home_goals = full_time.get("home") if "home" in full_time else full_time.get("homeTeam")
        away_goals = full_time.get("away") if "away" in full_time else full_time.get("awayTeam")

        if home_goals is None or away_goals is None:
            continue

        total_game_goals = home_goals + away_goals
        total_matches += 1
        total_goals_sum += total_game_goals  # הוספת השערים לסך הכללי

        comp_name = match.get("competition", {}).get("name", "")
        print(f"[{comp_name}] {home_team} {home_goals} - {away_goals} {away_team} | סך שערים: {total_game_goals}")

        if total_game_goals == 1:
            count_1_goal += 1
        elif 2 <= total_game_goals <= 3:
            count_2_3_goals += 1
        elif total_game_goals > 3:
            count_over_3_goals += 1
        else:
            count_0_goals += 1

    pct_1 = (count_1_goal / total_matches * 100) if total_matches > 0 else 0
    pct_2_3 = (count_2_3_goals / total_matches * 100) if total_matches > 0 else 0
    pct_over_3 = (count_over_3_goals / total_matches * 100) if total_matches > 0 else 0
    pct_0 = (count_0_goals / total_matches * 100) if total_matches > 0 else 0

    # חישוב הממוצע הכולל של שערים למשחק
    avg_goals_per_match = (total_goals_sum / total_matches) if total_matches > 0 else 0

    print(f"\n==================================================")
    print(f"=== סיכום סטטיסטיקה עבור {total_matches} המשחקים האחרונים ===")
    print(f"==================================================")
    print(f"📊 ממוצע שערים כולל למשחק: {avg_goals_per_match:.2f}")
    print(f"⚽ משחקים שבהם הובקע גול יחיד בסך הכל (1): {count_1_goal} ({pct_1:.2f}%)")
    print(f"⚽⚽ משחקים שבהם הובקעו בין 2 ל-3 גולים בסך הכל (2-3): {count_2_3_goals} ({pct_2_3:.2f}%)")
    print(f"🔥 משחקים שבהם הובקעו מעל 3 גולים בסך הכל (4+): {count_over_3_goals} ({pct_over_3:.2f}%)")
    if count_0_goals > 0:
        print(f"⚪ משחקים ללא שערים (0-0): {count_0_goals} ({pct_0:.2f}%)")

else:
    print(f"שגיאה בחיבור ל-API: {response.status_code}")