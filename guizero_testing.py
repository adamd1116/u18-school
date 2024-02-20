#TODO:

#Input form for new customer details - In progress
#Input form for new bookings
#Input form for new destination
#Input form for new trip

#Queries

from guizero import *
import mysql.connector

BG_COLOUR = "#5373A6"

# MAKE THIS A FUNCTION TO REPEAT
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

################## CUSTOMER DETAIL INPUT WINDOW ##################

#main section of customer details window    
customer_details_window = Window(app, title = "Add a new customer", height=700, width=600,layout="grid")
customer_details_window.bg = BG_COLOUR
customer_details_window_title = Box(customer_details_window,grid=[0,0],width=600,height=80,align="top",border=True)
customer_details_window_message = Text(customer_details_window_title, text="Add a new\ncustomer record",size=25)
customer_input_form_box = Box(customer_details_window,grid=[0,1],width=600,height=50,align="left",border=True)

def address_line_2_status():
    global include_address_2 # I went through an hour of debugging before giving up and using a global variable, sorry programming gods
    include_address_2 = False
    if customer_details_window_checkbox.value == 1:
        include_address_2 = True
        print(f"address 2: {include_address_2}")
    elif customer_details_window_checkbox.value == 0:
        include_address_2 = False
        print(f"address 2: {include_address_2}")
    else:
        print("Error")
        
include_address_2 = False

#Adding boxes to allow users to input data
customer_details_window_checkbox = CheckBox(customer_input_form_box,text="Include Address Line 2?",command=address_line_2_status)
customer_input_form_cust_ID = Box(customer_details_window,grid=[0,2],width=600,height=50,align="left",border=True)
customer_input_form_first_name = Box(customer_details_window,grid=[0,3],width=600,height=50,align="left",border=True)
customer_input_form_last_name = Box(customer_details_window,grid=[0,3],width=600,height=50,align="left",border=True)
customer_input_form_email = Box(customer_details_window,grid=[0,4],width=600,height=50,align="left",border=True)
customer_input_form_phone_number = Box(customer_details_window,grid=[0,5],width=600,height=50,align="left",border=True)
customer_input_form_address_1 = Box(customer_details_window,grid=[0,6],width=600,height=50,align="left",border=True)
customer_input_form_address_2 = Box(customer_details_window,grid=[0,7],width=600,height=50,align="left",border=True)
customer_input_form_postcode = Box(customer_details_window,grid=[0,8],width=600,height=50,align="left",border=True)
customer_input_form_city = Box(customer_details_window,grid=[0,9],width=600,height=50,align="left",border=True)
customer_input_form_special_notes = Box(customer_details_window,grid=[0,10],width=600,height=50,align="left",border=True)

if customer_details_window_checkbox.value == True:
    print("True")
else:
    print("False")


def verify_address_line_2_status():
    if include_address_2 == False:
        add2_input.visible=False
    elif include_address_2 == True:
        add2_input.visible=True
        
def begin_verifying_add2(): # IF NEEDED, USE THIS AS AN OPTIMISATION
    add2_input.repeat(100, verify_address_line_2_status) # only begins repeating when customer window is opened

# Filling boxes with input forms
custID_input = Text(customer_input_form_cust_ID,text="Enter the details below for the customer.") # Only temporary, auto increment is enabled just need to confirm it works
fname_input = TextBox(customer_input_form_first_name, text="Enter: First Name")
lname_input = TextBox(customer_input_form_last_name, text="Enter: Last Name")
email_input = TextBox(customer_input_form_email,text="Enter: Email Address")
pnumber_input = TextBox(customer_input_form_phone_number, text="Enter: Phone Number. Formats: 07XXXXXXXXX / 020XXXXXXXX (Max 11 characters)")
add1_input = TextBox(customer_input_form_address_1, text="Enter: Address Line 1")
add2_input = TextBox(customer_input_form_address_2, text="Enter: Address Line 2",command=verify_address_line_2_status,visible=False)
pcode_input = TextBox(customer_input_form_postcode, text="Enter: Post Code")
city_input = TextBox(customer_input_form_city, text="Enter: City")
snotes_input = TextBox(customer_input_form_special_notes, text="Enter: Special Notes (optional, leave blank if needed)")
input_forms = [fname_input,lname_input,email_input,pnumber_input,add1_input,add2_input,snotes_input,pcode_input,city_input]

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

#too lazy to manually change all backgrounds and widths
for i in input_forms:
    if i == pnumber_input:
        i.bg = "white"
        i.width = 75
    else:
        i.bg = "white"
        i.width = 50
    
def collect_data_to_send(data):# DATA TYPE MIGHT NEED TO BE CHANGED TO TUPLE
    global collected_data
    collected_data = [] # SOME DATA TYPES LIKE ID MIGHT NEED TO BE KEPT AS AN INT
    for x in data:
        collected_data.append(x.value)
    
    print(collected_data)
    
confirm_customer_details = PushButton(customer_details_window,grid=[0,11] ,text="Add customer data",command=lambda: collect_data_to_send(input_forms) )

def validate_customer_data(data):
    global customer_data_validated
    customer_data_validated = False
    list_for_validating = []
    email_verified = False
    phone_verified = False
    empty_data_check = True
    for x in data[2]: 
        if x == '@':
            email_verified = True
    for x in data[3]:
        try:
            str(x)
            phone_verified = False
        except:
            phone_verified = True
    for x in data:
        if (x=="" or x[0:6]=="Enter") and (data.index(x)!=5 or data.index(x)!=6):
            empty_data_check = False
            
    if email_verified == False:
        customer_details_window.error("Error!", "The email you entered was invalid, please try again")
    if phone_verified == False:
        customer_details_window.error("Error!", "The phone number you entered was invalid, please try again")
    
           
    if email_verified == True and phone_verified == True and empty_data_check == True:
        customer_data_validated = True
        

        
#ONCE YOU SEND DATA TO DATABASE, DO CANCEL() METHOD TO STOP REPEAT OR MEMORY IS WASTED#

booking_window = Window(app, title = "Add a new booking", height=500, width=600)
booking_window.bg = BG_COLOUR
booking_window_title = Box(booking_window,width=600,height=100,align="top",border=True)
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
    add2_input.repeat(100, verify_address_line_2_status)
    
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