'''

Welcome to the first practical exercise on class collaboration! In this task, we'll address the Feature Envy code smell. You'll find methods overly interested in data from another class rather than focusing on their own responsibilities. Your job is to refactor the code to improve clarity and ensure that each class is responsible for its own functionality.

The code consists of two classes, Employee and Department, with updated requirements. Let's refactor and organize the code such that each class handles its specific responsibilities!

'''

from enum import Enum

class Performance(Enum) :
# {
    AVERAGE = 1.0
    GOOD = 1.2
    EXCELLENT = 1.5
# }

class Employee :
# {
    def __init__(self, name, salary, fixed_bonus, performance) :
    # {
        self.name = name
        self.salary = salary
        self.fixed_bonus = fixed_bonus
        self.performance = performance
    # }

    def annual_bonus(self, bonus_rate) :
    # {    
        return self.salary * bonus_rate * self.performance.value + self.fixed_bonus
    # }

# }

class Department :
# {
    def __init__(self, bonus_rate) :
    # {
        self.bonus_rate = bonus_rate
        self.employees = []
    # }

    def add_employee(self, employee) :
    # {
        self.employees.append(employee)
    # }

    def calculate_total_bonuses(self) :
    # {
        tb  = 0 # total bonus

        for employee in self.employees :
        # {
            tb = tb + employee.annual_bonus(self.bonus_rate)
        # }

        return tb
    # }

# }

def main() :
# {
    employee1 = Employee("John Doe", 50000, 1000, Performance.GOOD)
    employee2 = Employee("Jane Smith", 60000, 1500, Performance.EXCELLENT)

    d = Department(0.10)  # 10% bonus rate
    d.add_employee(employee1)
    d.add_employee(employee2)
    
    # annual_bonus1 = d.calculate_annual_bonus(employee1)
    # annual_bonus2 = d.calculate_annual_bonus(employee2)

    print("Annual Bonus for John Doe:", employee1.annual_bonus(d.bonus_rate))
    print("Annual Bonus for Jane Smith:", employee2.annual_bonus(d.bonus_rate))

    # employees = [employee1, employee2]
    #total_bonuses = department.calculate_total_bonuses(employees)
    print("Total Bonuses for all Employees:", d.calculate_total_bonuses())
# }

if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

def get_salary(self) :
    # {
        return self.salary
    # }

    def get_performance(self) :
    # {
        return self.performance
    # }

    def get_fixed_bonus(self) :
    # {
        return self.fixed_bonus
    # }

'''