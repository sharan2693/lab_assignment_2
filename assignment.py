class Employee:
    def _init_(self, emp_id, name, age, sal):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.sal= sal

    def display(self):
        print(f"{self.emp_id} {self.name} {self.age} {self.sal}")

def sort_emp(employees, key):
    return sorted(employees, key=lambda emp: getattr(emp, key))

def main():
    # Creating Employee objects
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    while True:
        print("\nSort by: \n1. Age\n2. Name\n3. Salary\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sorted_employees = sort_emp(employees, 'age')
        elif choice == '2':
            sorted_employees = sort_emp(employees, 'name')
        elif choice == '3':
            sorted_employees = sort_emp(employees, 'salary')
        elif choice == '4':
            break
        else:
            print("Invalid choice. Enter a valid option.")
            continue

        print("\nSorted Employee Data:\n")
        for emp in sorted_employees:
            emp.display()

if _name_ == "_main_":
    main()