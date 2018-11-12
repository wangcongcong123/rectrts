def write_to_log(loglabel,log):
    with open("log-"+loglabel+".txt", "a") as f:
        f.write(log)
    pass