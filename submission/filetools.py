import numpy as np

def splitbyT(folder,subfile,thresholds=[0]):
    createFolder("./submission/"+folder)
    filenames_thre_dict = {}
    for each in thresholds:
        resultstr = ""
        with open("submission/"+subfile, "r") as f:
            lines = f.readlines()
            for line in lines:
                linecolumns = line.strip().split()
                if float(linecolumns[4]) > each:
                    resultstr += linecolumns[0] + "\t" + linecolumns[1] + "\t" + linecolumns[2] + "\t" + linecolumns[
                        3] + "\n"
        each = "{0:.2f}".format(each)
        filetowrite = "submission/"+folder+"/threshold-" + str(each).replace(".", "")
        filenames_thre_dict[filetowrite] = each
        with open(filetowrite, "w") as f1:
            f1.write(resultstr)
    return filenames_thre_dict

def subsort(run_path_, run_path_s_):
    run_path = run_path_
    run_path_s = run_path_s_
    with open(run_path, "r") as f:
        lines = f.readlines()
        alllist = []
        limit_count = dict()
        for line in lines:
            topid = line.strip().split()[0]
            date = line.strip().split()[2]
            id = topid + date[0:4]
            if id not in limit_count:
                limit_count[id] = 0
            else:
                limit_count[id] += 1
            if limit_count[id] < 10:
                alllist.append((int(topid[3:]), line))
        salllist = sorted(alllist, key=lambda a: a[0])
        for each in salllist:
            with open(run_path_s, "a") as f1:
                f1.write(each[1])
def createFolder(folder):
    import os
    if not os.path.exists(folder):
        os.makedirs(folder)



if __name__ == '__main__':
    # createFolder("name")
    pass
    # file_thre_dict = {'ExpansionCosTFIDF/threshold-030': '0.30', 'ExpansionCosTFIDF/threshold-032': '0.32',
    #                   'ExpansionCosTFIDF/threshold-034': '0.34', 'ExpansionCosTFIDF/threshold-036': '0.36',
    #                   'ExpansionCosTFIDF/threshold-038': '0.38', 'ExpansionCosTFIDF/threshold-040': '0.40',
    #                   'ExpansionCosTFIDF/threshold-042': '0.42', 'ExpansionCosTFIDF/threshold-044': '0.44',
    #                   'ExpansionCosTFIDF/threshold-046': '0.46', 'ExpansionCosTFIDF/threshold-048': '0.48',
    #                   'ExpansionCosTFIDF/threshold-050': '0.50', 'ExpansionCosTFIDF/threshold-052': '0.52',
    #                   'ExpansionCosTFIDF/threshold-054': '0.54', 'ExpansionCosTFIDF/threshold-056': '0.56',
    #                   'ExpansionCosTFIDF/threshold-058': '0.58', 'ExpansionCosTFIDF/threshold-060': '0.60',
    #                   'ExpansionCosTFIDF/threshold-062': '0.62', 'ExpansionCosTFIDF/threshold-064': '0.64',
    #                   'ExpansionCosTFIDF/threshold-066': '0.66', 'ExpansionCosTFIDF/threshold-068': '0.68',
    #                   'ExpansionCosTFIDF/threshold-070': '0.70', 'ExpansionCosTFIDF/threshold-072': '0.72',
    #                   'ExpansionCosTFIDF/threshold-074': '0.74', 'ExpansionCosTFIDF/threshold-076': '0.76',
    #                   'ExpansionCosTFIDF/threshold-078': '0.78', 'ExpansionCosTFIDF/threshold-080': '0.80',
    #                   'ExpansionCosTFIDF/threshold-082': '0.82', 'ExpansionCosTFIDF/threshold-084': '0.84',
    #                   'ExpansionCosTFIDF/threshold-086': '0.86', 'ExpansionCosTFIDF/threshold-088': '0.88',
    #                   'ExpansionCosTFIDF/threshold-090': '0.90'}
    # newfiledict={}
    # for k,v in file_thre_dict.items():
    #     subsort(k,k+"-s")
    #     newfiledict[k+"-s"]=v
    # print(newfiledict)
