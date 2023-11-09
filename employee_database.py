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
    """The personal information of an employee at a company.
    
    Attributes:
        info (dict): A dictionary containing the following key-value pairs {
            "id": (int) The employee's ID at the company. Should be unique.
            "name": (str)
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
    
    def __init__(self, employee, name="", gender="", dob="", email="", phone=""
            , address="", position="", department="", salary=-1):
        """Initializes the employee's record.
        
        Args:
            employee: Either an employee ID (int) or an Employee object. The
                following args must be given if the employee arg is an ID.
            "name": (str)
            "gender": (str) Either "m"an, "w"oman, or "n"onbinary.
            "dob": (str) Date of birth.
            "email": (str) Email address.
            "phone": (str) Phone number.
            "address": (str) Home address.
            "position": (str) The employee's job.
            "department": (str) The employee's department.
            "salary": (int) Annual gross salary.
        """
        if not isinstance(employee, (Employee, int)):
            raise TypeError("The employee arg should be an Employee or an int.")
        if isinstance(employee, int) and ({name, gender, dob, email, phone
                , address, position, department, salary} & BAD_VALUES):
            raise ValueError("If an ID is given then the other attributes must"
                "be non-empty.")
        if isinstance(employee, Employee):
            self.info = employee.info.copy()
            return
        