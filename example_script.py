from employee_database import Employee, Company

comp = Company()
comp.add_employees_from_file("add_employees.txt")
# print(comp.employees)
jims = comp.search_employee(first_name="Jim")
print(jims)
smiths = comp.search_employee(last_name="Smith")
print(smiths)