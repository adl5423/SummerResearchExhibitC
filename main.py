```python
# main.py

"""
This module contains the main execution code for the application.
"""

from employee_module import Employee
from employee_management import EmployeeManagement

if __name__ == "__main__":
    manager = EmployeeManagement()

    # Adding employees
    manager.add_employee(1, "John Doe", "Manager", 70000)
    manager.add_employee(2, "Jane Smith", "Developer", 80000)
    manager.add_employee(3, "Emily Davis", "Designer", 75000)

    # Displaying employees
    manager.display_employees()

    # Removing an employee
    manager.remove_employee(2)

    # Displaying employees after removal
    manager.display_employees()

    emp = Employee(4, "Chris Brown", "Intern", 5000)

    manager.remove_employee(emp.emp_id)

    manager.display_employees()
```