from asyncio.windows_events import NULL
import os

import pandas as pd


class FilesUtils:
    def __init__(self):
        pass




    def get_team_data_from_excel(self,excel_path: str, team_a: str, team_b: str):
        teams_data_excel = {}

        df = pd.read_excel(excel_path)
        teams_telesport = df["Telesport"]
        team_a_data = df[teams_telesport == team_a]
        result_a = team_a_data.iloc[0].to_dict()

        team_b_data = df[teams_telesport == team_b]
        result_b = team_b_data.iloc[0].to_dict()
        teams_data_excel["Team_A"]= result_a["Team"]
        teams_data_excel["ID_A"]= str(result_a["ESPN_Team_ID"]).split(".")[0]
        teams_data_excel["Team_B"] = result_b["Team"]
        teams_data_excel["ID_B"] = str(result_b["ESPN_Team_ID"]).split(".")[0]


        return teams_data_excel




    def get_team_ids(self,table_data, excel_path="../winner_final/data/wnba.xlsx"):
        if table_data:
            team_a = table_data["team_a"]
            team_b =  table_data["team_b"]
            teams_telesport = self.get_team_data_from_excel(excel_path,team_a,team_b)
            table_data["Team_A"] =teams_telesport["Team_A"]
            table_data["ID_A"] =teams_telesport["ID_A"]
            table_data["Team_B"] = teams_telesport["Team_B"]
            table_data["ID_B"] = teams_telesport["ID_B"]


            return table_data
        else:
            print ("Data did not found at Table ")
            return None
