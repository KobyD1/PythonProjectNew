from kerem_qa.persons_oop.person import Person


class Student(Person):

    def __init__(self, first_name, last_name="Doe"):
        self.first_name = first_name
        self.last_name = last_name

    def get_avarage_score(self,grades):
        sum  = 0
        for grade in grades:
            sum= sum+grade

        avg = sum / len(grades)
        print (F"The average score is {avg}")
        return avg

    def compare_score(self,avg1,avg2):
        if avg1>avg2:
            print ("AVG 1 is higher than AVG2")

        else:
            print ("AVG 1 is lower than AVG2")
