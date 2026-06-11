employees = []
def add_employee():
    try:
        emp = {}
        emp["ID"] = input("Enter employee ID: ")
        emp["name"] = input("Enter name:")
        emp["email"] = input("Enter email:")
        emp["department"] = input("Enter department:")
        emp["salary"] = float(input("Enter salary: "))
        emp["experience"] = int(input("Enter Experience (years): "))
        for e in employees:
            if e["ID"] == emp["ID"]:
                print("Employee with this ID already exists.")
                return
        employees.append(emp)
        print("Employee added successfully.")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")

def view_employees():
    if len(employees) == 0:
        print("\nNo employees to display.")
        return
    print("\nemployee Details")
    for emp in employees:
        print("--------------------------")
        print("ID           :", emp["ID"])
        print("Name         :", emp["name"])
        print("Email        :", emp["email"])
        print("Department   :", emp["department"])
        print("Salary       :", emp["salary"])
        print("Experience   :", emp["experience"], "years")

def search_employee():
    try:
        emp_id = input("Enter employee ID to search: ")
        for emp in employees:
            if emp["ID"] == emp_id:
                print("\nEmployee found:")
                print("--------------------------")
                print("ID           :", emp["ID"])
                print("Name         :", emp["name"])
                print("Email        :", emp["email"])
                print("Department   :", emp["department"])
                print("Salary       :", emp["salary"])
                print("Experience   :", emp["experience"], "years")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid ID!")

def update_employee():
    try:
        emp_id = input("Enter employee ID to update: ")
        for emp in employees:
            if emp["ID"] == emp_id:
                print("Enter New Details")
                emp["name"] = input("name:")
                emp["email"] = input("email:")
                emp["department"] = input("department:")
                emp["salary"] = float(input("salary: "))
                emp["experience"] = int(input("Experience (years): "))
                print("Employee updated successfully.")
                return
        print("Employee not found")
    except ValueError:
        print("Invalid input")
def delete_employee():
    try:
        emp_id = input("Enter employee ID to delete: ")
        for emp in employees:
            if emp["ID"] == emp_id:
                employees.remove(emp)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid ID!")

while True:
    print("\n==================")
    print("Employee Management System")
    print("==================") 
    print("1. Add Employee")
    print("2. View AllEmployees")
    print("3. Search Employee by ID")
    print("4. Update Employee Details")
    print("5. Delete Employee")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()
        elif choice == 6:
            print("Thank you for using Employee Management System!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print(" Please enter a valid number.")