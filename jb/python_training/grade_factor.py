

grade = 60

if grade <50:
    grade = grade*1.1

elif (grade <80) and (grade >50):
    print ("the grade is between 50 and 80")

elif grade <= 100:
    grade = grade+20
    print ("the grade is more than 80 , the student get 20 points")


else:
    print (f"not valide grade define the value is {grade}")
