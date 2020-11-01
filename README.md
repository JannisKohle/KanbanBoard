# KanbanBoard

This is a Command Line Interface for creating Kanban Boards. These Boards can have several columns
which can have several tasks. Tasks have some text and a label. Labels have a short text and
a color. I am writing this CLI in Python with the ```rich``` and ```argparse``` library.
I'm already planing a second version of this program, with which you can store Boards in the Cloud,
so that other people can contribute to it easily.

## Usage:

- Setup directory for storing notes: ```kanban dir set "path/to/directory"```
- Get directory for storing notes: ```kanban dir get```

----------

- Create a new Board: ```kanban board add --title "title of board"``` After using this command, the board will automatically be opened.
- Delete a Board: ```kanban board delete --id {idOfBoard}``` or ```kanban board delete --title "title of board"```
- Rename a Board: ```kanban board rename --id {idOfBoard} --new "new title of board"``` or ```kanban board rename --old "old title of board" --new "new title of board"```
- List all Boards: ```kanban board list```
- Open a Board: ```kanban board open --id {idOfBoard}``` or ```kanban board open --title "title of board"```
After opening a board, you can do stuff with it, e.g. add columns or tasks.
- Get currently opened board: ```kanban```
- Show graphical version of currently opened board: ```kanban show``` or ```kanban board show --id {idOfBoard}``` or ```kanban board show --title "title of board"```

----------

- Create a label: ```kanban label add --name "name of label" --color "color of label (in hex)"``` *A color is not necessary, but useful*
- Delete a label: ```kanban label delete --name "name of label"```
- Rename a label: ```kanban label rename --old "old name of label" --new "new name of label"```
- (Re-)color a label: ```kanban label color --name "name of label" --color "color of label (in hex)```
- List all labels: ```kanban label list```

----------

**You have to open a board before using the following commands:**

- Add a column to currently opened board: ```kanban column add --title "title of column"```
- Delete a cloumn: ```kanban column delete --title "title of column"```
- Rename a column: ```kanban column rename --old "old title of column" --new "new title of column"```
- List all columns: ```kanban column list```

----------

- Add a task to specific column: ```kanban task add --text "text of task" --column "title of column" --label "name of label"``` *A label is not necessary, but useful*
- Add a task to first column: ```kanban task add --text "text of task" --label "name of label"```
- Delete a task: ```kanban task delete --text "text of task"```
- Rename a task: ```kanban task rename --old "old text of task" --new "new text of taks"```
- Move a task to a different column: ```kanban task move --text "text of task" --column "title of column"```
- List all tasks: ```kanban task list```
- List all tasks in a specific column: ```kanban task list --column "title of column"```
- List all tasks with a specific label: ```kanban label list --label "name of label"```
- Add a label to a task: ```kanban task label --text "text of task" --label "name of label"```

## Notes for myself:

### How stuff is stored:

- Every board has its own directory inside ```{dir}/boards/``` (name ist the id)
- Info about the board is stored in ```{dir}/boards/{boardId}/.info.json```
- Every column is stored as a directory inside ```{dir}/boards/{boardId}/```
- Info about a column is stored in ```{dir}/boards/{boardId}/{columnName}/.info.json```
- Tasks are stored as json files inside ```{dir}/boards/{boardId}/{columnName}/```
- Labels are stored as json files inside ```{dir}/labels/```
