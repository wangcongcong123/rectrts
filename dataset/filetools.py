def write_to_log(loglabel,log):
    with open("log-"+loglabel+".txt", "a") as f:
        f.write(log)
    pass

def write_to_file(file,filecontent):
    with open(file, "w") as f:
        f.write(filecontent)
    pass