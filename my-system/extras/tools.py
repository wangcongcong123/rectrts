
from nltk.stem import PorterStemmer
import nltk

stopwords=[]
with open("extras/stopwords","r") as f:
    stopwords=f.read().split("\n")

#initial filtering for tweet
#tweets length should >= 3
#tweets with Reweet symbol are removed

def isvalidTeet(tweet):
    if "@RT" in tweet:
        return False
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
    tokens=[]
    for token in listofTokens:
        if token not in stopwords:
            token=stemmer.stem(token)
            tokens.append(token.lower())
    return tokens

def test():
    print("testing in tools")

# def loadStopwords
