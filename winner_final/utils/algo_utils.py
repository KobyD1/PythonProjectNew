class AlgoUtils:
    def __init__(self):
        pass


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
                    score_b = team_b_data['avg_diff'] + rate
                    score = score_b - team_a_data['avg_diff']
                    if score > 0:
                        favorite = "2"

                    else:
                        favorite = "1"
                        score = score * -1
                elif data["team_a"] == team_added:
                    score_a = team_a_data['avg_diff'] + rate
                    score = score_a - team_b_data['avg_diff']
                    if score > 0:
                        favorite = "1"
                    else :
                        favorite = "2"
                        score = score * -1
                    team_to_add,score_add = self.presentage_calculator(team_a_data, team_b_data,favorite)
                    if team_to_add ==favorite:
                        score =score+score_add
                        print (f"adding bonus {score_add} for presentage found ")
                print(f"****  Score found  , score = {score} ,favorite = {favorite} game = {data["team_a"]} VS{data["team_b"]}****")
                game = data["game"].split(" ")[2].replace(".", "").strip()
                plan = data["game"].split(" ")[0][1:2]

                result["game"] = game
                result["plan"] = plan
                result["favorite"] = favorite
                result["score"] = score
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
                        f" Under/Over results, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")

                if diff>0 :
                    result["favorite"]="1"
                else:
                    result["favorite"]="0"

                game = data["game"].split(" ")[2].replace(".", "").strip()
                plan = data["game"].split(" ")[0][1:2]

                result["game"] = game
                result["plan"] = plan
                return result

            case "2 Teams 3 points Under/Over":
             pass

    def presentage_calculator(self,team_a_data,team_b_data,favorite):
        score_add = (team_b_data['win_percentage'] - team_a_data['win_percentage']) / 10

        if team_b_data['win_percentage'] > team_a_data['win_percentage'] and favorite == "2":
            team_to_add = "2"

        elif team_b_data['win_percentage'] < team_a_data['win_percentage'] and favorite == "1":
            team_to_add = "1"
        return team_to_add,score_add










