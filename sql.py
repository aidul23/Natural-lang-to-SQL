import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## create cursor to insert, retrive record and create table
cursor = connection.cursor()

## create table
table = """
Create table STUDENT(NAME VARCHAR(20), CLASS VARCHAR(20), SECTION VARCHAR(20), MARKS INT);
"""

cursor.execute(table)

## Insert record
cursor.execute('''Insert Into STUDENT values('Aidul','Software','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sakib','Software','B',100)''')
cursor.execute('''Insert Into STUDENT values('Fahim','Software','A',86)''')
cursor.execute('''Insert Into STUDENT values('Sama','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Niloy','Devops','A',35)''')

## display records
print("Inserted recors are:")
data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()