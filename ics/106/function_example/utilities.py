


class Utilities():


    def calc_evg(self,grades):

        summery = 0
        i= len(grades)

        for grade in grades:
            summery += grade

        avg = summery / i

        print (f"the avg value is {avg}")