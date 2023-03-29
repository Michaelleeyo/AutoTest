class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.salary = 10000

    def give_raise(self, raise_salary=5000):
        self.salary += raise_salary
