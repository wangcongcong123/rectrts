
JACCARD_THRSHOLD=0.3

def calcualteSim(queryTokens, tweetTokens):
    return len(set(queryTokens) & set(tweetTokens))/len(set(queryTokens) | set(tweetTokens))


# if __name__ == '__main__':
#     print(calcualteSim(["a","b","c"],["i"]))