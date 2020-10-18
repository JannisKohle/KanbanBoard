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

    elif ergv[2] == "get":
        if len(argv) == 3:
            print(getConfig()["path"]
            exit()

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
