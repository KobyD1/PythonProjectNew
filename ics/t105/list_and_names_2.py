names = ["Leo Messi","Donald Trump","Shira Kamrad","Itamar_Cohen","Lial Morim"]

for name in names:
    print (name)
    if (name.count("_")==1):
        print (f"the {name} contains _")

    else:
        print (f"the name {name} did contains _ it contains space")
