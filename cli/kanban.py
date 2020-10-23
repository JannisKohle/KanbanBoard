#!/usr/bin/python3

import os
import sys
import json

argv = sys.argv

# This function returns the content of ~/.config/kanban.json as a dict
def getConfig():
    if "kanban.json" in os.listdir(os.path.expanduser("~/.config")):
        with open(os.path.expanduser("~/.config/kanban.json"), "r+") as f:
            return json.load(f)
    else: # config file doesn't exist
        return "error"

##########

if argv[1] == "dir":
    if argv[2] == "set":
        if len(argv) == 4:
            path = argv[3]
            if "kanban.json" in os.path.expanduser("~/.config"): # config file already exists -> overwrite it
                with open(os.path.expanduser("~/.config/kanban.json"), "r+") as f:
                    content = json.load(f)
                    content["path"] = path
                    f.truncate(0)
                    json.dump(content, f)
            else: # config file doesn't exist
                os.system(f"touch {os.path.expanduser('~/.config/kanban.json')}")
                with open(os.path.expanduser("~/.config/kanban.json"), "r+") as f:
                    json.dump({"path": path, "opened": None}, f)

            print("Successfully set path to directory for storing boards.")
            exit()

        else:
            print("Invalid command")
            exit()

    elif argv[2] == "get":
        if len(argv) == 3:
            print(getConfig()["path"])
            exit()

        else:
            print("Invalid command")
            exit()

    else:
        print("Invalid command")
        exit()

elif argv[1] == "board": # TODO
    if argv[2] == "add":
        pass

    elif argv[2] == "delete":
        pass

    elif argv[2] == "rename":
        pass

    elif argv[2] == "list":
        pass

    elif argv[2] == "open":
        pass

    else:
        print("Invalid command")
        exit()

elif argv[1] == "label": # TODO
    pass

elif argv[1] == "column": # TODO
    pass

elif argv[1] == "task": # TODO
    pass

else:
    if len(argv) == 1:
        pass # get opened board

    else:
        print("Invalid command")
        exit()
