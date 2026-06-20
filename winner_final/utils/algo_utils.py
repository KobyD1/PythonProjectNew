class AlgoUtils:
    def __init__(self):
        pass


    def under_over_algo(self,team_a,team_b,ref):
        print(f" Calculate Under Over for {team_a} and {team_b} with {ref}")

    def calculate_game_basketball_algo(self,team_a_data,team_b_data,data):
        print(f"Calculate Game results {team_a_data} and {team_b_data}")
        if (data["team_b"])==data["team_with_added_points"]:
            ref_final = team_a_data['avg_diff'] -data["rate"]
            favorite = data["team_a"]


        else:
            ref_final = team_b_data['avg_diff'] -data["rate"]
            favorite = data["team_b"]
        if ref_final>10:
            print (f"**** High Score found favorite is {favorite} , grade = {ref_final} ****")

        else:
            print (f"**** Typical  Score found favorite is {favorite} , grade = {ref_final} ****")






