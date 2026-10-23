total = 0

for i in range(0, 11):
    total = i * 4
    result = 12 / i
    print(total)

    if total == 12:
        print("the value is 12 ")
        continue
    if total > 10:
        print("the value is more than 10")

        break
    print(f"temp is {total}  ")

print("Test end")
