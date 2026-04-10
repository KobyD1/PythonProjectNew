

class utils106():

    def avg_calc(self,grades):
        len1 = len(grades)
        total = 0
        for grade in grades:
            total = total + grade

        avg = total / len1
        print(avg)
        return avg

    def print_start(self):
        print("start test ")

    def print_end(self):
        print ("Test End")

        #example of default value

    def print_text(self,text="Test Start"):
        print (text)
        # example of function with more than one parameter
    def avg_calc_by_nums(self,num1,num2,num4):
        summery = num1+num2 + num4
        avg= summery / 3
        return avg
