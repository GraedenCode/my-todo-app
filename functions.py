FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ This function gets the list of todos from the text file reads the lines and returns a list. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ This functions writes the Todos from the list to the todos.txt file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("This is a Module")