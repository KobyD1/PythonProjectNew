from winner_final.globals import DAYS, FILTER, PATH_PROGRAM_TEXT
from winner_final.utils.algo_utils import AlgoUtils
from winner_final.utils.espn_nba_api import EspnNbaApi
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI

playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
table_data =playwright_main.set_telesport_page(0,0,"wnba")
files_utils.wrote_to_text_file(table_data, PATH_PROGRAM_TEXT,"program")


print ("********  End  *********")