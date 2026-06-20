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
        teams_data_excel["ID_A"]= result_a["ESPN_Team_ID"]
        teams_data_excel["Team_B"] = result_b["Team"]
        teams_data_excel["ID_B"] = result_b["ESPN_Team_ID"]


        return teams_data_excel




    def get_team_ids(self,table_data, excel_path="../winner_final/data/wnba.xlsx"):
        if table_data:
            team_a = table_data[0]["team_a"]
            team_b =  table_data[0]["team_b"]
            teams_telesport = self.get_team_data_from_excel(excel_path,team_a,team_b)


            return teams_telesport
        else:
            print ("Data did not found at Table ")
            return NULL
