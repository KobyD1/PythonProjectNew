import requests

TEAM_NAME = "Manchester United FC"

BASE_URL = "https://pythonprojectnew-ps0h.onrender.com"

# קריאת טבלה
standings = requests.get(
    f"{BASE_URL}/standings"
).json()

# קריאת כל המשחקים
matches = requests.get(
    f"{BASE_URL}/all-results"
).json()

# מציאת נתוני הקבוצה בטבלה
team_table_data = None

for team in standings:

    if team["team"] == TEAM_NAME:
        team_table_data = team
        break

if team_table_data is None:
    print("הקבוצה לא נמצאה")
    exit()

games = 0
total_goals_sum = 0

count_0_1 = 0
count_2_3 = 0
count_4_plus = 0

for match in matches:

    home_team = match["home_team"]
    away_team = match["away_team"]

    if TEAM_NAME not in [home_team, away_team]:
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

print("\n" + "=" * 60)
print(TEAM_NAME)
print("=" * 60)

print(f"מיקום: {team_table_data['position']}")
print(f"נקודות: {team_table_data['points']}")

print(f"משחקים: {games}")

print(
    f"ממוצע שערים כולל למשחק: "
    f"{avg_goals:.2f}"
)

print(
    f"0-1 שערים: "
    f"{count_0_1} "
    f"({pct_0_1:.2f}%)"
)

print(
    f"2-3 שערים: "
    f"{count_2_3} "
    f"({pct_2_3:.2f}%)"
)

print(
    f"4+ שערים: "
    f"{count_4_plus} "
    f"({pct_4_plus:.2f}%)"
)
