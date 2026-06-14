

full_name = "Leo Messi"

index = full_name.index(" ")
first_name = full_name[:index]
last_name = full_name[index+1:]

if len(first_name)<len(last_name):
    full_name = last_name + " " + first_name

print (full_name)
