

def avg_calc(grades):

    len1 = len(grades)
    total = 0
    for grade in grades:
        total = total + grade

    avg = total/len1
    print (avg)

def  print_start():
    print ("start test ")




class avg_calc_by_function_1:
    print_start()

    grades_1 = [60,45,36,89,78,90]
    grades_2 = [55,453,136,859,768,90]

    grades_1.append(555)
    avg_calc(grades_1)
    avg_calc(grades_2)


