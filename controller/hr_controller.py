from model.hr import hr
from view import terminal as view


def list_employees():
    table = hr.open_file_return_table()
    view.print_table(table)


def add_employee():
    view.print_error_message("Not implemented yet.")


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    dictionary_of_bd = {}
    table = hr.open_file_return_table()
    for ele in range(1,len(table)):
        dictionary_of_bd[table[ele][1]] = table[ele][2]
    dictionary_of_bd = dict(sorted(dictionary_of_bd.items(), key=lambda item: item[1], reverse=True))
    youngest_oldest = list(dictionary_of_bd.items())
    youngest = (youngest_oldest[0][0])
    oldest = (youngest_oldest[-1][0])
    print(f'Youngest: {youngest}')
    print(f'Oldest: {oldest}')


def get_average_age():
    age_string = ''
    average_age_int = 0
    table = hr.open_file_return_table()
    average_age = []
    for ele in range(1,len(table)): 
        average_age.append(table[ele][2])
    for x in range(len(average_age)):
        for year in average_age[x]:
            if year == '-':
                break
            else:
                age_string += year
                if len(age_string) == 4:
                    employee_year = 2021 - int(age_string)
                    average_age_int += employee_year
                    age_string = ''
    average_age = average_age_int / len(average_age)
    print(f'Average age of emplyers is: {average_age}')
    

def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
