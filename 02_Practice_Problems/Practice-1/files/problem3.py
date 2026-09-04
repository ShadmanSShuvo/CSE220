class Employee:
    company_name = "TechCorp"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.salaries = []

    def add_salary(self, salary):
        self.salaries.append(salary)

    def average_salary(self):
        if not self.salaries:
            return 0
        return sum(self.salaries) / len(self.salaries)

    def highest_salary(self):
        if not self.salaries:
            return 0
        return max(self.salaries)

    def annual_income(self):
        return sum(self.salaries)

    def __str__(self):
        return (
            f"Employee Name : {self.name}\n"
            f"Employee ID : {self.employee_id}\n"
            f"Average Salary : {self.average_salary():.2f}\n"
            f"Highest Salary : {self.highest_salary()}\n"
            f"Annual Income : {self.annual_income()}"
        )


if __name__ == "__main__":
    import random

    random.seed(42)

    employees_data = [
        ("Alice", "E101"),
        ("Bob", "E102"),
        ("Charlie", "E103"),
        ("David", "E104"),
        ("Eva", "E105"),
    ]

    employees = []
    for name, emp_id in employees_data:
        emp = Employee(name, emp_id)
        for _ in range(12):
            emp.add_salary(random.randint(40000, 55000))
        employees.append(emp)

    for emp in employees:
        print(emp)
        print()
