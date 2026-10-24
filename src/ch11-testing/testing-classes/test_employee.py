from employee import Employee
import pytest

@pytest.fixture
def create_employee():
    """Create shared Employee instance"""
    employee = Employee('John', 'White', 60000)
    return employee

def test_give_default_raise(create_employee):
    """Check if the default functionality works."""
    create_employee.give_raise()
    assert create_employee.annual_salary == 65000


def test_give_custom_raise(create_employee):
    """Check if the custom functionality works."""
    create_employee.give_raise(10000)
    assert create_employee.annual_salary == 70000
