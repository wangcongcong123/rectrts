from nltk.stem import PorterStemmer
import nltk

stopwords=[]
with open("../filesupport/stopwordlist1","r") as f:
    stopwords=f.read().split("\n")

#initial filtering for tweet
#tweets length should >= 3
#tweets with Reweet symbol are removed

def isvalidTeet(tweet):
    # if "@RT" in tweet:
    #     return False
    tokens=tweet.split()
    if len(tokens)<3:
        return False
    return True

#tokenize a string
#URL, Hashtags, Stopwords, Stemming, Lemmatization
def textParse(bigString):
    import re
    stemmer=PorterStemmer()
    listofTokens=re.split(r"\W+",bigString)
    # listofTokens = re.split(r"([a-zA-Z]+)", bigString)
    tokens=[]
    # "congcong123".isalpha() return False
    for token in listofTokens:
        if len(token)>2:
            token=token.lower()
            if token not in stopwords:
                token=stemmer.stem(token)
                tokens.append(token)
    return tokens

#tokenize a string and calculate term frequency
def textParseWithFreq(bigString):
    tokens=textParse(bigString)
    freqdict={}
    for each in tokens:
        if each in freqdict:
            freqdict[each]+=1
        else:
            freqdict[each]=0
    return freqdict
#
# if __name__ == '__main__':
#     print()