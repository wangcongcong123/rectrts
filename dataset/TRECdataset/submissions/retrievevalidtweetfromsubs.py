scenarioAsubsnames=[]
scenarioBsubsnames=[]

with open("scenarioA-sub-names","r") as f:
    scenarioAsubsnames=[each.strip().split(".")[0] for each in f.readlines()]
with open("scenarioB-sub-names", "r") as f:
    scenarioBsubsnames = [each.strip().split(".")[0] for each in f.readlines()]


scenariosubsnames=scenarioAsubsnames+scenarioBsubsnames

allAids=[]

for each in scenarioAsubsnames:
    filename_="scenarioA/"+each
    with open(filename_,"r") as f:
        allAids+=[push.strip().split()[1] for push in f.readlines()]
print(len(set(allAids)))
allBids=[]
for each in scenarioBsubsnames:
    filename_="scenarioB/"+each
    with open(filename_,"r") as f:
        allBids+=[push.strip().split()[3] for push in f.readlines()]

print(len(set(allBids)))
allids=allAids+allBids
idsset=set(allids)

# print(len(idsset))
# print(idsset.)

newidset=set()

import simpledbtools as sdbt
idsindb=sdbt.getAll2017Ids()
dbidsdict=dict.fromkeys(idsindb,0)
for eachid in idsset:
    if eachid not in dbidsdict:
        newidset.add(eachid)

writetofilestr=""
print(len(newidset))#the total length of unique tweets in all submissions are 547117 (excluding those in db)
for each in newidset:
    writetofilestr+=each+"\n"
with open("unqiue-submissions-tweetids-collection","w") as f:
    f.write(writetofilestr)

