from functions import get_todo, write_todo


while True:
    userInput = input("Enter add, delete, edit, show: ")
    userInput = userInput.strip().split(" ", 1)
    user_command = userInput[0]
    if len(userInput) >= 2:
        user_content = userInput[1]

    match user_command:
        case "add":

            todos = get_todo()
            todos.append(user_content + "\n")
            write_todo(todos)

        case "delete":
            try:
                todos = get_todo()

                if user_content.isnumeric():
                    delete_content = todos.pop(int(user_content) - 1)
                    write_todo(todos)
                    print(f"{delete_content} is deleted.")

                else:
                    todos.remove(user_content + "\n")
                    write_todo(todos)
                    print(f"{user_content} is deleted.")
            except ValueError:
                print(f"{user_content} is not exist")

        case "edit":
            print("edit")

        case "show":
            todos = get_todo()

            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index+1}.{todo.capitalize()}")

        case _:
            print("invaild command, Please enter add, delete, edit, show.")
