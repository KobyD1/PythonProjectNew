from winner_final.globals import DAYS, FILTER, PATH_PROGRAM_TEXT
from winner_final.utils.algo_utils import AlgoUtils
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.football_data_api import FootballDataApi
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI

# 1. Initialize services once
football_data_api = FootballDataApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()

TARGET_DESCRIPTION = "2 Teams Under/Over 2-3 Range"
EXCEL_FILE = "football_all.xlsx"
day = DAYS


def process_league_games(day: int, type: int, league_name: str, league_code: str) -> list[dict]:
    results = []
    table_data = playwright_main.set_telesport_page(day, type, league_name)

    for data in table_data:
        team_a = data.get("team_a")
        team_b = data.get("team_b")
        print(f"******* Game : {data.get('game')} - {team_a} VS {team_b} *******")

        if data.get("description") != TARGET_DESCRIPTION:
            continue

        teams_data_excel = files_utils.get_teams_names_from_excel(EXCEL_FILE, team_a, team_b)
        teams_data = football_data_api.get_teams_data(
            league_code,
            [teams_data_excel.get("team_a"), teams_data_excel.get("team_b")]
        )

        score, favorite, avg_total = algo_utils.calc_football_under_over_algo(
            teams_data[0], teams_data[1], data["description"]
        )

        if favorite != 0:
            bet = data.get(f"bet{favorite}")
            favorite_label = "X" if favorite == 3 else favorite

            results.append({
                "bet": bet,
                "score": score,
                "favorite": favorite_label,
                "plan": data.get("game"),
                "game": data.get("game_in_program"),
                "avg_total": avg_total,
            })

    return results


def main():
    targets = [
        ( "spain", "PD"),
        (  "england", "PL"),
    ]

    results_not_sorted = []
    for   league_name, league_code in targets:
        results_not_sorted.extend(process_league_games(day, 2, league_name, league_code))

    headers = ["Favorite", "Game", "Plan", "Score", "Bet", "Avg Goals"]
    results_sorted = sorted(results_not_sorted, key=lambda x: x["score"], reverse=True)

    files_utils.print_results(results_sorted, headers, "** Summary Results for Under-Over 2-3 goals **")
    print("********  End  *********")


if __name__ == "__main__":
    main()