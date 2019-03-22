from os import path
from os import listdir
import shutil

def Sync(src, dir):
    lst = listdir(src)
    for file in lst:
        s = path.join(src, file)
        d = path.join(dir, file)
        if not path.exists(d):
            if path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        elif path.isdir(s):
            Sync(s, d)
        else:
            if s.__hash__() != d.__hash__():
                if not path.isdir(s):
                    shutil.copy2(s, d)