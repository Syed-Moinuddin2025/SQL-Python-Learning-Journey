import pyodbc

# Step 1: Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=PythonPracticeDB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
print("✅ Connected to PythonPracticeDB successfully.")

# Step 2: Insert data into Employees
employees = [
    (205, 'Ayesha', 'Qureshi', 1, 1, '2022-02-01'),
    (206, 'Bilal', 'Raza', 2, 2, '2023-01-15'),
    (207, 'Tariq', 'Zaman', 3, 3, '2020-07-25'),
]

insert_emp = '''
    INSERT INTO Employees (EmpID, FirstName, LastName, DeptID, DesigID, JoinDate)
    VALUES (?, ?, ?, ?, ?, ?)
'''

try:
    cursor.executemany(insert_emp, employees)
    conn.commit()
    print("✅ Employees inserted successfully.")
except Exception as e:
    print("❌ Error inserting employees:", e)

# Step 3: Insert data into Salaries
salaries = [
    (205, 50000, 4000, 1500),
    (206, 47000, 3000, 1000),
    (207, 52000, 3500, 1200),
]

insert_sal = '''
    INSERT INTO Salaries (EmpID, BasicSalary, Allowance, Deductions)
    VALUES (?, ?, ?, ?)
'''

try:
    cursor.executemany(insert_sal, salaries)
    conn.commit()
    print("✅ Salaries inserted successfully.")
except Exception as e:
    print("❌ Error inserting salaries:", e)

# Step 4: Close connection
cursor.close()
conn.close()
print("✅ Connection closed.")
