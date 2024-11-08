import FreeSimpleGUI as sg

text = sg.Text(text="miao")
input_text = sg.Input(tooltip="todos")
input_text2 = sg.Input()
filesbrower = sg.FilesBrowse()
button = sg.Button("button")
window = sg.Window(
    title="My_First_GUI",
    layout=[[text, button], [filesbrower, input_text2]],
)
window.read()
