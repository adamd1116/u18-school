import mysql.connector

with open('password.txt', 'r') as f:
    dbpassword = f.read()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=dbpassword,
    database="mydb"
)

dbcursor = mydb.cursor()

insert_statement = "INSERT INTO customer (firstName,lastName,email,phoneNumber,addressLine1,addressLine2,city,postcode,specialNotes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

insert_values = ("Ronnie", "Coleman", "ronniecoleman@gmail.com", "0763726993", "Apartment 1","123 Cherry Avenue", "London", "E9 HL7", "Needs two seats due to massive lats")

dbcursor.execute(insert_statement,insert_values)
mydb.commit()

dbcursor.close()
mydb.close()