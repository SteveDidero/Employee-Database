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

BAD_VALUES = frozenset({None, ""})

class Employee:
    """Represents the personal information of an employee at a company.
    
    Primary author: ?
    
    Attributes:
        info (dict): A dictionary containing the following key-value pairs {
            "name": (str) The employee's name.
            "gender": (str) Either "m"an, "w"oman, or "n"onbinary.
            "dob": (str) Date of birth.
            "email": (str) Email address.
            "phone": (str) Phone number.
            "address": (str) Home address.
            "position": (str) The employee's job.
            "department": (str) The employee's department.
            "salary": (int) Annual gross salary.
        }
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
            Creates and modifies the attribute called info.
        """
        if not isinstance(employee, (Employee, str)):
            raise TypeError("The employee arg should be an Employee or an int.")
        if isinstance(employee, str) and ({name, gender, dob, email, phone
                , address, position, department, salary} & BAD_VALUES):
            raise ValueError("If an ID is given then the other attributes must"
                "be non-empty.")
        if isinstance(employee, Employee):
            self.info = employee.info.copy()
            return
        self.info = {
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

class Company:
    """Represents the people in a company.
    
    Primary author: ?
    
    Attributes:
        PLACEHOLDER
        employees_file (str): A path to the JSON which stores all Employee
            objects.
        employees (dict of int:Employee): The employee IDs and the corresponding
            Employee objects.
    """
    
    def __init__(self, employees_file):
        """PLACEHOLDER
        
        Primary author: ?
        """
        # PLACEHOLDER
        self.employees_file = employees_file
        self.employees = {}
    
    def add_employee(self, id, employee, update=False):
        """Adds an Employee to the dictionary of employees.
        PLACEHOLDER
        
        Primary author: ?
        
        Args:
            id (int): The ID of the employee.
            employee (Employee): The employee's corresponding Employee object.
            update (bool): If update is False, then adding an existing ID will
                fail. If update is True and the ID exists, then the
                corresponding Employee will be overwritten.
        """
        # PLACEHOLDER
    
    def write_employees_json(self, file, employees, *, add_only=True):
        """Writes the information of Employees to a file.
        
        Primary author: Gene Yu
        
        Args:
            employees (list of Employee): Any combination of employees in the
                employees dict.
        """
        # PLACEHOLDER