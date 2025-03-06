import json
import mysql.connector

# Load database configuration from config.json
with open("config.prasad", "r") as file:
    config = json.load(file)

# Establish database connection using secure credentials
conn = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
)

cursor = conn.cursor()

# Function to add an employee
def add_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    email = input("Enter email: ")

    query = """INSERT INTO employee (name, age, department, salary, email) 
               VALUES (%s, %s, %s, %s, %s)"""
    values = (name, age, department, salary, email)

    cursor.execute(query, values)
    conn.commit()
    print("Employee added successfully!")


# Function to show all employees
def show_employees():
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()

    print("\nEmployee List:")
    print("ID | Name | Age | Department | Salary | Email")
    print("-" * 50)
    for row in rows:
        print(row)


# Function to update employee details
def update_employee():
    emp_id = input("Enter employee ID to update: ")
    new_age = input("Enter new age: ")
    new_department = input("Enter new department: ")
    new_salary = input("Enter new salary: ")
    new_email = input("Enter new email: ")

    query = """UPDATE employee 
               SET age=%s, department=%s, salary=%s, email=%s 
               WHERE id=%s"""
    values = (new_age, new_department, new_salary, new_email, emp_id)

    cursor.execute(query, values)
    conn.commit()
    print("Employee updated successfully!")


# Function to delete an employee
def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    query = "DELETE FROM employee WHERE id=%s"
    
    cursor.execute(query, (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")


# Main menu
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        show_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")

# Close the database connection before exiting
cursor.close()
conn.close()