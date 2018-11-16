# mobile[1], tweets2dayepoch[2], bathqrels[0]
batch1_id_dict={}

comp1="TRECdataset/rts2017-mobile-qrels.txt"
comp2="TRECdataset/rts2017-batch-qrels.txt"

with open(comp1,"r") as f1:
    lines=f1.readlines()
    for line in lines:
        batch1_id_dict[line.strip().split()[1]]=0
print("Unique IDs IN",comp1,":",len(batch1_id_dict))

batch2_id_dict={}
with open(comp2,"r") as f2:
    lines=f2.readlines()
    count=0
    for line in lines:
        id=line.strip().split()[2]
        if id not in batch1_id_dict:
            count+=1
            # print(id)
        batch2_id_dict[id]=0
print("Unique IDs IN",comp2,":",len(batch2_id_dict))
print("Different IDs Between",comp1,"and",comp1,":",count)

# 1483 tweets are in rts2017-batch-qrels.txt but not in rts2017-batch-tweets2dayepoch.txt
# no tweets in rts2017-batch-tweets2dayepoch.txt are not in rts2017-batch-qrels.txt

# 68037 tweets are in rts2017-batch-tweets2dayepoch.txt but not in rts2017-mobile-qrels.txt
# 40313 tweets are in rts2017-mobile-qrels.txt but are not in rts2017-batch-tweets2dayepoch.txt

# 40313 tweets are in rts2017-batch-qrels.txt but not in rts2017-mobile-qrels.txt
# 71133 tweets are in rts2017-mobile-qrels.txt but are not in rts2017-batch-qrels.txt
#
# dic_count={}
# with open("TRECDATASET/rts2017-batch-tweets2dayepoch.txt","r") as f:
#     lines=f.readlines()
#     for each in lines:
#         dic_count[each.strip().split()[0]]=0
# print(len(dic_count))
  #we checked here and found no repeated tweets are in the file rts2017-batch-tweets2dayepoch.txt
