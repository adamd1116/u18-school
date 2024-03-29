#WORK ON NEW INPUT FORMS

#TODO:

#Input form for new customer details - In progress
#Input form for new bookings
#Input form for new destination
#Input form for new trip

#Queries

from guizero import *
import mysql.connector
from datetime import *

BG_COLOUR = "#5373A6"

################## SETTING UP SQL INSERT/SELECT FUNCTIONS ##################

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword123",
    database="mydb"
    )
   
app = App(title="Silver Dawn Coaches Digital Booking System", height=300, width=550,layout="grid")
app.bg = BG_COLOUR

def sql_insert(insert_statement, insert_values):
    global mydb
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="rootpassword123",
        database="mydb"
    )
    global dbcursor
    dbcursor = mydb.cursor()
    try:
        dbcursor.execute(insert_statement, insert_values)
        mydb.commit()
        print("SQL INSERT SUCCESSFUL")
    except Exception as e:
        app.error("Error!", e)
        print(e)
        
def sql_select(data_to_select,table):
    pass
      
def close_sql():
    dbcursor.close()
    mydb.close()
    
app.when_closed = lambda: close_sql()

################## SQL FUNCTIONS END ##################

################## CUSTOMER DETAIL INPUT WINDOW START ##################

# main section of customer details window    
customer_details_window = Window(app, title = "Add a new customer", height=700, width=600,layout="grid")
customer_details_window.bg = BG_COLOUR
customer_details_window_title = Box(customer_details_window,grid=[0,0],width=600,height=80,align="top",border=True)
customer_details_window_message = Text(customer_details_window_title, text="Add a new\ncustomer record",size=25)
customer_input_form_box = Box(customer_details_window,grid=[0,1],width=600,height=50,align="left",border=True)

# adding boxes to allow users to input data
customer_details_window_subhedaing = Text(customer_input_form_box,text="Please fill in the following data",align="bottom")
customer_input_form_first_name = Box(customer_details_window,grid=[0,2],width=600,height=50,align="left",border=True)
customer_input_form_last_name = Box(customer_details_window,grid=[0,3],width=600,height=50,align="left",border=True)
customer_input_form_email = Box(customer_details_window,grid=[0,4],width=600,height=50,align="left",border=True)
customer_input_form_phone_number = Box(customer_details_window,grid=[0,5],width=600,height=50,align="left",border=True)
customer_input_form_address_1 = Box(customer_details_window,grid=[0,6],width=600,height=50,align="left",border=True)
customer_input_form_address_2 = Box(customer_details_window,grid=[0,7],width=600,height=50,align="left",border=True)
customer_input_form_postcode = Box(customer_details_window,grid=[0,8],width=600,height=50,align="left",border=True)
customer_input_form_city = Box(customer_details_window,grid=[0,9],width=600,height=50,align="left",border=True)
customer_input_form_special_notes = Box(customer_details_window,grid=[0,10],width=600,height=50,align="left",border=True)

# filling boxes with input forms
fname_input = TextBox(customer_input_form_first_name, text="Enter: First Name (required)")
lname_input = TextBox(customer_input_form_last_name, text="Enter: Last Name (required)")
email_input = TextBox(customer_input_form_email,text="Enter: Email Address (required)")
pnumber_input = TextBox(customer_input_form_phone_number, text="Enter: Phone Number (required)")
add1_input = TextBox(customer_input_form_address_1, text="Enter: Address Line 1 (required)")
add2_input = TextBox(customer_input_form_address_2, text="Enter: Address Line 2 (optional)")
pcode_input = TextBox(customer_input_form_postcode, text="Enter: Post Code (required)")
city_input = TextBox(customer_input_form_city, text="Enter: City (required)")
snotes_input = TextBox(customer_input_form_special_notes, text="Enter: Special Notes (optional)")
input_forms = [fname_input,lname_input,add1_input,add2_input,pcode_input,pnumber_input,email_input,snotes_input,city_input]

def clear_text(input_field):
    if input_field.value[0:6]=="Enter:": # clears the input field when user begins to type
        input_field.value = ""
        
# lambda is used otherwise if user begins typing in one box, every other box will clear
fname_input.when_key_pressed = lambda: clear_text(fname_input)
lname_input.when_key_pressed = lambda: clear_text(lname_input)
email_input.when_key_pressed = lambda: clear_text(email_input)
pnumber_input.when_key_pressed = lambda: clear_text(pnumber_input)
add1_input.when_key_pressed = lambda: clear_text(add1_input)
add2_input.when_key_pressed = lambda: clear_text(add2_input)
pcode_input.when_key_pressed = lambda: clear_text(pcode_input)
city_input.when_key_pressed = lambda: clear_text(city_input)
snotes_input.when_key_pressed = lambda: clear_text(snotes_input)

# too lazy to manually change all backgrounds and widths
for i in input_forms:
    i.bg = "white"
    i.width = 50 

previous_customer_data = ()

# collecting, validating and inserting into DB 
def confirm_insert_customer_data(data):
    
    presence_check = True
    
    collected_data = []
    conv_list = []
    
    for x in data:
        conv_list.append(x.value)
    
    for x in data:
        temp = x.value
        if temp[0:6]=='Enter:' or temp  == '':
            if conv_list.index(temp) == 3 or conv_list.index(temp) == 7:
                collected_data.append('None')
            else:
                presence_check = False
                customer_details_window.error("Error!", "Please ensure all required fields are filled in")
        else:
            collected_data.append(temp)
    
    customer_insert_statement = "INSERT INTO customer (firstName,surname,AddressLine1,AddressLine2,Postcode,phoneNum,email,specialNeed,city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    customer_insert_values = tuple(collected_data)
    
    if presence_check == True:
        sql_insert(customer_insert_statement,customer_insert_values)

confirm_customer_details = PushButton(customer_details_window,grid=[0,11] ,text="Add customer data",command=lambda: confirm_insert_customer_data(input_forms) )

################## CUSTOMER DETAIL INPUT WINDOW END ##################

################## BOOKING INPUT WINDOW START ##################

booking_window = Window(app, title = "Add a new booking", height=500, width=600)
booking_window.bg = BG_COLOUR
booking_window_title = Box(booking_window,width=600,height=100,align="top",border=True)
booking_window_message = Text(booking_window_title, text="Add a new booking",size=25)
booking_input_form = Box(booking_window,grid=[0,1],width=600,height=50,align="left",border=True)

booking_subheading = Text(booking_window,)

################## BOOKING INPUT WINDOW END ##################

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