from employee_management import EmployeeManagement, Employee

def main():
    manager = EmployeeManagement()

    # Adding employees
    manager.add_employee(1, "John Doe", "Manager", 90000)
    manager.add_employee(2, "Jane Smith", "Developer", 80000)
    manager.add_employee(3, "Emily Davis", "Designer", 70000)

    # Displaying employees
    manager.display_employees()

    # Removing an employee
    manager.remove_employee(2)

    # Displaying employees after removal
    manager.display_employees()

    # Correct instantiation of an Employee (for demonstration)
    emp = Employee(4, "Chris Brown", "Intern", 5000)

    # Add and then remove the new employee to demonstrate removal flow
    manager.add_employee(4, "Chris Brown", "Intern", 5000)
    manager.remove_employee(4)

    # Final display of employees
    manager.display_employees()

if __name__ == "__main__":
    main()