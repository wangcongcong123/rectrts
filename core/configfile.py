EXPANSION = True  # True or False
MODEL = "cosinetfidf"  # available so far: Jaccard, cosinetfidf,negativeKL
REL_THRESHOLD = 0.0
SUBMIT_FILE_NAME = "cosinetfidf-topics-expansion-online-all-withsocre"#"cosinetfidf-DIVtopid001-all-withsocre"
# QUERY_PATH = "dataset/TRECdataset/TREC2017-RTS-topics-final-expansion.json"
QUERY_PATH = "dataset/TRECdataset/TREC2017-RTS-topics-final-expansion.json"
DB_SRC="listenpool" #listenpool, status

MODE="online" #online, local