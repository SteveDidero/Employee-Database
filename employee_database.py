"""Classes representing a database of employees and managers in a company.

Copyright (C) 2023
Jordan Goodman, Trinity Hill, Spencer Morgan, Steve Tanekeu, Gene Yu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
# INST326 section 0101
# Team: Pythonista
from argparse import ArgumentParser
import json
from pathlib import Path
import re
BAD_VALUES = frozenset({None, ""})

class Employee():
    """Represents the personal information of an employee at a company.

    Primary author: Gene Yu

    Attributes:
        name (str): The employee's name.
        gender (str): Either "m"an, "w"oman, or "n"onbinary.
        dob (str): Date of birth.
        email (str): Email address.
        phone (str): Phone number.
        address (str): Home address.
        position (str): The employee's job.
        department (str): The employee's department.
        salary (int): Annual gross salary.
    """

    def __init__(self, employee, gender="", dob="", email="", phone=""
            , address="", position="", department="", salary=-1):
        """Initializes the employee's record.

        Primary author: Gene Yu

        Args:
            employee: Either a name (str) or an Employee object. The following
                args must be given if the employee arg is a name.
            gender: (str) Either "m"an, "w"oman, or "n"onbinary.
            dob: (str) Date of birth.
            email: (str) Email address.
            phone: (str) Phone number.
            address: (str) Home address.
            position: (str) The employee's job.
            department: (str) The employee's department.
            salary: (int) Annual gross salary.

        Side effects:
            Creates and modifies all attributes (name, gender, dob, email, phone
                , address, position, department, and salary).
        """
        if not isinstance(employee, (Employee, str)):
            raise TypeError("The employee arg should be an Employee or an str.")
        if isinstance(employee, str) and ({employee, gender, dob, email, phone
                , address, position, department, salary} & BAD_VALUES):
            raise ValueError("If a name is given as the first arg then all "
                "attributes must be non-empty.")
        if isinstance(employee, Employee):
            self.name = employee.name
            self.gender = employee.gender
            self.dob = employee.dob
            self.email = employee.email
            self.phone = employee.phone
            self.address = employee.address
            self.position = employee.position
            self.department = employee.department
            self.salary = employee.salary
            return
        self.name = employee
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address
        self.position = position
        self.department = department
        self.salary = salary

    def __repr__(self):
        """Gives the formal representation of the Employee instance.

        Primary author: Gene Yu

        Returns:
            (str): A string which when used as the arg for eval() reconstructs
                this Employee instance.
        """
        ordered_info = [
            self.name
            ,self.gender
            ,self.dob
            ,self.email
            ,self.phone
            ,self.address
            ,self.position
            ,self.department
            ,self.salary
        ]
        return "Employee(" + ",".join((repr(x) for x in ordered_info)) + ")"

    def to_dict(self):
        """Gives the dictionary representation of the Employee instance.

        Primary author: Gene Yu

        Returns:
            (dict): A dictionary containing all attributes as key-value pairs
                in the form "attribute_name":attribute_value.
        """
        info_dict = {
            "name":self.name
            ,"gender":self.gender
            ,"dob":self.dob
            ,"email":self.email
            ,"phone":self.phone
            ,"address":self.address
            ,"position":self.position
            ,"department":self.department
            ,"salary":self.salary
        }
        return info_dict

    def __str__(self):
        """Gives the informal representation of the Employee instance.

        Primary author: Gene Yu

        Returns:
            (str): The printable representation of the instance.
        """
        return str(self.to_dict())


class Company():
    """Represents the people in a company.

    Primary author: ?

    Attributes:
        employees_file (str): A path to the JSON which stores all Employee
            attributes.
        managers_file (str): A path to the JSON which stores the Manager ids
            and respective lists of their subordinates' ids.
        employees (dict of int:Employee): The employee IDs and the corresponding
            Employee objects. Includes Manager objects.
        managers (list of int): Employee IDs of the Manager objects according to
            the ids in the dictionary of employees.
    """

    def __init__(self, employees_file="../default_employees_file.json"):
        """Recreates the Company object from the files of employee and manager
        information.

        Primary author: Gene Yu

        Args:
            employees_file (str): A path to the JSON which stores all Employee
                objects.

        Side effects:
            Creates and sets the employees_file attribute.
            Creates and populates the employees attribute.
        """
        self.employees_file = employees_file
        emp_path = Path(self.employees_file)
        if not emp_path.exists() or emp_path.is_dir():
            self.employees = {}
            self.managers = {}
            return
        with open(self.employees_file, "r", encoding="utf-8") as emp_fp:
            try:
                employees_info = json.load(emp_fp)
            except json.JSONDecodeError:
                self.employees = {}
                self.managers = {}
                return
        try:
            employees_dict = employees_info["employees"]
        except KeyError:
            self.employees = {}
            self.managers = {}
            return
        self.employees = {}
        for id,e in employees_dict.items():
            self.employees[id] = Employee(e["name"],e["gender"],e["dob"]
                ,e["email"],e["phone"],e["address"],e["position"]
                ,e["department"],e["salary"])

    def add_employee(self, employee_id):
        """Adds an Employee to the dictionary of employees.

        Primary author: Spencer Morgan

        Args:
            employee_id (int): The ID of the employee.

        Side effects:
            displays the employee who was added to the database.
        """
        name = input("Enter employee name: ")
        gender =  input("Enter employee gender: ")
        dob = input("Enter employee date of birth (mm/dd/yyyy): ")
        email =  input("Enter employee email address: ")
        phone = input("Enter employee phone number(xxx-xxx-xxxx): ")
        address = input("Enter employee address: ")
        position = input("Enter employee company position: ")
        department = input("Enter employee department: ")
        salary = input("Enter employee salary: ")

        duplicate_employee = next(
            (emp for emp in self.employees.values() if emp.to_dict() == {"name": name,
                                                                "gender": gender,
                                                                "dob": dob,
                                                                "email": email,
                                                                "phone": phone,
                                                                "address": address,
                                                                "position": position,
                                                                "department": department,
                                                                "salary": salary}),
            None
        )

        if duplicate_employee:
            print("Duplicate employee data found:")
            print(f"{duplicate_employee.name} already exists in the employee database.")
            decision = input("Would you like to retry?\n"
                            "Enter 'y' to re-enter data or 'n' to cancel: ")

            if decision.lower() == 'y':
                self.add_employee(employee_id)
            else:
                print("Employee addition canceled.")
            return

        self.employees[employee_id] = Employee(name,gender,dob,email,phone,
                                               address,position,department,salary)

        print(f"{name} was added to employee database")

    def add_employees_from_file(self, file):
        """Add multiple Employees from a file using regex pattern for parsing the file.

        Primary author: Jordan Goodman

        Args:
            file (str): A path to the file to read.

        Side effects: Adds employee information to the employee dictionary.

        """
        """The file contains each employee's information separated by commas.
        The expected format for each employee's information is as follows:

        emp_id: Seven digits with three leading zeros.
        emp_name: First and last name.
        gender: Single letter.
        dob: Date of birth in the format "MM/DD/YYYY".
        email: Email address (only Gmail allowed).
        phone: Phone number with ten digits separated by dashes.
        address: Four numbers followed by the street name.
        position: Capitalized word.
        department: Capitalized word.
        salary: Annual gross salary starting with "$" and digits separated by commas.

        """
        with open(file, 'r') as f:
            employees_to_add = f.readlines()
            pattern = re.compile(r'(\d+),[ ]?(\w+ \w+),[ ]?([A-Z]+),[ ]?(\d{2}\/\d{2}\/\d{4}),[ ]?(\w+@gmail\.com),[ ]?(\d{3}-\d{3}-\d{4}),[ ]?(\d+ \w+ \w+),[ ]?([\w\s]+),[ ]?([\w\s]+),[ ]?(\$[\d,]+)')

        matches = [re.search(pattern, employee) for employee in employees_to_add]
        for match in matches:
            if match:
                employee_id = match[1]
                name = match[2]
                gender = match[3]
                dob = match[4]
                email = match[5]
                phone = match[6]
                address = match[7]
                position = match[8]
                department = match[9]
                salary = match[10]
                self.employees[employee_id] = Employee(name,gender,dob,email,phone,
                                               address,position,department,salary)
        return self.employees

    def write_employees_json(self, file, protect_attributes=True):
        """Writes all employees and managers to a file.

        Primary author: Gene Yu

        Args:
            file (str): A path to the JSON file to write to.
            protect_ettributes (bool): If True, prohibits writing to the
                employees_file. Warning: only does a naive string comparison
                of the file paths.

        Returns:
            (int): A status code. Exactly one of the following (
                0: The write succeeded.
                1: The write failed because the given file was the same as the
                    employees_file and protect_attributes was True.
            )

        Side effects:
            Overwrites the given file.
        """
        if (protect_attributes and file == self.employees_file):
            return 1
        employees = {id:self.employees[id].to_dict() for id in self.employees}
        write_info = {"employees":employees, "managers":self.managers}
        with open(file, "w", encoding="utf-8") as write_fp:
            json.dump(write_info, write_fp)
        return 0

    def search_employee(self, first_name=None, last_name=None, department=None):
        """Search for employees based on the provided criteria.

        Primary author: Trinity Hill

        Args:
            first_name (str, optional): First name of the employee.
            last_name (str, optional): Last name of the employee.
            department (str, optional): Department of the employee.

        Returns:
            List of Employee objects that match the search criteria.
        """
        if not first_name and not last_name and not department:
            return "Please provide at least one search criteria."
        matching_employees = []

        for employee_id, employee in self.employees.items():
            match = (
                (not first_name or employee.name.split()[0] == first_name) and
                (not last_name or employee.name.split()[-1] == last_name) and
                (not department or employee.department == department)
            )

            if match:
                matching_employees.append(employee)
                   
        return matching_employees

    def edit_employee(self, employee_id):
        if employee_id not in self.employees:
            print(f"No employee found with ID {employee_id}.")
            return

        employee = self.employees[employee_id]

        updated_attributes = {}
        for attr, value in employee.to_dict().items():
            updated_value = input(f"Enter updated {attr} (press Enter to skip): ") or value
            updated_attributes[attr] = updated_value

        self.employees[employee_id] = Employee(updated_attributes)
        print(f"Employee with ID {employee_id} updated successfully.")

    def add_manager(self, name):
        """

        Primary author: Steve Tanekeu
        """
        for i in self.employees.values():
            if i.name == name:
                self.managers[name] = []
                return f'{name} was successfully added!'
        return f'{name} is not an employee in the system.'

    def assign_employee(self, manager, name):
        """

        Primary author: Steve Tanekeu
        """
        if (manager not in self.managers):
            return f"Manager {manager} does not exist."

        for p in self.employees:
            if self.employees[p].name == name:
                self.managers[manager].append(name)
                return f'Task complete. {p} was assigned to {manager}'
        return f'{name} is not an employee in the system!'

    def remove_employee(self, employee_id):
        """Deletes an employee from the employee dictionary.

        Primary author: Jordan Goodman

        Args:
            employee_id(int): The ID of the employee.

        Side effects:
            displays the removed employee from the database.
        """
        if employee_id in self.employees:
            del self.employees[employee_id]
            return f"Employee with ID {employee_id} was removed from the database."
        else:
            return f"Employee not found."

    def remove_subordinate(self, manager, name):
        if manager not in self.managers:
            raise ValueError(f"{manager} is a not manager in the system!")
        if name not in self.managers[manager]:
            raise ValueError(f'{name} is not a subordinate of {manager}!')
        self.managers[manager].remove(name)
        return f"{name} was removed the list of {manager}'s subordinates!"

    def demote_manager(self, manager):
        if manager not in self.managers.keys():
            raise ValueError(f'{manager} is not a manager!')
        name = ''
        subordinate = ''
        for m in self.managers:
            name, subordinate = m, self.managers[m]
            
        if name == manager:
            del self.managers[name]
        return f"{manager} was removed!"


def main():
    com = Company()
    
    while True:
        print("Hello, welcome to INST 326 Employee management data Center!")
        print("Please review and select from the following options")
        print("""1: Add employee manually
                2: Add employee from file
                3: Add manager
                4: Assign employee to manager
                5: Demote manager
                6: Remove employee
                7: Remove employee from a manager
                8: Modify employee data
                9: Save company data
                10: Search for an employee
                11. Quit
        """)
        answer = int(input("Please enter a number: "))

        if answer == 1:
            id = int(input('Enter an Id for the employee you want to add'))
            task = com.add_employee(id)
        elif answer == 2:
            file = input("Enter your file name(example: myfile.txt): ")
            task = com.add_employees_from_file(file)
        elif answer == 3:
            name = input("Enter the new manager's name")
            task = com.add_manager(name)
        elif answer == 4:
            manager = input("Enter the manager's name: ")
            name = input("Enter the employee's name: ")
            task = com.assign_employee(manager, name)
        elif answer == 5:
            print("nothing")
        elif answer == 8:
            employee_id = int(input("Enter the employee's ID number: "))
            if employee_id in com.employees:
                com.edit_employee(employee_id)
            else:
                print(f"No employee found with ID {employee_id}")
        elif answer == 9:
            file = input("Enter the file path to save to. "
                "The file will be in JSON format.")
            status = com.write_employees_json(file)
            if status == 0:
                print(f"Employees and managers saved to {file}.")
            elif status == 1:
                confirm = input(f"Are you sure you want to write to {file}? y/n")
                if confirm.lower() == "y":
                    com.write_employees_json(file, protect_attributes=False)
                    print(f"Employees and managers saved to {file}.")
                else:
                    print("Data not saved.")
            else:
                print("Data not saved.")
        elif answer == 10:
            first_name = input("Enter employee's first name (leave empty if not specified): ").strip()
            last_name = input("Enter employee's last name (leave empty if not specified): ").strip()
            department = input("Enter employee's department (leave empty if not specified): ").strip()
            matching = com.search_employee(first_name, last_name, department)
            print(matching)
        elif answer == 11:
            print("Thank you for using the Employee Management Data Center")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 11.")   
        
def parse_args(args):
    """Parse command-line arguments.
    
    Args:
        args (int): option for commandline argument to initiate task.
        
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser(prog="INST 326 Employee Management", 
                            description="Manage company employee data")
    parser.add_argument("task", type=int, help="select a task to be completed from the options 1-10")
    return parser.parse_args(args)

if __name__=="__main__":
    main()
   
