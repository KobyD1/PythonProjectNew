date = "28-Nov-2025"

index_1= date.index("-")
day_1 = date[:index_1]

index_2= len(date)-4
month= date[index_1+1:index_2]
final_date = f"{month}{day_1}-2025"
print(final_date)
