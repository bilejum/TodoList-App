while True:
    userInput = input("Enter add, delete, edit, show: ")
    userInput = userInput.strip().split(" ", 1)
    user_command = userInput[0]
    if len(userInput) >= 2:
        user_content = userInput[1]

    match user_command:
        case "add":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(user_content + "\n")
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "delete":
            try:
                with open("todos.txt", "r") as file:
                    todos = file.readlines()

                if user_content.isnumeric():
                    delete_content = todos.pop(int(user_content) - 1)
                    with open("todos.txt", "w") as file:
                        file.writelines(todos)
                        print(f"{delete_content} is deleted.")

                else:
                    todos.remove(user_content + "\n")
                    with open("todos.txt", "w") as file:
                        file.writelines(todos)
                        print(f"{user_content} is deleted.")
            except:
                print(f"{user_content} is not exist")

        case "edit":
            print("edit")

        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index+1}.{todo.capitalize()}")

        case _:
            print("invaild command, Please enter add, delete, edit, show.")
