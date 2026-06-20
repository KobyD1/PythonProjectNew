
from winner_final.utils.espn_nba_api import EspnNbaApi
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI

espn_nba_api = EspnNbaApi()
playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()

table_data =playwright_main.set_telesport_page( "כדורסל",1,"wnba")
teams_telesport =files_utils.get_team_ids(table_data,"../winner_final/data/wnba.xlsx")


team_id = 18  # Las Vegas Aces
stats_a = espn_nba_api.get_wnba_team_stats(teams_telesport["ID_A"],'wnba')
stats_b = espn_nba_api.get_wnba_team_stats(18,'wnba')

espn_nba_api.get_team_data(stats_a)
espn_nba_api.get_team_data(stats_b)


print ("********  End  *********")