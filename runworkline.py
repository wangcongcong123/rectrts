import runlineconfig
import os
import logging
import signal

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class TimeoutException(Exception):
    pass


def timeour_Handler(sugnum, frame):
    raise TimeoutException

signal.signal(signal.SIGALRM, timeour_Handler)


def evalThresholdABatch(files2evaldict):
    from submission import evaluateinbatch
    rts2017Mobileevalresult = evaluateinbatch.rts2017Mobileeval(files2evaldict)
    rts2017BatchAevalresult = evaluateinbatch.rts2017BatchAeval(files2evaldict)
    print(rts2017Mobileevalresult)
    print(rts2017BatchAevalresult)


def thesholdAEval(submitfile):
    from submission import filetools
    import numpy as np
    thresholds = np.arange(0.0, 0.92, 0.02)
    splitfoldername=submitfile.replace("-","")
    files2eval = filetools.splitbyT(splitfoldername, submitfile, thresholds=thresholds)
    logging.info("Submission file is split to sub files by thresholds : {0}".format(thresholds))
    if not runlineconfig.STOP_BY_SPLIT:
        evalThresholdABatch(files2eval)

def evalSubmitAFile(submitpath):
    from submission import evaluateinbatch
    evaluateinbatch.eval2017Mobile(submitpath)
    evaluateinbatch.eval2017BatchA(submitpath)

def evalSubmitsABatch(submitfolder):
    filestoeval=[]
    for root,dir,files in os.walk(submitfolder):
        for file in files:
            filestoeval.append(submitfolder+"/"+file)

    from submission import evaluateinbatch
    if not runlineconfig.IS_THRESHOLD_EVAL:
        return1= evaluateinbatch.eval2017MobileBatch(filestoeval)
        return2= evaluateinbatch.eval2017BatchABatch(filestoeval)
        print(return1)
        print(return2)
    else:
        files2evaldict={}
        for each in filestoeval:
            if not each.endswith(".DS_Store"):
                tem=each.split("-")[1]
                t=float(tem[0]+"."+tem[1:])
                files2evaldict[each]=t
        evalThresholdABatch(files2evaldict)

def evalSubmitsBBatch(submitfolder):
    filestoeval = []
    for root, dir, files in os.walk(submitfolder):
        for file in files:
            filestoeval.append(submitfolder + "/" + file)
    from submission import evaluateinbatch
    return1 = evaluateinbatch.eval2017BBatch(filestoeval)
    print(return1)


if __name__ == '__main__':
    if runlineconfig.IS_EXECUTOR:
        from core import executor
        from core import configfile
        submitpath = configfile.SUBMIT_FILE_NAME
        # thesholdAEval(submitpath)

        if os.path.exists("submission/" + submitpath):
            os.remove("submission/" + submitpath)
            logging.info("remove existed submission file: " + "submission/" + submitpath)
        for i in range(1):
            signal.alarm(runlineconfig.SIMULATION_TIME)
            try:
                executor.execute()
            except TimeoutException:
                continue
        logging.info("get submission file path: " + submitpath)
        if runlineconfig.TRESHOLD_EVAL:
            thesholdAEval(submitpath)
        else:
            evalSubmitAFile(submitpath)
    else:

        if runlineconfig.EVAL_A_SINGLE:
            logging.info("Start ScenarioA evaluating file: "+runlineconfig.EVAL_A_SINGLE_FILE)
            evalSubmitAFile(runlineconfig.EVAL_A_SINGLE_FILE)
        if runlineconfig.EVAL_A_BATCH:
            logging.info("Start ScenarioA evaluating all files in folder: "+runlineconfig.EVAL_A_BATCH_FOLDER)
            evalSubmitsABatch(runlineconfig.EVAL_A_BATCH_FOLDER)
        if runlineconfig.EVAL_B_BATCH:
            logging.info("Start ScenarioB evaluating all files in folder: " + runlineconfig.EVAL_B_BATCH_FOLDER)
            evalSubmitsBBatch(runlineconfig.EVAL_B_BATCH_FOLDER)

