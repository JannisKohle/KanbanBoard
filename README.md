# KanbanBoard

This is a Command Line Interface for creating Kanban Boards. These Boards can have several columns
which can have several tasks. Tasks have some text and a label. Labels have a short text and
a color. I am writing this CLI in Python with the ```rich``` and ```argparse``` library.
I'm already planing a second version of this program, with which you can store Boards in the Cloud,
so that other people can contribute to it easily.

## Usage:

- Setup directory for storing notes: ```kanban dir --set "path"```
- Get directory for storing notes: ```kanban dir --get```

- Create a new Board: ```kanban board create --title "title of board"``` After using this command, the board will automatically be opened.
- Delete a Board: ```kanban board delete --id {idOfBoard}``` or ```kanban board delete --title "title of board"```
- Rename a Board: ```kanban board rename --id {idOfBoard} --new "new title of board"``` or ```kanban board rename --old "old title of board" --new "new title of board"```
- List all Boards: ```kanban board list```
- Open a Board: ```kanban board open --id {idOfBoard}``` or ```kanban board open --title "title of board"```
After opening a board, you can do stuff with it, e.g. add columns or tasks.


