import csv
import sqlite3

conn = sqlite3.connect('Python_HW_8.db')
cursor = conn.cursor()


drop_table1 = "DROP TABLE IF EXISTS project"
drop_table2 = "DROP TABLE IF EXISTS tasks"

cursor.execute(drop_table1)
cursor.execute(drop_table2)

create_table1 = '''CREATE TABLE IF NOT EXISTS project
                (
                name text PRIMARY KEY, 
                description text, 
                deadline date
                )'''

create_table2 = '''CREATE TABLE tasks
                (
                id number PRIMARY KEY, 
                priority integer, 
                details date,
                status text,
                deadline date,
                completed date,
                project text,
                FOREIGN KEY(project) REFERENCES project(name)
                )'''
                
cursor.execute(create_table1)
cursor.execute(create_table2)
        
proj = csv.reader(open('project.csv'))
for row in proj:                                                          
        cursor.executemany("INSERT INTO project VALUES (?,?,?)", proj)

tasks = csv.reader(open('tasks.csv'))
for row in tasks:                                                          
        cursor.executemany("INSERT INTO tasks VALUES (?,?,?,?,?,?,?)", tasks)

query = """SELECT t.status, t.deadline, p.name, p.description 
           FROM project p JOIN tasks t ON p.name=t.project 
           WHERE t.status='done'"""
for row in cursor.execute(query):
        print(row)

conn.commit()
cursor.close()
conn.close()
