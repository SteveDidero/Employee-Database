from employee_database import Employee, Company

emp = Employee("Name","n","Yesterday","email@email","1234","My house"
    ,"Floor crawler","Crawling Department",45)
print("Example employee:")
print(emp)
print()

comp = Company()
comp.add_employees_from_file("add_employees.txt")
print("Employees added from a file:")
print(comp.employees)
print()

jims = comp.search_employee(first_name="Jim")
print("Searching for employee by first name Jim:")
print(jims)
print()

smiths = comp.search_employee(last_name="Smith")
print("Searching for employee by last name Smith:")
print(smiths)
print()

new_id = 58435
print("Adding an employee manually:")
comp.add_employee(new_id)
print(comp.employees[new_id])
print()

comp.add_manager("Karen Brown")
comp.assign_employee("Karen Brown", "Bob Marley")
comp.assign_employee("Karen Brown", "Rebecca Miraj")
print("Adding a manager and assigning subordinates:")
print(comp.managers)
print()