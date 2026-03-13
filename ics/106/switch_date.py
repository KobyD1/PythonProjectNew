# Switch date with month by index:

date = "D08M03Y2026"

date_index_month = date.index("M")
date_index_year = date.index("Y")
get_current_day = date[:date_index_month]
get_current_month = date[date_index_month:date_index_year]
get_current_year = date[date_index_year:]

new_date = get_current_month+get_current_day+get_current_year
print(F'the new date is {new_date}')

# print(f'3. Original order: {date}\n   New order: {get_current_month}{get_current_day}{get_current_year}')