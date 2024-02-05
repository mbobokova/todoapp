while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            index += 1
            row = f"{index}-{item}"
            print(row)
    elif "exit" in user_action:
        break
    elif "edit" in user_action:
        number = int(input("Number of the todo to edit: "))
        number -= 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action[0:8]:
        number = int(input("Number of the todo to complete: "))

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        completed_todo = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        complete_message = f"Todo {completed_todo} was completed"
        print(complete_message)

        ''' whatever
        case _:            
            print("You entered an unknown command!")
        '''

print("Goodbye!")