run_path = "submissions/Jaccard-No-Expansion-Run-all-withsocre"
run_path_s = "submissions/Jaccard-No-Expansion-Run-all-withsocre-NT"

# with open(run_path,"r") as f:
#     lines=f.readlines()
#     alllist=[]
#     for line in lines:
#         topid=line.strip().split()[0]
#         alllist.append((int(topid[3:]),line))
#     salllist=sorted(alllist,key=lambda a:a[0])
#     import pprint
#     pprint.pprint(salllist)
#     for each in salllist:
#         with open(run_path_s,"a") as f1:
#             f1.write(each[1])

mystr=""
with open(run_path,"r") as f:
    lines=f.readlines()
    for line in lines:
        mystr+=line.strip().split()[0] + "\t" + line.strip().split()[1] + "\t" + line.strip().split()[2] + "\t" +line.strip().split()[3] + "\n"
with open(run_path_s, "a") as f1:
        f1.write(mystr)
