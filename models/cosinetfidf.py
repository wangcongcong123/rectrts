__author__ = 'congcong'

import math
from collections import Counter
from extras import tools as tl
idf_dict = {}
max = 1

def getDFIDFVector(tokens):
    vector_dict={}
    words_counted = Counter(tokens)
    unique_words = list(words_counted.keys())
    for each in unique_words:
        idf = max if each not in idf_dict else idf_dict[each]
        wd_tf_idf = words_counted[each] * idf
        vector_dict[each]=wd_tf_idf
    return vector_dict

# Computes TF for words in each doc, DF for all features in all docs; finally whole IDF dict
def computeIDFByDocs(tweet_batch_withid):
    all_words = []  # list to collect all unique words in each tweet id pairs
    counts_dict = {}  # dict to collect doc data, word-counts and word-lists
    for tweet_withid in tweet_batch_withid:
        tweetid = tweet_withid[0]
        tweet = tweet_withid[1]
        tokens = tl.textParse(tweet)
        words_counted = Counter(tokens)  # counts words in a doc
        unique_words = list(words_counted.keys())  # list of the unique words in the doc
        counts_dict[tweetid] = words_counted  # make dict entry {'d1' : {'a': 1, 'b':6}}
        all_words = all_words + unique_words  # collect all unique words from each doc; bit hacky
    n = len(counts_dict)  # number of documents is no of entries in dict
    df_counts = Counter(all_words)  # DF of all unique words from each doc, counted
    global max
    global idf_dict
    for word in all_words:
        idf=math.log(n / df_counts[word], 10)
        idf_dict[word] = idf
        if idf > max:
            max=idf

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    # NB strictly, this is not really correct, needs vector of all features with zeros
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return round(float(numerator) / denominator, 3)
