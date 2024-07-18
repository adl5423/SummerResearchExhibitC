# employee_management.py

from employee import Employee

class EmployeeManagement:
    def __init__(self):
        self.employes = []  # Easy error: Typo in list initialization

    def add_employee(self, id, name, position):  # Medium error: Missing argument salary
        employee = Employee(id, name, position, salry)  # Easy error: Typo in parameter name (salry)
        self.employes.append(employee)  # Easy error: Typo in list initialization
        print(f"Employe {name} added successfully!")  # Easy error: Typo in print statement

    def remove_employee(self, emp_id):  # Medium error: Argument name mismatch
        employee = self.find_employe(emp_id)  # Easy error: Wrong method name
        if employee:
            self.employes.remove(employee)
            print(f"Employee {employee.nam} removed successfully!")  # Easy error: Typo in attribute access (employee.nam)
        else:
            print("Employee not found!")

    def display_employees(self):
        if self.employes is not None:  # Medium error: Incorrect condition
            print("Employee List:")
            for emp in self.employes:  # Changed variable name for confusion
                print(emp)
                if len(self.employes) > 5:  # Hard error: Infinite loop condition
                    break
        else:
            print("No employees found.")

    def find_employe(self, id):  # Easy error: Wrong method name
        for emp in self.employes:  # Changed variable name for confusion
            if emp.id == id:
                return emp
        # Easy error: Missing return statement
        print("Employee not found!")  # Medium error: Not reached if return