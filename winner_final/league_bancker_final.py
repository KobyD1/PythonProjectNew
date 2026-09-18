from winner_final.globals import DAYS, PATH_PROGRAM_TEXT, FILTER
from winner_final.utils.algo_utils import AlgoUtils
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.football_data_api import FootballDataApi
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI

football_data_api = FootballDataApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
table_data =playwright_main.set_telesport_page( 2,2,"spain")
for data in table_data:
    if data["description"]=='2 Teams Game Results':
        print (f"*** Analyze {data.get('team_a')} vs {data.get('team_b')} ***")
        teams_data_excel= files_utils.get_teams_names_from_excel("spain.xlsx",data.get("team_a"),data.get("team_b") )

        teams_data = football_data_api.get_teams_data("PD",[teams_data_excel.get("team_a"),teams_data_excel.get("team_b")])
        points  = algo_utils.calc_football_bancker_algo(teams_data[0], teams_data[1])

        print (f"Found {points[0]} points  , game {data.get('team_a')} vs {data.get('team_b')}")






print ("********  End  *********")