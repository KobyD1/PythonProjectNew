


class commision_calc_by_month():
    # the payment will be according month 9 - 5 $
    # other nonths 1 $
    #
    months = [1,4,5,7,11,9,6,9,10,9,9]
    payment = 0
    for month in months:
        if month ==9:
            payment +=5

        else:
            payment +=1

    print (f"total payment is {payment}")


class commision_calc_by_full_date():
    exp_month = "07"
    counter = 0
    dates=["10-11-2024","14-07-2024","18-09-2024","08-09-2024","03-09-24","12-01-24"]
    for date in dates:
        date_split = date.split("-")
        month = date_split[1]
        if month == exp_month:
            counter+=1

    if counter >2 :
        commision =0

    else:
        commision =5

    print (f"total commitment is {commision}")




