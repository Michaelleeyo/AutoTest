from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('zhang', 'san')

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        add_salary = 3000
        self.employee.give_raise(add_salary)
        self.assertEqual(self.employee.salary, 13000)


unittest.main()
