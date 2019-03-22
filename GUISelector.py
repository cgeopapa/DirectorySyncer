from Syncer import Sync
import sys
import easygui


def main(args):
    d = easygui.diropenbox("Select a Directory to Sync", "Directory to Sync", args[0])
    Sync(args[0], d)


if __name__ == "__main__":
    main(sys.argv[1:])
