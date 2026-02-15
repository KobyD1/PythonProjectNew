from kerem_qa.persons_oop.student import Student

student_1 = Student("John", "Doe1")
student_2 = Student("Mike", "Doe2")
student_3 = Student("Mike" )


avg1 = student_1.get_avarage_score([77,87,98,67,80])
avg2 = student_2.get_avarage_score([77,87,99,88,80,77,97])
student_1.get_avarage_score([56,88,66,45,99,80])  # example of using function without getting the return value
is_young1 = student_1.age_calculator(66)
is_young2 = student_1.age_calculator(77)
if avg1 > avg2:
    print("AVG 1 is higher than AVG2")

else:
    print("AVG 1 is lower than AVG2")


