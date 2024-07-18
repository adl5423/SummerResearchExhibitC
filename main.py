```python
"""Module docstring for main.py"""

from employee_management import EmployeeManagement

if __name__ == "__main__":
    manager = EmployeeManagement()

    # Adding employees
    manager.add_employee(1, "John Doe", "Manager", 70000)
    manager.add_employee(2, "Jane Smith", "Developer", 80000)
    manager.add_employee(3, "Emily Davis", "Designer", 75000)
    manager.add_employee(4, "Chris Brown", "Intern", 5000)

    # Displaying employees
    manager.display_employees()

    # Removing an employee
    if manager.remove_employee(2):
        print(f"Employee Jane Smith removed successfully!")
    else:
        print("Employee not found!")

    # Displaying employees after removal
    manager.display_employees()

    if manager.remove_employee(4):
        print(f"Employee Chris Brown removed successfully!")
    else:
        print("Employee not found!")

    manager.display_employees()
```