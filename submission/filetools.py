
import numpy as np

thresholds=np.arange(0, 0.92, 0.02)
# print(thresholds)
# thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

filenames_thre_dict={}
for each in thresholds:
    resultstr = ""
    # with open("Jaccard-No-Expansion-Run-all-withsocre", "r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         linecolumns = line.strip().split()
    #         if float(linecolumns[4]) > each:
    #             resultstr += linecolumns[0] + "\t" + linecolumns[1] + "\t" + linecolumns[2] + "\t" + linecolumns[
    #                 3] + "\n"
    filetowrite = "BasicJaccard/threshold-" + str(each).split(".")[0] + str(each).split(".")[1]
    filenames_thre_dict[filetowrite]=each
    #
    # with open(filetowrite, "w") as f1:
    #     f1.write(resultstr)
print(filenames_thre_dict)