#!/usr/bin/python3

import os
import sys
import json
import random

argv = sys.argv

# This function returns the content of ~/.config/kanban.json as a dict
def getConfig():
    if "kanban.json" in os.listdir(os.path.expanduser("~/.config")):
        with open(os.path.expanduser("~/.config/kanban.json"), "r+") as f:
            return json.load(f)
    else:  # config file doesn't exist
        return "error"

# This function creates a new, unique id
def generateId():
    used = listBoards()  # all used ids
    while True:
        new = random.randint(100, 999)
        if new not in used:
            return new

##########

def listBoards():
    return [id for id in os.listdir(os.path.expanduser(getConfig()["path"]+"/boards")) if not id.startswith(".")]

def listLabels():
    return os.listdir(os.path.expanduser(getConfig()["path"]+"/labels"))

##########

if argv[1] == "dir":
    if argv[2] == "set":
        if len(argv) == 4:
            path = argv[3]
            # config file already exists -> overwrite it
            if "kanban.json" in os.path.expanduser("~/.config"):
                with open(os.path.expanduser("~/.config/kanban.json"), "r+") as f:
                    content = json.load(f)
                    content["path"] = path
                    f.truncate(0)
                    json.dump(content, f)
            else:  # config file doesn't exist
                os.system(f"touch ~/.config/kanban.json")
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

elif argv[1] == "board":  # TODO
    if argv[2] == "add":
        if len(argv) == 5 and argv[3] == "--title":
            title = argv[4]
            id = generateId()
            os.system(f"mkdir {getConfig()["path"]}/boards/{id}") # create directory

            os.system(f"touch {getConfig()["path"]}/boards/{id}/.info.json") # create info file
            with open(f"{os.path.expanduser(getConfig()["path"])}/boards/{id}/.info.json", "r+") as f: # write info file
                content = {"id": id, "title": title}
                json.dump(content, f)

        else:
            print("Invalid command")
            exit()

    elif argv[2] == "delete":
        if len(argv) == 5:
            if argv[3] == "--id":
                if argv[4] in listBoards():
                    with open(f"{os.path.expanduser(getConfig()["path"])}/boards/{argv[4]}/.info.json", "r+") as f:
                        title = json.load(f)["title"]
                    if input(f"Delete board {title}? (y/n) ") == "y":
                        os.system(f"rm -r {getConfig()["path"]}/boards/{argv[4]}")
                    exit()

                else:
                    print(f"Board #{argv[4]} does not exist.")
                    exit()

            elif argv[3] == "--title":
                for id in listBoards():
                    with open(f"", "r+") as f:
                        title = json.load(f)["title"]
                    if title == argv[4]:
                        if input(f"Delete board {argv[4]}? (y/n) ") == "y":
                            os.system(f"rm -r {getConfig()["path"]}/boards/{id}")
                        exit()

                print(f"Board {argv[4]} does not exist.")
                exit()

            else:
                print("Invalid command")
                exit()

        else:
            print("Invalid command")
            exit()

    elif argv[2] == "rename":
        pass

    elif argv[2] == "list":
        pass

    elif argv[2] == "open":
        pass

    else:
        print("Invalid command")
        exit()

elif argv[1] == "label":  # TODO
    pass

elif argv[1] == "column":  # TODO
    pass

elif argv[1] == "task":  # TODO
    pass

else:
    if len(argv) == 1:
        pass  # get opened board

    else:
        print("Invalid command")
        exit()
