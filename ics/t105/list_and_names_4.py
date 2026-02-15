names = ["Mr. John", "Mr. Tal","Miss Lelel","Miss Almog","Mr. Dany"]

for name in names :
    print (name)
    if (name.__contains__("Mr")):
        print (f"Male Found the name is {name}")
    else:
        print (f"Female Found the name is {name}")


