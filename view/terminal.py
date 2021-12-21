from os import umask


def print_menu(title, list_options):
    print(f"{title}:")
    for item in range(len(list_options)):
        print(f"({item}) {list_options[item]}")
    pass


"""Prints options in standard menu format like this:
    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program
    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """


def print_message(message):
    """Prints a single message to the terminal.
    Args:
        message: str - the message
    """
    print(f'Message: {message}')


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == str:
        #label = 'String'
        print(f'{label}:\n {result}')
    elif type(result) == int:
        #label = 'Number'
        print(f'{label}:\n {result}')
    elif type(result) == float:
        formatted_resoult = "{:.2f}".format(result)
        #label = 'Float'
        print(f'{label}:\n {formatted_resoult}')
    elif type(result) == list:
        #label = 'List'
        print(f'{label}:\n {result}')
    elif type(result) == tuple:
        #label = 'Tuple'
        print(f'{label}:\n {result}')
    elif type(result) == dict:
        #label = 'Dictionary'
        print(f'{label}:\n {result}')


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
#table = [['id', 'product', 'type'], ['0', 'bazooka','portable'], ['1', 'sidewinder', 'missile']]
#table = [['id', 'product', 'type', 'costam1', 'costam2'], ['0', 'bazooka','portable','wartosc1','wartosc2'], ['1', 'sidewinder', 'missile','wartosc3','wartosc4'], ['1', 'sidewinder', 'missile','wartosc3','wartosc4'], ['4', 'siddfd', 'assadsaf','rekgpe','pasas']]

def print_table(table):
    """Prints tabular data like above.
    Args:
        table: list of lists - the table to print out
    """
    longest_string = []
    for row in range(len(table)):
        for col in range(len(table[row])):
            longest_string.append(len(table[row][col]))
    top = ['-']
    suma = (max(longest_string)+2) * len(table[0])
    top = top * (suma - 1 + len(table[0]))
    border_table = ''.join(top)
    print(f'/{border_table}\\')
    for row in range(len(table)):
        # print('dupa')
        for col in range(len(table[row])):
            item = table[row][col]
            item = item.center(max(longest_string)+2, ' ')
            print(f"|{item}", end='')
        if table[row][col] == table[-1][-1]:
            pass
        else:
            print('|')
            print(f'|{border_table}|')
    print('|')
    print(f'\\{border_table}/')


# print_table(table)


def get_input(label):
    """Gets single string input from the user.
    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f'{label} :')
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.
    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    user_input_list = []
    for i in range(len(labels)):
        user_input_list.append(input(f'{labels[i]} :'))
    return user_input_list


def print_error_message(message):
    """Prints an error message to the terminal.
    Args:
        message: str - the error message
    """
    print(f'Error: {message}')
