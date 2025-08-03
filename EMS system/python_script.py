# Step 1: Plan the Data Storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Asha', 'age': 30, 'department': 'IT', 'salary': 70000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'Sales', 'salary': 45000},
    104 : {'name': 'khushi', 'age': 22, 'department': 'IT', 'salary': 65000}
}

#Step 2 - Define the Menu System

def main_Menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. search for a Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()

        elif choice == '2':
            view_employees()

        elif choice == '3':
            search_employee()

        elif choice== '4':
            print("Thank You for using EMS! ")
        else:
            print("Invalid choice")

# Step 3 - Add Employee Functionality

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        print("ID Already Exists")
        return
    
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter department: ")
    salary = float(input("salary: "))

    employees[emp_id] = {
        'name' : name,
        'age' : age,
        'department' : department,
        'salary' : salary
    }
    print("Employee Added Succesfully.")

#Step 4 - View All Employees

def view_employees():
    if not employees:
        print("No Employees available")
        return
    print(f"{'ID': <10} {'Name':<20} {'Age': <10} {'Department':<15}{'Salary': <10}")
    for emp_id , info in employees.items():
        print(f"{emp_id:<10}{info['name']: <20}{info['age']:<10}{info['department']:<15}{info['salary']: <10}")

def search_employee():
    emp_id = int(input("Enter employee ID: "))
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"Name: {emp['name']}")  
        print(f"Age: {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: {emp['salary']}")
    else:
        print("Employee Not Found.")

if __name__ == "__main__":
    main_Menu()
