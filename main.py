todos = []

while True:
    userInput = input("Enter add, delete, edit, show: ")
    userInput = userInput.strip().split(' ',1)
    user_command = userInput[0]
    if len(userInput) >=2:
        user_content = userInput[1]

    todos = open('todos.txt','r').readlines()

    match user_command:
        case 'add':
            file = open("todos.txt",'a')
            todos.append(user_content + '\n')
            file.writelines(user_content+'\n')
            

        case 'delete':
            if user_content.isnumeric():
                todos.pop(int(user_content)+1)
            else:
                todos.remove(user_content)
                         
        case 'edit':
            print('edit')

        case 'show':
            for index, todo in enumerate(todos):
                print(f"{index+1}.{todo.capitalize()}")