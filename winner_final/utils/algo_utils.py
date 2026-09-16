class AlgoUtils:
    def __init__(self):
        pass

    def calculate_football_algo(self, team_a_data, team_b_data):
         position_diff = int(team_a_data["Position"].iloc[0])-int(team_b_data["Position"].iloc[0])
         points_diff = int(team_a_data["Points"].iloc[0]) - int(team_b_data["Points"].iloc[0])
         if (abs(position_diff>10)):
             print ("Teams  found for Bancker Algo by position")
             points = abs(position_diff)*10
             if (abs(points_diff > 10)):
                 print("Teams  found for Bancker Algo by points")
                 points = points + (abs(points_diff) * 10)
             # add points in case of home
             if int(team_a_data["Position"].iloc[0]) > int(team_b_data["Position"].iloc[0]):
                 points+=20
                 return points


         else :
             print ("Teams positions diff are not for Bancker Algo")
             return 0

    def under_over_algo(self,team_a,team_b,ref):
        print(f" Calculate Under Over for {team_a} and {team_b} with {ref}")

    def calculate_game_basketball_algo(self,team_a_data,team_b_data,data):
        result = {}

        match data["description"]:
            case "2 Teams Game Results":

                print(f"Calculate Game results {team_a_data} and {team_b_data}")

                team_added = data["team_with_added_points"]
                rate = data["rate"]


                if data["team_b"] == team_added:
                    added_diff = team_b_data['avg_diff']
                    other_diff = team_a_data['avg_diff']
                    bet_added = data["bet2"]
                    bet_other = data["bet1"]
                    favorite_added = "2"
                    favorite_other = "1"

                else:
                    added_diff = team_a_data['avg_diff']
                    other_diff = team_b_data['avg_diff']
                    bet_added = data["bet1"]
                    bet_other = data["bet2"]
                    favorite_added = "1"
                    favorite_other = "2"

                score = added_diff + rate - other_diff

                if score > 0:
                    favorite = favorite_added
                    result["bet"] = bet_added
                else:
                    favorite = favorite_other
                    result["bet"] = bet_other
                    score = -score

                    team_to_add,score_add = self.presentage_calculator(team_a_data, team_b_data,favorite)
                    if team_to_add ==favorite:
                        score =score+score_add
                        print (f"adding bonus {score_add} for presentage found ")
                print(f"****  Score found, score = {score} ,favorite = {favorite} game = {data["team_a"]} VS {data["team_b"]} ****")


                result["favorite"] = favorite
                result["score"] = score
                result = self.data_parser(data,result)

                return result

            case  "2 Teams Under/Over":
                print(f"Calculate Game results for under over {team_a_data} and {team_b_data}")
                avg_total = (team_a_data['avg_total_points'] + team_b_data['avg_total_points']) / 2
                diff = int(avg_total - data["rate"])
                if abs(diff) > 10:
                    result["score"] = diff + 5  # bonus for high def
                    print(
                        f"***** High Under found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")

                elif diff < 10 and diff >-10 :
                    result["score"] = diff
                    print(
                        f"***** Under/Over results, ממוצע נקודות למשחק = {avg_total} |ערך נקודות מטופס = {data["rate"]}| game = {data["team_a"]} VS{data["team_b"]} *****")

                if diff>0 : # case of Over
                    result["favorite"]="1"
                    result["bet"] = data["bet1"]
                else:  # case of Under
                    result["favorite"]="2"
                    result["bet"] = data["bet2"]

                result = self.data_parser(data,result)


                return result

            case "2 Teams 3 points Under/Over":
             pass

    def data_parser(self,data,result):
        game = data["game"].split(" ")[2].replace(".", "").strip()
        plan = data["game"].split(" ")[0][1:2]

        result["game"] = game
        result["plan"] = plan
        return result

    def presentage_calculator(self,team_a_data,team_b_data,favorite):
        score_add = (team_b_data['win_percentage'] - team_a_data['win_percentage']) / 10

        if team_b_data['win_percentage'] > team_a_data['win_percentage'] and favorite == "2":
            team_to_add = "2"

        elif team_b_data['win_percentage'] < team_a_data['win_percentage'] and favorite == "1":
            team_to_add = "1"
        return team_to_add,score_add










