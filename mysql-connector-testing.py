import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword123",
    database="mydb"
)

dbcursor = mydb.cursor()

empty_data = []
new_data = []
statement_one = "SELECT customer_id FROM booking WHERE trip_id = (%s)"
statement_one_data = [8]

with dbcursor as cursor:
    result = cursor.execute(statement_one,statement_one_data)
    rows = cursor.fetchall()
    for rows in rows:
        empty_data.append(rows)
        
for x in empty_data:
    new_data.append(int(x[0]))

placeholders = ', '.join(['%s'] * len(new_data))

query = "SELECT * FROM customer WHERE customer_id IN ({})".format(placeholders)

dbcursor = mydb.cursor()
with dbcursor as cursor:
    cursor.execute(query, new_data)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

dbcursor.close()
mydb.close()

"""
with dbcursor as cursor:
    result = cursor.execute("SELECT * FROM booking")
    rows = cursor.fetchall()
    for rows in rows:
        print(rows)
"""