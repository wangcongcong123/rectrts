import operator

from extras import profilehandler as ph
from extras import tools as tl
from core.local_listener import LocalListener
from extras import googleCSE as gcse
import pprint

ll = LocalListener()
profiles2017 = ph.get2017Profiles()

print("Jaccard Similarity:")
from models import jaccardModel
push_dict={}
terminator=0
total_pushed=0
relevant_pushed=0
for profile in profiles2017:
    if terminator == 10:
        break
    terminator+=1
    # query expansion
    profile_title = profile['title']
    query_title_expanded_by_google = gcse.expand_by_google_url(profile_title)
    profile_desc = profile['description']
    query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
    # get all test set of tweets of the current topic
    tweetsSteamBatch = ll.get_status_by_topic(profile['topid'])
    pushed_tweet_list=[]
    for tweetstream in tweetsSteamBatch:
        tweettokens = tl.textParse(tweetstream[1])
        simscore = jaccardModel.calcualteSim(query_expaned_tokens,tweettokens)
        if simscore>jaccardModel.JACCARD_THRSHOLD:
            pushed_tweet_list.append((tweetstream[0],simscore,tweetstream[3]))
    #only push top 10 (a simulation for TREC RTS)
    pushed_tweet_list = sorted(pushed_tweet_list, key=operator.itemgetter(1), reverse=True)
    pushed_tweet_list = pushed_tweet_list if len(pushed_tweet_list)<10 else pushed_tweet_list[:10]
    total_pushed+=len(pushed_tweet_list)
    for tw in pushed_tweet_list:
        if tw[2]>0:
            relevant_pushed+=1
    push_dict[profile['topid']] = pushed_tweet_list
    print(profile['topid'],":")
    pprint.pprint(pushed_tweet_list)
# pprint.pprint(push_dict)
print("Jaccard (query expansion with Google, based on Jacarrd Similarity) Precison is: ",relevant_pushed/total_pushed)

print("------------------------------------------------------------")
from models import cosinetfidf as cti
tweets_collection = ll.get_topn_status(1000)
all_tweets_batch = list(tweets_collection)
cti.computeIDFByDocs(all_tweets_batch)

push_dict={}
terminator=0
total_pushed=0
relevant_pushed=0

for profile in profiles2017:
    if terminator == 10:
        break
    terminator+=1
    # query expansion
    profile_title = profile['title']
    query_title_expanded_by_google = gcse.expand_by_google_url(profile_title)
    profile_desc = profile['description']
    query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
    # query_expaned_tokens =  tl.textParse(profile_desc)
    # get profile vector
    profile_vector = cti.getDFIDFVector(query_expaned_tokens)
    # get all test set of tweets of the current topic
    tweetsSteamBatch = ll.get_status_by_topic(profile['topid'])
    pushed_tweet_list=[]
    for tweetstream in tweetsSteamBatch:
        tweettokens = tl.textParse(tweetstream[1])
        tweetvector = cti.getDFIDFVector(tweettokens)
        simscore = cti.get_cosine(profile_vector, tweetvector)
        if simscore>cti.SIM_THRESHOLD:
            pushed_tweet_list.append((tweetstream[0],simscore,tweetstream[3]))

    #only push top 10 (a simulation for TREC RTS)
    pushed_tweet_list = sorted(pushed_tweet_list, key=operator.itemgetter(1), reverse=True)
    pushed_tweet_list = pushed_tweet_list if len(pushed_tweet_list)<10 else pushed_tweet_list[:10]
    total_pushed+=len(pushed_tweet_list)
    for tw in pushed_tweet_list:
        if tw[2]>0:
            relevant_pushed+=1
    push_dict[profile['topid']] = pushed_tweet_list
    print(profile['topid'],":")
    pprint.pprint(pushed_tweet_list)
# pprint.pprint(push_dict)
print("TF-IDF cosine (query expansion with Google, IDF based on top 1000 tweets) Precison is: ",relevant_pushed/total_pushed)
        # print("The consine similarity between profile ", profile['topid'], "(", profile_title, ") and ",
        #       tweetstream[0], "(", tweetstream[1], "): ")
        # print("based on TF-IDF: ", simscore)
        # print("labelled: ", tweetstream[3])
        # print(query_expaned_tokens)
