""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

#from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def open_file_return_table():
    with open(DATAFILE, 'r') as file:
        content = file.read().splitlines()
        for i in range(len(content)):
            content[i] = str(content[i])
            content[i] = content[i].split(';')
        content.insert(0, HEADERS)
        return content
