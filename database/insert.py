#! /usr/bin/env python3

import MySQLdb

db = MySQLdb.connect('localhost', 'root', '10169', 'TESTDB')

cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE (FIRST_NAME,
LAST_NAME, AGE, SEX)
VALUES ('Mac', 'Mohan', 20, 'M')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    db.commit()

except:
    # Rollback in case there is any error
    db.rollback()

db.close()