import FreeSimpleGUI as sg
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", mode="w") as file:
        pass


Text_label = sg.Text("Type in ToDo")
todo_input = sg.Input(key="Input")
add_button = sg.Button("Add", key="Add")
list_box = sg.Listbox(
    values=functions.get_todo(), size=(45, 10), enable_events=True, key="List_Box"
)
edit_button = sg.Button("Edit", key="Edit")
complete_button = sg.Button("Complete", key="Complete")

window = sg.Window(
    title="ToDo List",
    layout=[
        [Text_label],
        [todo_input, add_button],
        [list_box, [edit_button, complete_button]],
    ],
    font=("黑体", 14),
)
while True:
    event, values = window.read()
    print(values)
    print(event)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Add":
        todos = functions.get_todo()
        todos.append(values["Input"] + "\n")
        functions.write_todo(todos)
        window["List_Box"].update(todos)

    if event == "Edit":
        try:
            todos = functions.get_todo()
            new_todo = values["Input"]
            old_todo = values["List_Box"][0]
            todo_index = todos.index(old_todo)
            todos[todo_index] = new_todo + "\n"
            functions.write_todo(todos=todos)
            window["List_Box"].update(todos)
        except IndexError:
            sg.popup("Please select a todo")

    if event == "List_Box":
        window["Input"].update(values["List_Box"][0].strip("\n"))

    if event == "Complete":
        try:
            todos = functions.get_todo()
            selected_todo = values["List_Box"][0]
            print(selected_todo)
            todos.remove(selected_todo)
            functions.write_todo(todos)
            window["List_Box"].update(todos)
        except IndexError:
            sg.popup("Please select a todo")
window.close()
