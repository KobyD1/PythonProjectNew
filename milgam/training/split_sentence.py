text = "Hi ,  my name is John I live in London"

text_new = text.replace("London", "Rome")
print(text_new)
index = text_new.index("in")
city = text [index+3:]
prefix = text[:index]
full_text= prefix+ " Rome"
full_text_2 = f"{prefix} Rome"

print ("end")