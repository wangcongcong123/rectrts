import json
from extras import tools as tl
from extras import googleCSE as gcse

#   with open("dataset/TRECdataset/TREC2017-RTS-topics-final-expansion.json") as f:
def loadprofiles(filepath):
    with open(filepath) as f:
        loaded_profiles = json.load(f)
    return loaded_profiles

def expandQuery(profile):
    profile_title = profile['title']
    query_title_expanded_by_google = gcse.expand_by_google_url(profile_title)
    profile_desc = profile['description']
    query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
    return query_expaned_tokens

def convertwithexpansion(src, des):
    count = 0
    profiles = loadprofiles(src)
    for profile in profiles:
        print("Process expansion...:", count)
        profile["expansion"] = expandQuery(profile)
        count += 1
    import json
    with open(des, 'w') as fout:
        json.dump(profiles, fout)
if __name__ == '__main__':
    convertwithexpansion("/Users/wangcongcong/PycharmProjects/rtsFlask/rts/ajax/static/TREC-DIY-Topics.json","../dataset/TREC-DIY-Topics-Expansion.json")