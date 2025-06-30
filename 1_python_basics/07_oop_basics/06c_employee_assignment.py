# 👨‍💼 Employee Class with total count tracking

class Employee:
    total_employees = 0  # ✅ Class variable

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.total_employees += 1  # 📈 Count each new employee

    def display_info(self):
        print(f" ID: {self.emp_id} | Name: {self.name} | Dept: {self.department} |  Salary: {self.salary}")

    @classmethod
    def show_total(cls):
        print(f"\n📊 Total Employees: {cls.total_employees}")

# ✅ Create employee objects
emp1 = Employee(101, "Aamir", "HR", 25000)
emp2 = Employee(102, "Zoya", "Finance", 30000)
emp3 = Employee(103, "Ravi", "IT    "  , 45000)
emp4 = Employee(104, "Neha", "Marketing", 28000)
emp5 = Employee(105, "Tariq", "Oprations", 28000)

# 🔁 Display all employees
print("📋 Employee List\n" + "-"*35)
emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
emp5.display_info()
# 📊 Show total
Employee.show_total()
