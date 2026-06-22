from asyncio.windows_events import NULL
import os
import unicodedata

import pandas as pd

from winner_final.globals import EXCEL_PREFIX


class FilesUtils:
    def __init__(self):
        pass




    def get_team_data_from_excel(self,excel_path: str, team_a: str, team_b: str):

        teams_data_excel = {}
        try:

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

        except:
            print (f"team data not found at excel {excel_path} ,teams : {team_a}, {team_b}")


        return teams_data_excel





    def get_team_ids(self,table_data, excel_file="wnba.xlsx"):
        path= EXCEL_PREFIX+excel_file
        if table_data:
            team_a = table_data["team_a"]
            team_b =  table_data["team_b"]
            teams_telesport = self.get_team_data_from_excel(path,team_a,team_b)
            table_data["Team_A"] =teams_telesport["Team_A"]
            table_data["ID_A"] =teams_telesport["ID_A"]
            table_data["Team_B"] = teams_telesport["Team_B"]
            table_data["ID_B"] = teams_telesport["ID_B"]

            return table_data
        else:
            print (f"Data did not found at Table {excel_file}")
            return None

    def visual_length(self, text):
        """ מחשב אורך ויזואלי נכון גם לעברית וגם לאנגלית """
        import unicodedata
        count = 0
        for ch in text:
            if unicodedata.bidirectional(ch) in ("R", "AL"):
                count += 1
            else:
                count += 1
        return count

    def print_results(self, results_sorted):
        if results_sorted:
            headers = ["Favorite", "Game", "Plan", "Score"]

            rows = [
                [
                    str(item["favorite"]),
                    str(item["game"]),
                    str(item["plan"]),
                    f"{item['score']*10:.2f}"
                ]
                for item in results_sorted
            ]

            # calc. width of Col.
            col_widths = []
            for col in range(len(headers)):
                max_len = max(
                    self.visual_length(headers[col]),
                    max(self.visual_length(row[col]) for row in rows)
                )
                col_widths.append(max_len)

            def build_separator(left, fill, middle, right):
                parts = [left]
                for i, w in enumerate(col_widths):
                    parts.append(fill * (w + 2))
                    parts.append(middle if i < len(col_widths) - 1 else right)
                return "".join(parts)

            def build_row(values):
                parts = ["│"]
                for i, v in enumerate(values):
                    pad = col_widths[i] - self.visual_length(v)
                    parts.append(" " + v + " " * (pad + 1))
                    parts.append("│")
                return "".join(parts)

            print(build_separator("┌", "─", "┬", "┐"))
            print(build_row(headers))
            print(build_separator("├", "─", "┼", "┤"))

            for row in rows:
                print(build_row(row))

            print(build_separator("└", "─", "┴", "┘"))



