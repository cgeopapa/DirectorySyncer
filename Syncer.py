import sys
from os import path
from os import listdir
import shutil

def main(args):
    A = args[0]
    B = args[1]
    src = listdir(args[0])

    while path.isdir(src):
        
        for dir in src:
            s = path.join(A, dir)
            d = path.join(B, dir)
            if not path.exists(d):
                if path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
            else:
                if s.__hash__() != d.__hash__():
                    if not path.isdir(s):
                        shutil.copy2(s, d)


if __name__ == "__main__":
    main(sys.argv[1:])
