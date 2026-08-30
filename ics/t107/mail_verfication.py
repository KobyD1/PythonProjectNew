# to find the incorrect mail
# mail must contains @
mails = ["john@gmail.com", "sara.outlook.com", "david@domain.org","nike#sdsds.com"]

for mail in mails:
    print (mail)
    if mail.count("@") == 1:
        print ("valid mail found")
    if "@" in mail:
        print (f" valid mail found")
    else:
        print (f" invalid mail found")
