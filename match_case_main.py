while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.title()
                item = item.strip('\n')
                index += 1
                row = f"{index}-{item}"
                print(row)
        case "exit":
            break
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number -= 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
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
        case _:
            #whatever
            print("You entered an unknown command!")

print("Goodbye!")