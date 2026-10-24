"""Employee class"""


class Employee:
    """Employee class"""

    def __init__(self, first_name, last_name, annual_salary):
        """Store the first/last name and salary of an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Give raise to the employee, defaults to 5000"""
        self.annual_salary += amount
