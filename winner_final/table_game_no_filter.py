from winner_final.globals import DAYS, FILTER, PATH_PROGRAM_TEXT
from winner_final.utils.algo_utils import AlgoUtils
from winner_final.utils.espn_nba_api import EspnNbaApi
from winner_final.utils.files_utils import FilesUtils
from winner_final.utils.playwright_telersport_ui import PlaywrightMainUI

playwright_main = PlaywrightMainUI()
files_utils = FilesUtils()
algo_utils = AlgoUtils()
table_data =playwright_main.set_telesport_page(1,1,"wnba")
path = files_utils.save_output(table_data, PATH_PROGRAM_TEXT,"program")
files_utils.convert_txt_folder_to_pdf(PATH_PROGRAM_TEXT+"/results")


print ("********  End  *********")