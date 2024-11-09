import FreeSimpleGUI as sg
import functions

Text_label = sg.Text("Type in ToDo")
todo_input = sg.Input(key="Input")
add_button = sg.Button("Add", key="Add")
list_box = sg.Listbox(
    values=functions.get_todo(), size=(45, 10), enable_events=True, key="List_Box"
)
edit_button = sg.Button("Edit", key="Edit")

window = sg.Window(
    title="ToDo List",
    layout=[[Text_label], [todo_input, add_button], [list_box, edit_button]],
    font=("黑体", 14),
)
while True:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Add":
        todos = functions.get_todo()
        todos.append(values["Input"] + "\n")
        functions.write_todo(todos)
        window["List_Box"].update(todos)

    if event == "Edit":
        todos = functions.get_todo()
        new_todo = values["Input"]
        old_todo = values["List_Box"][0]
        todo_index = todos.index(old_todo)
        todos[todo_index] = new_todo + "\n"
        functions.write_todo(todos=todos)
        window["List_Box"].update(todos)
window.close
