

class utils106():

    def avg_calc(self,grades):
        len1 = len(grades)
        total = 0
        for grade in grades:
            total = total + grade

        avg = total / len1
        print(avg)
        # return avg

    def print_start(self):
        print("start test ")

    def print_end(self):
        print ("Test End")
