with open("rts2017-mobile-qrels.txt","r") as f:
    lines=f.readlines()
    strtowrtie=""
    tweetdict={}
    for line in lines:
        linecols=line.strip().split()
        if linecols[1] not in tweetdict:
            tweetdict[linecols[1]]=0
            strtowrtie+=linecols[1]+"\t"+"20170728"+"\t"+ "1501481401"+"\n"


# strtowrtie=""
# with open("rts2017-batch-tweets2dayepoch.txt","r") as f:
#     lines = f.readlines()
#     for line in lines:
#         linecols = line.strip().split()
#         if linecols[1] not in tweetdict:
#             strtowrtie+=line

with open("rts2017-mobile-tweets2dayepoch.txt","a") as f:
    f.write(strtowrtie)