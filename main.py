#TODO:

#Input form for new customer details - In progress
#Input form for new bookings
#Input form for new destination
#Input form for new trip

#Queries

from guizero import *
import mysql.connector

BG_COLOUR = "#5373A6"

"""
with open('password.txt', 'r') as f:
    dbpassword = f.read()

cnx = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password=dbpassword, database="mydb")

if cnx and cnx.is_connected():

    with cnx.cursor() as cursor:

        result = cursor.execute("SELECT * FROM bookings")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)

    cnx.close()

else:

    print("Could not connect")

cnx.close()
"""    
    
app = App(title="Silver Dawn Coaches Digital Booking System", height=300, width=550,layout="grid")
app.bg = BG_COLOUR
    
customer_details_window = Window(app, title = "Add a new customer", height=600, width=600,layout="grid")
customer_details_window.bg = BG_COLOUR
customer_details_window_title = Box(customer_details_window,grid=[0,0],width=600,height=80,align="top",border=True)
customer_details_window_message = Text(customer_details_window_title, text="Add a new\ncustomer record",size=25)
customer_input_form_box = Box(customer_details_window,grid=[0,1],width=600,height=50,align="left",border=True)
customer_details_window_checkbox = CheckBox(customer_input_form_box,text="Include Address Line 2?")
customer_input_form_cust_ID = Box(customer_details_window,grid=[0,2],width=600,height=50,align="left",border=True)
customer_input_form_first_name = Box(customer_details_window,grid=[0,3],width=600,height=50,align="left",border=True)
customer_input_form_last_name = Box(customer_details_window,grid=[0,3],width=600,height=50,align="left",border=True)
customer_input_form_email = Box(customer_details_window,grid=[0,4],width=600,height=50,align="left",border=True)
customer_input_form_phone_number = Box(customer_details_window,grid=[0,5],width=600,height=50,align="left",border=True)
customer_input_form_address_1 = Box(customer_details_window,grid=[0,6],width=600,height=50,align="left",border=True)


booking_window = Window(app, title = "Add a new booking", height=500, width=600,layout="grid")
booking_window.bg = BG_COLOUR
booking_window_title = Box(booking_window,grid=[0,0],width=600,height=500,align="top",border=True)
booking_window_message = Text(booking_window_title, text="Add a new booking",size=25)

destination_window = Window(app, title = "Add a new destination", height=500, width=600,layout="grid")
destination_window.bg = BG_COLOUR
destination_window_title = Box(destination_window,grid=[0,0],width=600,height=500,align="top",border=True)
destination_window_message = Text(destination_window_title, text="Add a new\ndestination",size=25)

trip_window = Window(app, title = "Add a new trip", height=500, width=600,layout="grid")
trip_window.bg = BG_COLOUR
trip_window_title = Box(trip_window,grid=[0,0],width=600,height=500,align="top",border=True)
trip_window_message = Text(trip_window_title, text="Add a new trip",size=25)

customer_details_window.hide()
booking_window.hide()
destination_window.hide()
trip_window.hide()

title_box = Box(app,grid=[0,0],width=550,height=100,align="top",border=True)

message = Text(title_box, text="Silver Dawn Coaches\nDigital Booking System")
message.text_size = 30
message.font =  "Futura"

input_form_box = Box(app,width=200,height=177,align="left",border=False,layout="grid",grid=[0,1])

def open_customer_window():
    customer_details_window.show(wait=True)
    
def open_booking_window():
    booking_window.show(wait=True)

def open_destination_window():
    destination_window.show(wait=True)

def open_trip_window():
    trip_window.show(wait=True)

new_customer_details = PushButton(input_form_box, text="Add a new customer",grid=[0,0],width="fill",command=open_customer_window)#add a function here that executes when pressed
new_booking = PushButton(input_form_box, text="Add a new booking",grid=[0,1],width="fill",command=open_booking_window)
new_destination = PushButton(input_form_box, text="Add a new destination",grid=[0,2],width="fill",command=open_destination_window)
new_trip = PushButton(input_form_box, text="Add a new trip",grid=[0,3],width="fill",command=open_trip_window)

app.display()