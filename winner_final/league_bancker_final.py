from winner_final.globals import DAYS, PATH_PROGRAM_TEXT, FILTER
from winner_final.utils.algo_utils import AlgoUtils
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.football_data_api import FootballDataApi
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI

football_data_api = FootballDataApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
table_data =playwright_main.set_telesport_page( 2,DAYS,"spain")
for data in table_data:
    if data["description"]=='2 Teams Game Results':
        teams_data_excel= files_utils.get_teams_names_from_excel("spain.xlsx",data.get("team_a"),data.get("team_b") )
        team_a_data = football_data_api.get_team_data("PD",teams_data_excel.get("team_a"))
        team_b_data = football_data_api.get_team_data("PD",teams_data_excel.get("team_b"))
        points  = algo_utils.calculate_football_algo(team_a_data,team_b_data)

        print (f"Found {points} points at {data['description']} , game {data.get('team_a')} vs {data.get('team_b')}")






print ("********  End  *********")