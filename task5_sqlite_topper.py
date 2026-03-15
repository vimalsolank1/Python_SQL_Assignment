'''Task 5 - SQL topper in class - Write a sql code to identify the following'''

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

#---------------------------------------------------------------------------------------------------------------
#  --------------> a) The second topper in class <----------------

cursor.execute("drop TABLE IF EXISTS students")
# create table
cursor.execute("""
CREATE TABLE students (
    name TEXT,marks INTEGER
)
""")
# insert rows
cursor.execute("INSERT INTO students VALUES ('Sahil',95)")
cursor.execute("INSERT INTO students VALUES ('Kaushik',90)")
cursor.execute("INSERT INTO students VALUES ('John',89)")
cursor.execute("INSERT INTO students VALUES ('Kara',87)")
cursor.execute("INSERT INTO students VALUES ('Simpson',97)")


# sql query  The second topper in class
cursor.execute("""
SELECT name, marks FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1
""")

result = cursor.fetchone()
print(f"a) problem second topper in class {result}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----> b) The second topper in class. If 2 candidates have same marks then the one with their name first in alphabetical order is given the better(lower) rank

cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    name TEXT,
    marks INTEGER
)
""")

# insert data for question (b)
cursor.execute("INSERT INTO students VALUES ('Sahil',95)")
cursor.execute("INSERT INTO students VALUES ('Kaushik',97)")
cursor.execute("INSERT INTO students VALUES ('John',89)")
cursor.execute("INSERT INTO students VALUES ('Kara',87)")
cursor.execute("INSERT INTO students VALUES ('Simpson',97)")

cursor.execute("""
SELECT name, marks
FROM students
               
ORDER BY marks DESC, name ASC
LIMIT 1 OFFSET 1
""")

result = cursor.fetchone()
print(f"b) problem  Second topper in class {result}")


# -------------------------------------------------------------------------------------------------------------------------
# -----> c) The second topper(s) in class. If multiple candidates have same marks, they are given the same rank <-------
cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    name TEXT, marks INTEGER
)
""")

cursor.execute("INSERT INTO students VALUES ('Sahil',95)")
cursor.execute("INSERT INTO students VALUES ('Kaushik',97)")
cursor.execute("INSERT INTO students VALUES ('John',95)")
cursor.execute("INSERT INTO students VALUES ('Kara',87)")
cursor.execute("INSERT INTO students VALUES ('Simpson',97)")

cursor.execute("""
SELECT name, marks
FROM (
    SELECT name, marks,
    DENSE_RANK() OVER (ORDER BY marks DESC) AS rank  FROM students)
WHERE rank = 2
""")

result = cursor.fetchall()
lst=[]
for row in result:
    lst.append(row)

print(f"c) problem  second topper in class {lst}")