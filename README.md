# Inst-326 Pythonista Final Project

## Existing files in the repository and their purpose
1. **employee_database.py**
  * What the employee_database.py file does......in-progress
2. **example_script.py**
  * Python script for demonstration. Completes the following tasks:
     1. Creates employees from file.
     2. Creates employees through manual input prompts.
     3. Searches for an employee in the database.
     4. Add manager
     5. Add subordinates
     6. Demote manager   
3. Simplecal.py
  * Team familiarization with git commands.
    1. git add
    2. git commit
    3. git pull
    4. git push
    5. git merge
    6. git fetch
    7. git status
4. **add_employees.txt**
  * Text file with employee information to be added to the company database. Information is as follows (separated by commas with no spaces):
    1. Employee ID (7 digits: ex. 0001234)
    2. Name (First and Last name: ex. Jim Smith)
    3. Gender (F, M, or N)
    4. Birthdate (MM/DD/YYY: ex. 10/13/1970)
    5. Email Address (@gmail.com: john54@gmail.com)
    6. Phone Number (xxx-xxx-xxxx: 301-555-9876)
    7. Mailing Address (3722 Turkey Road)
    8. Position
    9. Department
    10. Salary (include $ and commas: ex.85,000)

## Instructions to run a program from the command line
1. Provide a file to be created and written to save employee data. 
2. Select the task to be completed from the following options:
   ```python
   1: Add employee manually
   2: Add employee from file
   3: Add manager
   4: Assign employee to manager
   5: Demote manager
   6: Remove employee
   7: Remove employee from a manager
   8: Modify employee data
   9: Save company data
   10: Search for an employee
   11: Print all employees
   12: Print all managers
   99. Quit
   ```
3. Option 1: Add employee manually:
   * name (First Last)
   * gender 
   * dob (mm/dd/yyyy)
   * email 
   * phone(xxx-xxx-xxxx)
   * address 
   * position 
   * department 
   * salary 
4. Option 2: Add employee from file:
   * filename
5. Option 3: Add manager:
   * manager name (First Last)
6. Option 4: Assign employee to manager:
   * manger name (First Last)
   * employee name (First Last)
7. Option 5: Demote manger:
   * manager name (First Last)
8. Option 6: Remove employee:
   * employee id of individual to be removed.
9. Option 7: Remove employee from manager:
   * manager name (First Last)
   * employee name (First Last)
10. Option 8: Modify employee data:
   * employee id of individual to be modified
11. Option 9: Save Company Data:
   * save data added
12. Option 10: Search for an employee:
   * search for an employee by name (First Last)
13. Option 11: Print all employees:
   * show all employees in database
14. Option 12: Print all managers:
   * show all managers in database
15. Option 99: Quit
   * Exits program

## How to use the program and interpret the output
* progam
* output


|Method/function                |Primary author  |Techniques demonstrated                  |
| :---------------------------- | :------------- | :-------------------------------------- |
|Company.write_employees_json   |Gene Yu         |json.load()                              |
|Company.add_employees_from_file|Jordan Goodman  |Regular Expressions,With statements      |
|Company.search_employees       |Trinity Hill    |Optional parameters (keyword arguments)  |
|Company.remove_subordinate     |Steve Tanekeu   |f-strings                                |
|Company.add_employee           |Spencer Morgan  |Generator expression                     |
|Employee.\_\_repr\_\_          |Gene Yu         |Magic methods other than \_\_init\_\_()  |
|Company.remove_employees       |Jordan Goodman  |Conditional statement                    |
|Edit employee attributes       |Trinity Hill    |                                         |
|Company.demote_manager         |Steve Tanekeu   |Sequence unpacking                       |
|parse_args                     |Spencer Morgan  |ArgumentParser                           |
  
## Sources
* None


For INST326 project at UMD fall 2023
