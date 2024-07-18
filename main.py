# main.py

from employee_management import EmployeManagement  # Easy error: Typo in import statement

if __name__ == "__main__":
    manager = EmployeeManagment()  # Easy error: Typo in class instantiation

    # Adding employees
    manager.add_employee(1, "John Doe", "Manager")
    manager.add_employee(2, "Jane Smith", "Developer")
    manager.add_employee(3, "Emily Davis", "Designer")

    # Displaying employees
    manager.display_employees()

    # Removing an employee
    manager.remove_emploe(2)  # Easy error: Typo in method call

    # Displaying employees after removal
    manager.display_employs()  # Easy error: Typo in method call

    # Hard error: Incorrect object instantiation
    emp = Employee(str(4), "Chris Brown", "Intern", "5000")  # id should be an int, and salary should be an int, not str

    # Medium error: Logical error in remove_employee
    manager.remove_employee(4)  # Trying to remove non-existing employee

    # Medium error: Misspelled variable name
    manager.display_employ()  # Wrong method name (should be display_employees)
