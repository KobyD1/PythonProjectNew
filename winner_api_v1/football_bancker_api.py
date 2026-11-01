
import sys
from pathlib import Path

from winner_api_v1.utils.files_utils import FilesUtils
from winner_api_v1.utils.football_data_api import FootballDataApi
from winner_api_v1.utils.playwright_ui_utils import PlaywrightMainUI
from winner_api_v1.utils.render_api import RenderApi

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

from globals import DAYS, LEAGUE
from utils.algo_utils import AlgoUtils


football_data_api = FootballDataApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
results_not_sorted =[]

render_api = RenderApi()
league_code=render_api.get_league_code(LEAGUE)
ui_config = render_api.get_ui_config()
table_data, is_found =playwright_main.set_main_page(DAYS, 2, ui_config,LEAGUE)
matches, standings = render_api.get_all_football_league_data(league_code)
results = []

if is_found:
    for data in table_data:
        if data["description"]=='2 Teams Game Results':
            print (f"*** Analyze {data.get('team_a')} vs {data.get('team_b')} ***")
            teams_data_excel= files_utils.get_teams_names_from_excel("football_all.xlsx",data.get("team_a"),data.get("team_b") )

            team_data_a =render_api.get_teams_data(teams_data_excel.get("team_a"),matches,standings)
            team_data_b =render_api.get_teams_data(teams_data_excel.get("team_b"),matches,standings)
            scores,favorite  = render_api.calc_football_banker(team_data_a, team_data_b)

            print (f"Found {scores} scores  , game {data.get('team_a')} vs {data.get('team_b')}")
            if favorite != 0:
                bet = data.get(f"bet{favorite}")

                results.append({
                    "bet": bet,
                    "score": scores,
                    "favorite": favorite,
                    "plan": data.get("game"),
                    "game": data.get("game_in_program"),
                    "avg_total":"-"
                })




    headers = ["Favorite", "Game", "Plan", "Score", "Bet", "Avg Goals"]
    results_sorted = sorted(results, key=lambda x: x["score"], reverse=True)

    files_utils.print_results(results_sorted, headers, "** Summary Results for Bancker **")
print ("********  End  *********")