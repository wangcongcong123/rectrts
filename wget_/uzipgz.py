import os
import gzip
import shutil
for root, dirs,files in os.walk("."):
    print(root)
    print(dirs)
    for each in files:
        if each.endswith('.gz'):
            with gzip.open(each, 'rb') as f_in:
                with open(each.split(".")[0], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)