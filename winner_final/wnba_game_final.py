from winner_final.utils.algo_utils import AlgoUtils
from winner_final.utils.espn_nba_api import EspnNbaApi
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI
from pprint import pprint
is_under_over = True
espn_nba_api = EspnNbaApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
table_data =playwright_main.set_telesport_page( "כדורסל",1,"wnba",is_under_over)
results_not_sorted =[]
for data in table_data:
    excel_data = files_utils.get_team_ids(data, "../winner_final/data/wnba.xlsx")

    stats_a = espn_nba_api.get_basketball_team_stats(excel_data["ID_A"], 'wnba')
    stats_b = espn_nba_api.get_basketball_team_stats(excel_data["ID_B"], 'wnba')
    results =algo_utils.calculate_game_basketball_algo(stats_a,stats_b,data)
    results_not_sorted.append(results)
results_sorted = sorted(results_not_sorted, key=lambda x: x["score"], reverse=True)
pprint(results_sorted)
print ("********  End  *********")