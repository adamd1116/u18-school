import mysql.connector



mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword123",
    database="mydb"
)

dbcursor = mydb.cursor()

#insert_statement = "INSERT INTO customer (firstName,lastName,email,phoneNumber,addressLine1,addressLine2,city,postcode,specialNotes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#insert_values = ("Ronnie", "Coleman", "ronniecoleman@gmail.com", "0763726993", "Apartment 1","123 Cherry Avenue", "London", "E9 HL7", "Needs two seats due to massive lats")

#dbcursor.execute(insert_statement,insert_values)

with dbcursor as cursor:
    result = cursor.execute("SELECT * FROM booking")
    rows = cursor.fetchall()
    for rows in rows:
        print(rows)
#mydb.commit() - Only needed for insert

dbcursor.close()
mydb.close()