# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add") or user_action.startswith("new"):
    # if "add" in user_action[0:3] or "new" in user_action[0:3]:
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            index += 1
            row = f"{index}-{item}"
            print(row)
    elif user_action.startswith("exit"):
        break
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Wrong command, must be number of ToDo")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            complete_message = f"Todo {completed_todo} was completed"
            print(complete_message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Wrong command, must be number of ToDo")
            continue

    else:
        print("You entered an unknown command!")


print("Goodbye!")