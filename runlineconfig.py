IS_EXECUTOR = True
IS_EVALUATE = True
TRESHOLD_EVAL = True
# The evluation  stops after splitting and not further for generating evaluation scores
STOP_BY_SPLIT = True
####
SIMULATION_TIME = 3000

if not IS_EXECUTOR:
    EVAL_A_SINGLE = False
    if EVAL_A_SINGLE:
        EVAL_A_SINGLE_FILE = "submission/cosinetfidf-Expansion-Run-T030"

    EVAL_A_BATCH = True
    if EVAL_A_BATCH:
        EVAL_A_SINGLE = False
        # EVAL_A_BATCH_FOLDER="dataset/TRECdataset/submissions/scenarioAF"
        EVAL_A_BATCH_FOLDER = "submission/ExpansionCosTFIDF"
        IS_THRESHOLD_EVAL = True

    EVAL_B_BATCH = False
    if EVAL_B_BATCH:
        EVAL_A_SINGLE = False
        EVAL_A_BATCH = False
        EVAL_B_BATCH_FOLDER = "dataset/TRECdataset/submissions/scenarioBF"
