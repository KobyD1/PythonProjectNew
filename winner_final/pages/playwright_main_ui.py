import re


class telesport_main_page:

    def __init__(self,page):
        self.page = page

    def set_table_filters(self,title = "כדורגל"):
        self.page.locator("div.ddlTitleFilters").click()
        self.page.locator("#ddlBoxFilters").get_by_text(title).click()
        print (f"success to click on {title}")

    def set_table_league(self,league="wnba"):
        self.page.get_by_text("ליגות").nth(0).click()
        if league == "wnba":
            self.page.locator("#checkbox_1663").click()

        self.page.locator("div.sportlive_LeagueSelect_btnFilter").click()
        print (f"success to click on {league}")

    def set_date(self):
        self.page.locator("div.sportLive_calendar_left").click()

    def get_table_content(self, is_uder_over = False):
        table_content = []
        status_time=""
        rows = self.page.locator("tr.winnerBodyTr:visible").all()

        actual_index = 1
        for row in rows:
            if not row.is_visible():
                continue

            row_data= {}
            teams = row.locator(".th_td_WinnerteamsAndBetType").inner_text().strip()
            game = row.locator(".tdWinId").inner_text().replace(".","")
            if teams.count("מעל") :
                team_a,team_b,rate,description,team_with_added_points = self.teams_data_parser_uder_over(teams)
                status_time = row.locator(".tdWinnerStatus").inner_text().strip()
                row_data["status_time"] = status_time
                row_data["team_a"] = team_a
                row_data["team_b"] = team_b
                row_data["rate"] = rate
                row_data["description"] = description
                row_data["team_with_added_points"] = team_with_added_points
                row_data["game"] = game

                score = row.locator(".tdWinScore").inner_text().strip()
                bets = row.locator('[class*="th_td_WinnerBet"]').all()
                for bet in bets:
                    index = bets.index(bet)
                    row_data[f"bet{index}"] = bet.inner_text().strip()

            elif teams.count("+") > 0 :
                team_a,team_b,rate,description,team_with_added_points = self.teams_data_parser_game(teams)

                status_time = row.locator(".tdWinnerStatus").inner_text().strip()
                row_data["status_time"] = status_time
                row_data["team_a"] = team_a
                row_data["team_b"] = team_b
                row_data["rate"] = rate
                row_data["description"] = description
                row_data["team_with_added_points"] = team_with_added_points
                row_data["game"] = game

                score = row.locator(".tdWinScore").inner_text().strip()
                bets = row.locator('[class*="th_td_WinnerBet"]').all()

                for bet in bets:
                    index = bets.index(bet)
                    row_data[f"bet{index}"] = bet.inner_text().strip()


            if  ":"  in status_time and len(row_data)>0:
                print(f"-------------{game}-------------")
                print(f" משחק פעיל נמצא בתכניה ")

                print(f"שורה מספר {actual_index}:")
                print(f" שעת משחק_סטטוס: {status_time}")
                print(f"  קבוצות: {teams}")
                print(f"  תוצאה: {score}")
                print(f"  פרטי משחק(תכניה) משחק: {game}")

                print(f"  יתרון לקבוצה : {team_with_added_points}")

                row_data["team_with_added_points"] = team_with_added_points


                table_content.append(row_data)
            actual_index += 1
        return table_content

    def teams_data_parser_uder_over(self,teams):
        if teams.count("(") > 1:
            print("נמצא בתכניה " + teams)
            parts = teams.split("(")
            team_part = parts[1].split(")")[0]
            number_part = parts[2].split(")")[0]
            team = team_part.strip()
            rate = float(number_part)
            team_b = "not found"
            description = '1 Team Under/Over'
            team_with_added_points = ""

            return team,team_b,rate,description,team_with_added_points

        elif "שלשות" in teams:
            parts = teams.split("-")
            team_b = parts[1].strip()
            index_1 = parts[0].index(")") + 1
            index_2 = parts[0].index("(")

            team_a = parts[0][index_1:].strip()
            rate = float(parts[0][index_2 + 1:index_1 - 1].strip())
            description = '2 Teams 3 points Under/Over'
            team_with_added_points = "not found"

            return team_a,team_b,rate,description,team_with_added_points

        elif "מעל/מתחת" in teams:
            print("נמצא בתכניה " + teams)
            parts = teams.split("-")
            team_b = parts[1].strip()
            index_1 = parts[0].index(")")+1
            index_2 = parts[0].index("(")

            team_a = parts[0][index_1:].strip()
            rate = float(parts[0][index_2+1:index_1-1].strip())
            description = '2 Teams Under/Over'
            team_with_added_points = "not found"


            return team_a,team_b,rate,description,team_with_added_points


        else:
            return "not found","not found","not found","not found"


    def teams_data_parser_game(self,teams):
        row_data = {}
        print( teams +"נמצא בתכניה ")
        parts = teams.split("-")
        team_b = parts[1].strip().split("(")[0].strip()
        team_a= parts[0].strip().split("(")[0].strip()

        if parts[0].count("+") > 0:
            part_with_ref = parts[0]
            team_with_added_points = team_a
        else:
            part_with_ref = parts[1]
            team_with_added_points = team_b



        added_points =part_with_ref.split("-")[0].replace(")","")


        num = re.sub(r'[^\d\.\-+]', '', added_points)
        num = num.replace("..","")
        rate = float(num)
        row_data['description'] = '2 Teams Game Results'

        description = '2 Teams Game Results'
        return team_a,team_b,rate,description,team_with_added_points


    def add_row_data_to_table(self):
        pass
