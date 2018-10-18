import json

with open("dataset/TREC2017-RTS-topics-final.json","r") as f:
    # print(f.read())
    content=f.read()
    # json.loads()
    js=json.loads(content)
    print(js[0]['narrative'])
    # print(js[0])