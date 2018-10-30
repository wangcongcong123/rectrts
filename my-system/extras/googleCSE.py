import pprint
from googleapiclient.discovery import build
import json

def expand_by_google(query):
    service = build("customsearch", "v1",
                    developerKey="AIzaSyA0n2zmxqpK3Ac6s4QYgMa0HcoBw4RuB_o")
    res = service.cse().list(
        q=query,
        cx='005913137875547826480:0czjq6qque0',
        start=1,
        num=10
    ).execute()
    with open(query + ".json", "w") as f:
        f.write(json.dumps(res))
    pprint.pprint(res)

#
# if __name__ == '__main__':
#     expand_by_google("UCD")