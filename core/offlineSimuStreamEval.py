import operator

from extras import profilehandler as ph
from extras import tools as tl
from core.local_listener import LocalListener
from extras import googleCSE as gcse
import pprint

ll = LocalListener()
profiles2017 = ph.get2017Profiles()

terminator=0
profileIDs=[]
profileQuerys=[]
for profile in profiles2017:
    if terminator == 10:
        break
    terminator+=1
    # query expansion
    profile_title = profile['title']
    query_title_expanded_by_google = gcse.expand_by_google_url(profile_title)
    profile_desc = profile['description']
    query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
    topicid=profile['topid']
    profileIDs.append(topicid)
    profileQuerys.append((topicid,query_expaned_tokens))
# print(profileIDs)
print("Jaccard Similarity:")
from models import jaccardModel
tweetsSteamBatch = ll.get_status_by_topiclist(profileIDs)
print(len(tweetsSteamBatch))
    # get all test set of tweets of the current topic
    # tweetsSteamBatch = ll.get_status_by_topic(profile['topid'])
push_dict={}
for tweetstream in tweetsSteamBatch:
    tweettokens = tl.textParse(tweetstream[1])
    for profileQuery in profileQuerys:
        simscore = jaccardModel.calcualteSim(profileQuery[1],tweettokens)
        if simscore>jaccardModel.JACCARD_THRSHOLD:
            if profileQuery[0] in push_dict:
                push_dict[profileQuery[0]].append((tweetstream[0],simscore,tweetstream[3],tweetstream[2]))
            else:
                push_dict[profileQuery[0]]=[(tweetstream[0],simscore,tweetstream[3],tweetstream[2])]

# total_pushed=0
# relevant_pushed=0
#only push top 10 (a simulation for TREC RTS)
# pushed_tweet_list = sorted(pushed_tweet_list, key=operator.itemgetter(1), reverse=True)
# pushed_tweet_list = pushed_tweet_list if len(pushed_tweet_list)<10 else pushed_tweet_list[:10]
# total_pushed+=len(pushed_tweet_list)
# for tw in pushed_tweet_list:
#     if tw[2]>0:
#         relevant_pushed+=1
# push_dict[profile['topid']] = pushed_tweet_list
# print(profile['topid'],":")
# pprint.pprint(pushed_tweet_list)
pprint.pprint(push_dict)
# print("Jaccard (query expansion with Google, based on Jacarrd Similarity) Precison is: ",relevant_pushed/total_pushed)
print("------------------------------------------------------------")
from models import cosinetfidf as cti
tweets_collection = ll.get_topn_status(1000)
all_tweets_batch = list(tweets_collection)
cti.computeIDFByDocs(all_tweets_batch)
print("TF-IDF Cosine Similarity:")
tweetsSteamBatch = ll.get_status_by_topiclist(profileIDs)
push_dict={}
for tweetstream in tweetsSteamBatch:
    tweettokens = tl.textParse(tweetstream[1])
    tweetvector = cti.getDFIDFVector(tweettokens)
    for profileQuery in profileQuerys:
        profile_vector=cti.getDFIDFVector(profileQuery[1])
        simscore = cti.get_cosine(profile_vector, tweetvector)
        if simscore>cti.SIM_THRESHOLD:
            if profileQuery[0] in push_dict:
                push_dict[profileQuery[0]].append((tweetstream[0],simscore,tweetstream[3],tweetstream[2]))
            else:
                push_dict[profileQuery[0]]=[(tweetstream[0],simscore,tweetstream[3],tweetstream[2])]
# total_pushed=0
# relevant_pushed=0
#only push top 10 (a simulation for TREC RTS)
# pushed_tweet_list = sorted(pushed_tweet_list, key=operator.itemgetter(1), reverse=True)
# pushed_tweet_list = pushed_tweet_list if len(pushed_tweet_list)<10 else pushed_tweet_list[:10]
# total_pushed+=len(pushed_tweet_list)
# for tw in pushed_tweet_list:
#     if tw[2]>0:
#         relevant_pushed+=1
# push_dict[profile['topid']] = pushed_tweet_list
# print(profile['topid'],":")
# pprint.pprint(pushed_tweet_list)
pprint.pprint(push_dict)
# print("Jaccard (query expansion with Google, based on Jacarrd Similarity) Precison is: ",relevant_pushed/total_pushed)

