import sqlite3

# connect to sqlite
connection = sqlite3.connect('student.db')

# create a cursor object to insert record, create table, retrieve

cursor = connection.cursor()

# create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert records
cursor.execute('''Insert Into STUDENT values("Vamsi","Gen ai","A",95)''')
cursor.execute('''Insert Into STUDENT values("Ashish","Ai & Ml","A",100)''')
cursor.execute('''Insert Into STUDENT values("Sumanth","Gen ai","A",90)''')
cursor.execute('''Insert Into STUDENT values("Josam","Gen ai","A",80)''')
cursor.execute('''Insert Into STUDENT values("Naveen","Gen ai","B",35)''')

# Dispaly all the records
print("The inserted records are...")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

# close connection
connection.commit()
connection.close()