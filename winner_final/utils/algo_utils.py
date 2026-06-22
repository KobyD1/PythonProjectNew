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
                if avg_total - data["rate"] > 10:
                    result["score"] = avg_total - data["rate"] + 2  # bonus for high def
                    favorite = "Under"
                    print(
                        f"***** High Under found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")

                elif avg_total - data["rate"] < 10:
                    favorite = "Over"
                    result["score"] = avg_total - data["rate"] + 2  # bonus for high def
                    print(
                        f"***** High Over found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")
                else:
                    print(
                        f" Over found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")

                    result["score"] = avg_total - data["rate"]

                result["favorite"] = favorite
                result["score"] = result["score"]
                game = data["game"].split(" ")[2].replace(".", "").strip()
                plan = data["game"].split(" ")[0][1:2]

                result["game"] = game
                result["plan"] = plan
                return result

            case "2 Teams 3 points Under/Over":
             pass

        # default case

        # if data["description"]=="2 Teams Game Results":
        #     print(f"Calculate Game results {team_a_data} and {team_b_data}")
        #     if (data["team_b"])==data["team_with_added_points"]:
        #         score = team_a_data['avg_diff'] -data["rate"]
        #         favorite = "1"
        #
        #
        #     else:
        #         score = team_b_data['avg_diff'] -data["rate"]
        #         favorite = "2"
        #
        #     print(f"****  Score found  , score = {score} ,favorite = {favorite} game = {data["team_a"]} VS{data["team_b"]}****")

            # game = data["game"].split(" ")[2].replace(".", "").strip()
            # plan = data["game"].split(" ")[0][1:2]
            #
            # result["game"] = game
            # result["plan"] = plan
            # result["favorite"] = favorite
            # result["score"] = score
            # return result

        # elif data["description"]=="2 Teams Under/Over":
        #     print(f"Calculate Game results for under over {team_a_data} and {team_b_data}")
        #
        #     avg_total =(team_a_data['avg_total_points'] +team_b_data['avg_total_points'])/2
        #     if avg_total - data["rate"] >10 :
        #         result["score"] = avg_total - data["rate"]+2 # bonus for high def
        #         favorite = "Under"
        #         print( f"***** High Under found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")
        #
        #     elif avg_total - data["rate"] <10 :
        #         favorite = "Over"
        #         result["score"] = avg_total - data["rate"]+2 # bonus for high def
        #         print( f"***** High Over found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")
        #     else:
        #         print( f" Over found Under/Over, avg_total = {avg_total} ,rate = {data["rate"]} game = {data["team_a"]} VS{data["team_b"]}")
        #
        #         result["score"] = avg_total - data["rate"]
        #
        #     result["favorite"] = favorite
        #     result["score"] = result["score"]
        #     game = data["game"].split(" ")[2].replace(".", "").strip()
        #     plan = data["game"].split(" ")[0][1:2]
        #
        #     result["game"] = game
        #     result["plan"] = plan
        #     return result










