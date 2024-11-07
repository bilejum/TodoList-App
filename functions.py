def get_todo():
    with open("todos.txt", "r", encoding="utf-8") as file:
        todos = file.readlines()
    return todos


def write_todo(todos):
    with open("todos.txt", "w", encoding="utf-8") as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Im run")
