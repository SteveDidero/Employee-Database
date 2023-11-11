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

import json
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
            raise TypeError("The employee arg should be an Employee or an int.")
        if isinstance(employee, str) and ({name, gender, dob, email, phone
                , address, position, department, salary} & BAD_VALUES):
            raise ValueError("If a name is given as the first arg then all"
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
        return {
            "name":employee
            ,"gender":gender
            ,"dob":dob
            ,"email":email
            ,"phone":phone
            ,"address":address
            ,"position":position
            ,"department":department
            ,"salary":salary
        }
    
    def __str__(self):
        """Gives the informal representation of the Employee instance.
        
        Primary author: Gene Yu
        
        Returns:
            (str): The printable representation of the instance.
        """
        return str(self.to_dict())


class Company:
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
    
    def __init__(self, employees_file, managers_file):
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
        try:
            employees_dict = json.load(employees_file)
        except json.JSONDecodeError:
            employees_dict = {}
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
        self.employee_id = employee_id

        name = input("Enter employee name: "),
        gender =  input("Enter employee gender: "),
        dob = input("Enter employee date of birth (mm/dd/yyyy): "),
        email =  input("Enter employee email address: "),
        phone_number = input("Enter employee phone number(xxx-xxx-xxxx): "),
        address = input("Enter employee address: "),
        position = input("Enter employee company position: "),
        department = input("Enter employee department: "),
        salary = input("Enter employee salary: ")
        
        duplicate_employee = next(
            (emp for emp in self.employees.values() if emp == {"name": name,
                                                                "gender": gender,
                                                                "dob": dob,
                                                                "email": email,
                                                                "phone_number": phone_number,
                                                                "address": address,
                                                                "position": position,
                                                                "department": department,
                                                                "salary": salary}),
            None
        )

        if duplicate_employee:
            print("Duplicate employee data found:")
            print(f"{duplicate_employee['name']} already exists in the employee database.")
            decision = input("Would you like to retry?\n"
                            "Enter 'y' to re-enter data or 'n' to cancel: ")

        if decision.lower() == 'y':
            self.add_employee(employee_id) 
        else:
            print("Employee addition canceled.")
            return
            
        self.employees[employee_id] = {"name": name,
                         "gender": gender,
                         "dob": dob,
                         "email": email,
                         "phone_number": phone_number,
                         "address": address,
                         "position": position,
                         "department": department,
                         "salary": salary
                         }
        
        print(f"{name} was added to employee database")
    
    def add_employees_from_file(self, file):
        """Add multiple Employees from a file using regex pattern for parsing the file.
        
        Primary author: Jordan Goodman
        
        Args:
            file (str): A path to the file to read.
            
        Side effects: Adds employee information to the employee dictionary.

        """
        with open(file, 'r') as f:
            employees_to_add = [employee for employee in f]
            pattern = re.compile(r'(\d+),[ ]?(\w+ \w+),[ ]?([A-Z]+),[ ]?(\d{2}\/\d{2}\/\d{4}),[ ]?(\w+@gmail\.com),[ ]?(\d{3}-\d{3}-\d{4}),[ ]?(\d+ \w+ \w+),[ ]?([\w\s]+),[ ]?([\w\s]+),[ ]?(\$[\d,]+)') 
        
        matches = re.search(pattern, employees_to_add) 
        for match in matches:            
                employee_id = match[0]
                name = match[1]
                gender = match[2]
                dob = match[3]
                email = match[4]
                phone_number = match[5]
                address = match[6]
                position = match[7]
                department = match[8]
                salary = match[9]
                self.employees[employee_id] = {"name": name, 
                                               "gender": gender, 
                                               "dob": dob, 
                                               "email": email, 
                                               "phone number": phone_number, 
                                               "address": address, 
                                               "position": position, 
                                               "department": department,
                                               "salary": salary}
        return self.employees
    
    def write_employees_json(self, file, employees, *, transaction=True,
            protect_attributes=True):
        """Writes the information of specified Employees to a file.
        
        Primary author: Gene Yu
        
        Args:
            file (str): A path to the JSON to write to.
            employees (iterable of int and Employee): Any combination of
                employee IDs and Employee objects in the employees dict.
            transaction (bool, keyword-only): If True, the write fails if the
                employees arg contains invalid elements.
            protect_attributes (bool, keyword-only): If True, the write fails if
                the file arg is the same as the Company employees file but the
                employees arg is not the same as the employees dictionary.
        
        Returns:
            (int): A status code. Exactly one of the following (
                0: All employees specified were written to the file.
                1: The user attempted to overwrite the Company employees file
                    with something other than the employees dictionary.
                    Nothing was written.
                2: A given Employee or ID did not match an ID in the employees
                    dict. Nothing was written.
                3: A given Employee or ID did not match an ID in the employees
                    dict. Matching employees were written to the file, while
                    non-matching elements were ignored.
            )
        
        Side effects:
            Overwrites the given file.
        """
        if (protect_attributes and file == self.employees_file
                and employees != self.employees):
            # TODO: If allowed, use os.path.realpath() instead of a string
            # equality comparison
            return 1
        if employees == self.employees:
            match_dict = {id:str(self.employees[id]) for id in self.employees}
            json.dump(self.employees, file)
            return 0
        employees_set = set(employees)
        ids = {x for x in employees_set if isinstance(x, int)}
        non_ids_set = employees_set - ids
        objs = {x for x in non_ids_set if isinstance(x, Employee)}
        right_type = ids + objs
        mismatch = False
        if len(right_type) != len(employees_set):
            mismatch = True
        if transaction and mismatch:
            return 2
        employee_to_id = {v:k for k,v in self.employees.items()}
        matches = set()
        mismatches = set()
        for id in ids:
            if id in self.employees:
                matches.add(id)
            else:
                mismatches.add(id)
        for obj in objs:
            if obj in employee_to_id:
                matches.add(employee_to_id(obj))
            else:
                mismatches.add(employee_to_id(obj))
        if mismatches:
            mismatch = True
        if transaction and mismatch:
            return 2
        match_dict = {id:self.employees[id].to_dict() for id in matches}
        json.dump(match_dict, file)
        if mismatch:
            return 3
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
        matching_employees = []

        for employee_id, employee in self.employees.items():
            match = (
                (first_name is None or employee.name.split()[0] == first_name) and
                (last_name is None or employee.name.split()[-1] == last_name) and
                (department is None or employee.department == department)
            )

            if match:
                matching_employees.append(employee)

        return matching_employees

class Manager(Employee):
    """Represents an employee manager in a Company.
    
    Primary author: Steve Tanekeu
    
    Attributes:
        subordinates (list of int): The employee IDs of the manager's
            subordinate Employees.
    """
    
    def __init__(self, employee):
        """Creates the Manager class from an Employee.
        
        Primary author: Gene Yu
        
        Args:
            employee (Employee): The employee to be converted to a Manager.
        
        Side effects:
            Recreates the Employee class attributes.
            Initializes the subordinates attribute.
        """
        super().__init__(employee)
        self.subordinates = []
    
    def add_manager(self):
        """
        check the self.info dictionary and if the position of an employee is manager,
        that person gets added to the manager dictionary else they add to the employees dictionary.

        """
        self.employees = {}
        self.managers = {}
        for p in self.info:
            if p["position"] == "manager":
                self.managers[p["name"]] = p
            else:
                self.employees[p["name"]] = p
        
    def assign_employee(self):
        """
        Cross check the department of each employment and manager and append the employee's name
        to the corresponding manager's employee key.
        """

        for p in self.managers:
            self.managers[p]["employees"] = []

        for em in self.employees:
            for i in self.managers:
                if em['department'] == self.managers[i]['department']:
                    self.managers[i]["employees"].append(em["name"])
        
        name = input('Give me a name: ')
    
        for i in self.managers:
            # for a in i: # This line is not needed
            if name in self.managers[i]["employees"]:
                print(f"{name} falls under {i}")
            else:
                None        



