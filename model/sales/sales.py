""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def open_file_return_table():
    with open(DATAFILE, 'r') as file:
        content = file.read().splitlines()
        for i in range(len(content)):
            content[i] = str(content[i])
            content[i] = content[i].split(';')
        content.insert(0, HEADERS)
        return content

def modify_file():
    id = get_new_id()
    customer_name = input('provide customer name ')
    product = input('provide product name ')
    price = input('provide item price ')
    date = input('provide transaction date ')
    
    to_append = (f'{id};{customer_name};{product};{price};{date}')
    with open(DATAFILE, 'a') as file:
        file.write(to_append)
        file.write('\n')

def get_new_id():
    util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
