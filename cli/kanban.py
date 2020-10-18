import os
import sys
import json

argv = sys.argv

# This function returns the content of ~/.config/kanban.json as a dict
def getConfig():
    if "kanban.json" in os.path.expanduser("~/.config"):
        with open(os.path.expanduser("~/.config/kanban.json"), "r+") as f:
            return json.load(f)
    else: # config file doesn't exist
        return 1

##########

if argv[1] == "dir":
    if argv[2] == "set":
        if len(argv) == 4:
            pass

        else:
            print("Invalid command")
            exit()

    elif ergv[2] == "get":
        if len(argv) == 3:
            pass

        else:
            print("Invalid command")
            exit()

    else:
        print("Invalid command")
        exit()

elif argv[1] == "board":
    pass

elif argv[1] == "label":
    pass

elif argv[1] == "column":
    pass

elif argv[1] == "task":
    pass

else:
    print("Invalid command")
    exit()
