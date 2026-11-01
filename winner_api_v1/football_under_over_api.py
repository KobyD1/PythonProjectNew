from winner_api_v1.globals import DAYS, LEAGUE
from winner_api_v1.utils.render_api import RenderApi
from winner_api_v1.utils.algo_utils import AlgoUtils
from winner_api_v1.utils.files_utils import FilesUtils
from winner_api_v1.utils.football_data_api import FootballDataApi
from winner_api_v1.utils.playwright_telersport_ui import PlaywrightMainUI

football_data_api = FootballDataApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
results_not_sorted =[]

league_code = files_utils.get_league_code(LEAGUE)
render_api = RenderApi(league_code)
render_api.get_teams()
table_data, is_found =playwright_main.set_telesport_page( DAYS,2,LEAGUE)
matches, standings = render_api.get_all_football_league_data()

if is_found:
    for data in table_data:
        print (f"******* Game : {data["game"]} - {data['team_a']} VS {data['team_b']} *******")
        if data["description"] == '2 Teams Under/Over 2-3 Range':

            teams_data_excel= files_utils.get_teams_names_from_excel("football_all.xlsx",data.get("team_a"),data.get("team_b") )
            team_data_a =render_api.get_teams_data(teams_data_excel.get("team_a"),matches,standings)
            team_data_b =render_api.get_teams_data(teams_data_excel.get("team_b"),matches,standings)
            under_response = render_api.calc_football_under(team_data_a, team_data_b, data["description"])
            favorite = under_response["favorite"]
            # score , favorite ,avg_total = algo_utils.calc_football_under_over_api_algo(team_data_a, team_data_b,data["description"])
            if (favorite != 0):
                bet = data[f"bet{favorite}"]
                if favorite == 3: favorite = "X"
                results_not_sorted.append({"bet": bet, "score":under_response["score"], "favorite": under_response["favorite"], "plan": data["game"],
                                           'game': data["game_in_program"], "avg_total": under_response["avg_total"]})

    headers =  ["Favorite", "Game", "Plan", "Score", "Bet", "Avg Goals"]
    results_sorted = sorted(results_not_sorted, key=lambda x: x["score"], reverse=True)
    files_utils.print_results(results_sorted,headers,"** Summery Results for Under-Over 2-3 goals **")


print ("********  End  *********")