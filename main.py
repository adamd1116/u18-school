#WORK ON NEW INPUT FORMS

#TODO:

#Input form for new customer details - Done
#Input form for new bookings
#Input form for new destination
#Input form for new trip

#Queries

from guizero import *
import mysql.connector
from datetime import *

BG_COLOUR = "#fd474a"

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
        app.info("Alert","Data inputted succesfully, application might need to be restarted for changes to be recognised")
    except Exception as e:
        app.error("Error!", e)
        print(e)      
      
def close_sql():
    dbcursor.close()
    mydb.close()
    print("SQL closed")
    app.destroy()
    
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

################## DESTINATION INPUT WINDOW START ##################

destination_window = Window(app, title = "Add a new destination", height=500, width=600)
destination_window.bg = BG_COLOUR
destination_window_title = Box(destination_window,width=600,height=200,align="top",border=True)
destination_window_message = Text(destination_window_title, text="Add a new\ndestination",size=25)
destination_input_box = Box(destination_window,width=600,height=200,align="top",border=True)

destination_name = TextBox(destination_input_box,text="Enter: Destination Name")
hotel_name = TextBox(destination_input_box, text="Enter: Hotel Name (optional)")
dest_input_forms = [destination_name,hotel_name]
for i in dest_input_forms:
    i.bg = "white"
    i.width=50
    
destination_name.when_key_pressed = lambda: clear_text(destination_name)
hotel_name.when_key_pressed = lambda: clear_text(hotel_name)

dbcursor = mydb.cursor()

def insert_destination(dest,hotel):
    query = "INSERT INTO destination (destName, hotelName) VALUES (%s,%s)"
    values = (dest,hotel)
    sql_insert(query,values)

submit_destination_data = PushButton(destination_input_box,text="Submit Destination",command = lambda: insert_destination(destination_name.value,hotel_name.value))

################## DESTINATION INPUT WINDOW END ##################

################## TRIP INPUT WINDOW START ##################

trip_window = Window(app, title = "Add a new trip", height=500, width=600)
trip_window.bg = BG_COLOUR
trip_window_title = Box(trip_window,width=600,height=200,align="top",border=True)
trip_window_message = Text(trip_window_title, text="Add a new trip",size=25)
trip_input_box = Box(trip_window,width=600,height=400,border=True, align="top")

def select_all_from_table(table_name,output_list): # Used when wanting to display all data for user selection
    
    dbcursor = mydb.cursor()
    
    with dbcursor as dbc:
        dbc.execute(f"SELECT * FROM {table_name}")
        rows = dbc.fetchall()
        for r in rows:
            output_list.append(r)
            
all_destinations = []      
all_coaches = []
all_drivers = []
select_all_from_table("destination", all_destinations)
select_all_from_table("coach", all_coaches)
select_all_from_table("driver", all_drivers)

def get_dest(selected_value):
    global selected_destination
    selected_destination = selected_value
def get_coach(selected_value):
    global selected_coach
    selected_coach = selected_value
def get_driver(selected_value):
    global selected_driver
    selected_driver = selected_value

def make_lists_look_nicer(unsorted_original, first_value):

    unsorted_2 = []
    final_sorted = [first_value]

    for i in unsorted_original:
        temp = []
        for column in i:
            temp.append(str(column))
        unsorted_2.append(temp)
        
    for i in unsorted_2:
        temp = " - ".join(i)
        final_sorted.append(temp)
        
    return final_sorted

all_destinations_sorted = make_lists_look_nicer(all_destinations, "ID - Destination - Hotel")
all_coaches_sorted = make_lists_look_nicer(all_coaches, "ID - Registration - Seats")
all_drivers_sorted = make_lists_look_nicer(all_drivers, "ID - First Name - Last Name")
all_sorted_lists = [all_destinations_sorted,all_coaches_sorted,all_drivers_sorted]

def insert_trip(dest,cost,date,duration,coach,driver, sorted_lists):
    destination = sorted_lists[0].index(dest)
    total_cost = cost
    final_date = date
    total_duration = duration
    selected_coach = sorted_lists[1].index(coach)
    selected_driver = sorted_lists[2].index(driver)

    query = "INSERT INTO trip (destination_id,personCost,startDate,duration,coach_id,driver_id) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (destination,int(total_cost),final_date,int(total_duration),selected_coach,selected_driver)
    sql_insert(query,values)

select_dest = Text(trip_input_box,text="Select Destination v")
dest_dropdown = Combo(trip_input_box,options=all_destinations_sorted,width=60,command=get_dest)
input_cost = TextBox(trip_input_box,text="Enter: Cost for the trip (Whole number)")
input_start_date = TextBox(trip_input_box,text="Enter: Date for the trip (YYYY-MM-DD)")
input_duration = TextBox(trip_input_box,text="Enter: Duration of trip (days)")
trip_inputs = [input_cost,input_start_date,input_duration]
for i in trip_inputs:
    i.bg="White"
    i.width=50
