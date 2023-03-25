from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    name: str
    salary: int


class EmployeeDataset:
    def __init__(self, employee_list: List[Employee]) -> None:
        self.employee_list = employee_list

    def calculate_avg_salary(self) -> float:
        total_salary = 0
        for employee in self.employee_list:
            total_salary += employee.salary
        return total_salary / len(self.employee_list)


employee_list = [Employee("John", 500), Employee("Jane", 600), Employee("Bob", 400)]


dataset = EmployeeDataset(employee_list)
avg_salary = dataset.calculate_avg_salary()

print(f"The average salary of the emp is ${avg_salary:.2f}")
