import json

def get2017Profiles():
    with open("../dataset/TRECdataset/TREC2017-RTS-topics-final.json") as f:
        profiles = json.load(f)
    return profiles

def get2016Profiles():
    with open("../dataset/TRECdataset/TREC2016-RTS-topics.json") as f:
        profiles1 = json.load(f)
    with open("../dataset/TRECdataset/TREC2015-MB-noeval-topics-culled.json") as f:
        profiles2 = json.load(f)
    with open("../dataset/TRECdataset/TREC2015-MB-eval-topics.json") as f:
        profiles3 = json.load(f)
    return profiles1+profiles2+profiles3

def getAllProfiles():
    return get2017Profiles()+get2016Profiles()

# if __name__ == '__main__':
#     profiles = getAllProfiles()
#     print(len(profiles))