input_cost.when_key_pressed = lambda: clear_text(input_cost)
input_start_date.when_key_pressed = lambda: clear_text(input_start_date)
input_duration.when_key_pressed = lambda: clear_text(input_duration)
select_coach = Text(trip_input_box,text="Select Coach v")
coach_dropdown = Combo(trip_input_box,options=all_coaches_sorted,width=60,command=get_coach)
select_driver = Text(trip_input_box,text="Select Driver v")
driver_dropdown = Combo(trip_input_box,options=all_drivers_sorted,width=60,command=get_driver)
confirm_button2 = PushButton(trip_input_box,text="Submit Trip",command = lambda: insert_trip(selected_destination,input_cost.value,input_start_date.value,input_duration.value,selected_coach,selected_driver,all_sorted_lists))

################## TRIP INPUT WINDOW END ##################

################## BOOKING INPUT WINDOW START ##################

booking_window = Window(app, title = "Add a new booking", height=500, width=600)
booking_window.bg = BG_COLOUR
booking_window_title = Box(booking_window,width=600,height=100,align="top",border=True)
booking_window_message = Text(booking_window_title, text="Add a new booking",size=25)
booking_input_form = Box(booking_window,width=600,height=300,align="left",border=True)

dbcursor = mydb.cursor()

#Customer drop down
#Trip drop down
#Input number of seats
#insert all including current date

all_customers = []
trip_stuff = []
dest_id = []

customer_query = "SELECT customer_id, firstName, surname, email FROM customer"
dbcursor.execute(customer_query)
cust_data = dbcursor.fetchall()
for row in cust_data:
    all_customers.append(row)
    
dest_query = "SELECT * FROM destination"
dbcursor.execute(dest_query)
dest_data = dbcursor.fetchall()
for row in dest_data:
    dest_id.append(row)

trip_query = "SELECT trip_id, destination_id, personCost, startDate, duration FROM trip"
dbcursor.execute(trip_query)
trip_data = dbcursor.fetchall()
for row in trip_data:
    trip_stuff.append(row)
    
nice_looking_trip_data = []

for x in trip_stuff:
    temptemp = []
    temptemp.append(x[0])
    for i in dest_id:
        if i[0] == x[1]:
            temptemp.append(i[1])
            if i[2] == '':
                temptemp.append('No Hotel')
            else:
                temptemp.append(i[2])
    temptemp.append(x[2])
    temptemp.append(x[3])
    temptemp.append(x[4])
    nice_looking_trip_data.append(temptemp)
        
all_customers_sorted = make_lists_look_nicer(all_customers,"ID - First Name - Surname - Email")
all_trips_sorted = make_lists_look_nicer(nice_looking_trip_data,"ID - Destination - Hotel - Cost - Date - Duration")

sorted_booking_list = [all_customers_sorted,all_trips_sorted]

def get_cust(selected_value):
    global selected_cust
    selected_cust = selected_value

def get_trip(selected_value):
    global selected_trip
    selected_trip = selected_value
    
def insert_booking(cust,trip,seat):
    customer = sorted_booking_list[0].index(cust)
    trips = sorted_booking_list[1].index(trip)
    number_seats = seat
    
    query = "INSERT INTO booking (customer_id,trip_id,seatNumber,bookingDate) VALUES (%s,%s,%s,%s)"
    values = (customer,trips,int(number_seats),date.today())
    sql_insert(query,values)

select_cust = Text(booking_input_form,text="Select customer for booking v")
cust_dropdown = Combo(booking_input_form,options=all_customers_sorted,width=80,command=get_cust)
select_trip = Text(booking_input_form, text="Select trip for booking v")
trip_dropdown = Combo(booking_input_form, options=all_trips_sorted,width=80,command=get_trip)
number_of_seats = TextBox(booking_input_form, text="Enter: number of seats for booking")
number_of_seats.bg = "white"
number_of_seats.width = 60
number_of_seats.when_key_pressed = lambda: clear_text(number_of_seats)
submit_booking_data = PushButton(booking_input_form,text="Submit Booking",command=lambda: insert_booking(selected_cust,selected_trip,number_of_seats.value))


#customer_dropdown = Combo(booking_input_form)

################## BOOKING INPUT WINDOW END ################## ONCE DONE, DO QUERIES

customer_details_window.hide()
booking_window.hide()
destination_window.hide()
trip_window.hide()

"""
title_box = Box(app,grid=[0,0],width=550,height=100,align="top",border=True)

message = Text(title_box, text="Silver Dawn Coaches\nDigital Booking System")
message.text_size = 30
message.font =  "Futura"    
"""

logo = Picture(app, image = r'SDlogoResized.png',grid=[2,0])

input_form_box = Box(app,width=200,height=177,align="left",border=False,layout="grid",grid=[0,0])

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

app.when_closed = lambda: close_sql()
app.display()