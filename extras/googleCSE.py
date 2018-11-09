import operator
import pprint
import re

from googleapiclient.discovery import build
import json
import extras.tools as tl
import parameters
import requests
import bs4

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def expand_by_google_url(query):
    query_tokens = tl.textParse(query)
    contents = requests.get("https://www.google.com/search?q="+query).content
    soup2 = bs4.BeautifulSoup(contents,features="html.parser")
    returnlist=soup2.findAll("span", {"class": "st"})
    expansion_string=""
    for element in returnlist:
        expansion_string+=cleanhtml(str(element))+" "
    # print(expansion_string)
    expansion_tokens = tl.textParseWithFreq(expansion_string)
    sorted_expansion_tokens = sorted(expansion_tokens.items(), key=operator.itemgetter(1), reverse=True)
    # any candidate token with frequency larger than QUERY_EXPANSION_FRE_THRESHOLD(2 by default) is selected
    for expanded_token, fre in sorted_expansion_tokens:
        if not expanded_token.isnumeric():
            if fre >= parameters.QUERY_EXPANSION_FRE_THRESHOLD:
                if expanded_token not in query_tokens:
                    query_tokens.append(expanded_token)
    return query_tokens

def expand_by_google(query):
    # Top 10 google search result selected for query expansion
    service = build("customsearch", "v1",
                    developerKey="AIzaSyA0n2zmxqpK3Ac6s4QYgMa0HcoBw4RuB_o")
    res = service.cse().list(
        q=query,
        cx='005913137875547826480:0czjq6qque0',
        start=1,
        num=10
    ).execute()
    query_tokens = tl.textParse(query)
    returnitmes = res['items']
    expansion_string = ""
    for each in returnitmes:
        expansion_string += each['title'] + " "
        expansion_string += each['snippet'] + " "
    expansion_tokens = tl.textParseWithFreq(expansion_string)
    sorted_expansion_tokens = sorted(expansion_tokens.items(), key=operator.itemgetter(1), reverse=True)
    # any candidate token with frequency larger than QUERY_EXPANSION_FRE_THRESHOLD(2 by default) is selected
    for expanded_token, fre in sorted_expansion_tokens:
        if not expanded_token.isnumeric():
            if fre >= parameters.QUERY_EXPANSION_FRE_THRESHOLD:
                if expanded_token not in query_tokens:
                    query_tokens.append(expanded_token)
    return query_tokens

if __name__ == '__main__':
    print(expand_by_google_url("HPV vaccine side effects"))
    # pprint.pprint(expand_by_google())
