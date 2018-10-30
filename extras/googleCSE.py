import operator
import pprint
from googleapiclient.discovery import build
import json
import extras.tools as tl
import parameters

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

# if __name__ == '__main__':
#     pprint.pprint(expand_by_google("Zika in Ecuador"))
