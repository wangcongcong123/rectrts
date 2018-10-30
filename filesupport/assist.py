with open("stopwordlist1","r") as f:
    list=f.read().split("\n\n")
    str=""
    for each in list:
        if len(each)>2:
            str+=each+"\n"
    with open("stopwordlist1_","w") as f:
        f.write(str)