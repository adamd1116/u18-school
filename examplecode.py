import mysql.connector
import datetime
from guizero import *

# MySQL connection parameters
db_params = {
    "host": "localhost",
    "user": "root",
    "passwd": "",#blanked
    "database": "mydb"
}

# MySQL connection
mydb = mysql.connector.connect(**db_params)
mycursor = mydb.cursor()

# GUI setup
app = App("Silver Dawn")

# List to keep track of created input boxes
input_boxes = []

# Declare the back_button outside the function to make it accessible in both functions
back_button = None
current_form = None
insertscreen = None
table_dropdown = None
view_data_window = None

# Additional global variables for deletion functionality
delete_data_window = None
table_dropdown_for_delete = None
record_dropdown = None

# Define a mapping of table names to primary key column names
table_primary_keys = {
    "customerdetails": "CustomerID",
    "booking": "BookingID",
    "coaches": "CoachID",
    "driver": "DriverID",
    "trips": "TripID",
    "destination": "DestinationID",
}

def add_to_mysql():
    # Assuming 'current_form' holds the identifier of the current form
    global current_form

    # Define your insert queries for each form
    insert_queries = {
        "customerdetails": "INSERT INTO customerdetails (`FirstName`, `Surname`, `Email`, `AddressLine1`, `AddressLine2`, `Postcode`, `PhoneNumber`, `SpecialNotes`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        "booking": "INSERT INTO booking (`CustomerID`, `BookingDate`, `TripID`, `NumberOfPeople`, `WheelchairZones`, `SpecialRequest`, `TotalCost`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        "coaches": "INSERT INTO coach (`Registration`, `Seats`, `WheelchairZones`) VALUES (%s, %s, %s)",
        "driver": "INSERT INTO driver (`Staff`) VALUES (%s)",
        "trips": "INSERT INTO trip (`DestinationID`, `CoachID`, `DriverID`, `Cost`, `Date`) VALUES (%s, %s, %s, %s, %s)",
        "destination": "INSERT INTO destination (`TripDestination`, `TripHotel`, `Days`) VALUES (%s, %s, %s)",
    }
    # Select the correct query based on 'current_form'
    insert_query = insert_queries.get(current_form, None)
    if insert_query is None:
        print("Invalid form context or not implemented")
        return

    # Extract values from input boxes
    values = [input_box.value for input_box in input_boxes]

    # You might want to add form-specific validation here

    # Execute the query with the values
    try:
        mycursor.execute(insert_query, tuple(values))
        mydb.commit()
        print(f"Data added to MySQL for {current_form}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def show_main_view():
    # Destroy input boxes, 'Add to' buttons, and back button
    for widget in input_boxes:
        widget.destroy()
    input_boxes.clear()

    if back_button is not None:
        back_button.destroy()

    # Destroy all buttons
    for widget in insertscreen.children:
        if isinstance(widget, PushButton) and widget.text.startswith("Add to "):
            widget.destroy()

    # Unhide all widgets
    for widget in insertscreen.children:
        widget.visible = True


def insertmenu():
    global insertscreen  # Declare insertscreen as a global variable
    insertscreen = Window(app, title="Insert Menu")
    customerdetails_button = PushButton(insertscreen, text="Customer Details", command=customerdetails)
    booking_button = PushButton(insertscreen, text="Booking", command=booking)
    coaches_button = PushButton(insertscreen, text="Coaches", command=coaches)
    driver_button = PushButton(insertscreen, text="Driver", command=driver)
    trips_button = PushButton(insertscreen, text="Trips", command=trips)
    destination_button = PushButton(insertscreen, text="Destination", command=destination)


def customerdetails():
    global current_form, back_button  # Declare back_button as a global variable
    current_form = "customerdetails"

    # Hide existing widgets
    for widget in insertscreen.children:
        widget.visible = False

    # Create input boxes for FirstName, LastName, and Address
    column_names = ["FirstName", "Surname", "Email", "AddressLine1", "AddressLine2", "Postcode", "PhoneNumber", "SpecialNotes"]
    for column_name in column_names:
        input_box = TextBox(insertscreen, width=30, text=column_name, visible=True)
        input_boxes.append(input_box)

    # Create a button to add information to MySQL and back button
    add_button = PushButton(insertscreen, text="Add to Customer Details", command=add_to_mysql)
    back_button = PushButton(insertscreen, text="Back", command=show_main_view)

       
def booking():
    global current_form, back_button  # Declare back_button as a global variable
    current_form = "booking"

    # Hide existing widgets
    for widget in insertscreen.children:
        widget.visible = False

    # Create input boxes
    column_names = ["CustomerID", "BookingDate", "TripID", "NumberOfPeople", "WheelchairZones", "SpecialRequest", "TotalCost"]
    for column_name in column_names:
        input_box = TextBox(insertscreen, width=30, text=column_name, visible=True)
        input_boxes.append(input_box)

    # Create a button to add information to MySQL
    add_button = PushButton(insertscreen, text="Add to Booking", command=add_to_mysql)
    back_button = PushButton(insertscreen, text="Back", command=show_main_view)

def coaches():
    global current_form, back_button  # Declare back_button as a global variable
    current_form = "coaches"

    # Hide existing widgets
    for widget in insertscreen.children:
        widget.visible = False
       
    # Create input boxes
    column_names = ["Registration", "Seats", "WheelchairZones"]
    for column_name in column_names:
        input_box = TextBox(insertscreen, width=30, text=column_name, visible=True)
        input_boxes.append(input_box)

    # Create a button to add information to MySQL
    add_button = PushButton(insertscreen, text="Add to Coaches", command=add_to_mysql)
    back_button = PushButton(insertscreen, text="Back", command=show_main_view)

def driver():
    global current_form, back_button  # Declare back_button as a global variable
    current_form = "driver"

    # Hide existing widgets
    for widget in insertscreen.children:
        widget.visible = False

    # Create input boxes
    column_names = ["Driver"]
    for column_name in column_names:
        input_box = TextBox(insertscreen, width=30, text=column_name, visible=True)
        input_boxes.append(input_box)

    # Create a button to add information to MySQL
    add_button = PushButton(insertscreen, text="Add to Driver", command=add_to_mysql)
    back_button = PushButton(insertscreen, text="Back", command=show_main_view)

def trips():
    global current_form, back_button  # Declare back_button as a global variable
    current_form = "trips"

    # Hide existing widgets
    for widget in insertscreen.children:
        widget.visible = False

    # Create input boxes
    column_names = ["DestinationID", "CoachID", "DriverID", "Cost", "Date"]
    for column_name in column_names:
        input_box = TextBox(insertscreen, width=30, text=column_name, visible=True)
        input_boxes.append(input_box)

    # Create a button to add information to MySQL
    add_button = PushButton(insertscreen, text="Add to Trips", command=add_to_mysql)
    back_button = PushButton(insertscreen, text="Back", command=show_main_view)

def destination():
    global current_form, back_button  # Declare back_button as a global variable
    current_form = "destination"

    # Hide existing widgets
    for widget in insertscreen.children:
        widget.visible = False

    # Create input boxes
    column_names = ["TripDestination", "TripHotel", "Days"]
    for column_name in column_names:
        input_box = TextBox(insertscreen, width=30, text=column_name, visible=True)
        input_boxes.append(input_box)

    # Create a button to add information to MySQL
    add_button = PushButton(insertscreen, text="Add to Destinations", command=add_to_mysql)
    back_button = PushButton(insertscreen, text="Back", command=show_main_view)

# Function to view data from the database

def seedata():
    global table_dropdown, view_data_window
    view_data_window = Window(app, title="View Data")
    Text(view_data_window, text="Select a table to view:", size=12)
    tables = ["customerdetails", "booking", "driver", "coach", "trip", "destination"]
    table_dropdown = Combo(view_data_window, options=tables, selected=tables[0], width=20)
    view_button = PushButton(view_data_window, text="View Data", command=view_table_data)

def view_table_data():
    selected_table = table_dropdown.value
    query = f"SELECT * FROM {selected_table}"
    try:
        mycursor.execute(query)
        results = mycursor.fetchall()
        column_names = [i[0] for i in mycursor.description]
        display_results_window(selected_table, column_names, results)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def display_results_window(table_name, columns, data):
    results_window = Window(app, title=f"Data from {table_name}")
    Text(results_window, text=f"Data from {table_name}:", size=14, font="Bold")
    column_headers = " | ".join(columns)
    Text(results_window, text=column_headers, size=12, font="Bold")
    for row in data:
        row_data = " | ".join([str(item) for item in row])
        Text(results_window, text=row_data)

# Functions for data deletion functionality

def fetch_records_for_table(table_name):
    if table_name == "customerdetails":
        query = "SELECT CustomerID, CONCAT_WS(' - ', FirstName, Surname, Email, AddressLine1, AddressLine2, City, Postcode, PhoneNumber, SpecialNotes) AS RecordDisplay FROM customerdetails"
    elif table_name == "booking":
        query = "SELECT BookingID, CONCAT_WS(' - ', CustomerID, BookingDate, TripID, NumberOfPeople, WheelchairZones, SpecialRequest, TotalCost) AS RecordDisplay FROM booking"
    elif table_name == "coach":
        query = "SELECT CoachID, CONCAT_WS(' - ', Registration, Seats, WheelchairZones) AS RecordDisplay FROM coach"
    elif table_name == "driver":
        query = "SELECT DriverID, CONCAT(' - ', Driver) AS RecordDisplay FROM driver"
    elif table_name == "trip":
        query = "SELECT TripID, CONCAT_WS(' - ', DestinationID, CoachID, DriverID, Cost, Date) AS RecordDisplay FROM trip"
    elif table_name == "destination":
        query = "SELECT DestinationID, CONCAT_WS(' - ', TripDestination, TripHotel, Days) AS RecordDisplay FROM destination"
    else:
        # Fallback for unhandled tables, adjust as necessary
        query = f"SELECT id, CONCAT_WS(' - ', id, 'Fallback Display') FROM {table_name}"
    try:
        mycursor.execute(query)
        records = mycursor.fetchall()
        return [f"{record[0]}: {record[1]}" for record in records]  # Format: "ID: Concatenated fields"
    except mysql.connector.Error as err:
        print(f"Error fetching records for table {table_name}: {err}")
        return []

def update_record_dropdown():
    selected_table = table_dropdown_for_delete.value
    records = fetch_records_for_table(selected_table)
    record_dropdown.clear()
    record_dropdown.append("Select a record")  # Reset the dropdown with a default option
    for record in records:
        record_dropdown.append(record)  # Add each record individually
    if records:
        record_dropdown.value = records[0]  # Optionally set the first record as the selected value

def delete_record():
    selected_item = record_dropdown.value
    selected_record_id = selected_item.split(":")[0]  # Extract the ID part before the colon
    selected_table = table_dropdown_for_delete.value
    
    if selected_table == "customerdetails":
        primary_key_column = "CustomerID"
    elif selected_table == "booking":
        primary_key_column = "BookingID"
    elif selected_table == "coach":
        primary_key_column = "CoachID"
    elif selected_table == "driver":
        primary_key_column = "DriverID"
    elif selected_table == "trip":
        primary_key_column = "TripID"
    elif selected_table == "destination":
        primary_key_column = "DestinationID"
    # Add conditions for other tables as necessary
    
    if selected_record_id:
        query = f"DELETE FROM {selected_table} WHERE {primary_key_column} = %s"
        try:
            mycursor.execute(query, (selected_record_id,))
            mydb.commit()
            print(f"Record with {primary_key_column} {selected_record_id} deleted from {selected_table}.")
            update_record_dropdown()  # Refresh the records dropdown
        except mysql.connector.Error as err:
            print(f"Error deleting record from {selected_table}: {err}")
    else:
        print("Please select a valid record to delete.")
        
def deletedata():
    global delete_data_window, table_dropdown_for_delete, record_dropdown
    delete_data_window = Window(app, title="Delete Data")
    Text(delete_data_window, text="Select a table:", size=12)
    tables = ["customerdetails", "booking", "coach", "driver", "trip", "destination"]
    table_dropdown_for_delete = Combo(delete_data_window, options=tables, selected=tables[0], width=20, command=lambda: update_record_dropdown())
    
    Text(delete_data_window, text="Select a record:", size=12)
    record_dropdown = Combo(delete_data_window, options=["Select a table first"], width=20)
    delete_button = PushButton(delete_data_window, text="Delete Record", command=delete_record)
    
    update_record_dropdown()  # Initialize records for the initially selected table

# Functions for specific trip search functionality
def specifictripdata():
    global specific_trip_window, destination_dropdown_specific, date_dropdown_specific
    specific_trip_window = Window(app, title="Search for Specific Trip")
    Text(specific_trip_window, text="Select Destination:")

    # Initialize destination dropdown with TripDestination names
    destination_dropdown_specific = Combo(specific_trip_window, command=update_date_dropdown_specific)
    mycursor.execute("SELECT DISTINCT TripDestination FROM destination")
    destinations = mycursor.fetchall()
    for destination in destinations:
        destination_dropdown_specific.append(destination[0])  # Use TripDestination directly

    Text(specific_trip_window, text="Select Date:")
    date_dropdown_specific = Combo(specific_trip_window)

    fetch_customers_button = PushButton(specific_trip_window, text="Fetch Customers", command=fetch_customers_specific)

def update_date_dropdown_specific(selected_destination):
    date_dropdown_specific.clear()
    query = """
    SELECT DISTINCT trip.Date 
    FROM trip
    JOIN destination ON trip.DestinationID = destination.DestinationID
    WHERE destination.TripDestination = %s
    """
    mycursor.execute(query, (selected_destination,))
    dates = mycursor.fetchall()
    for date in dates:
        date_dropdown_specific.append(str(date[0]))

def fetch_customers_specific():
    selected_date = date_dropdown_specific.value
    selected_destination = destination_dropdown_specific.value
    query = """
    SELECT customerdetails.FirstName, customerdetails.Surname, customerdetails.Email, customerdetails.AddressLine1,
           customerdetails.AddressLine2, customerdetails.City, customerdetails.Postcode, customerdetails.PhoneNumber, customerdetails.SpecialNotes
    FROM customerdetails
    JOIN booking ON customerdetails.CustomerID = booking.CustomerID
    JOIN trip ON booking.TripID = trip.TripID
    JOIN destination ON trip.DestinationID = destination.DestinationID
    WHERE destination.TripDestination = %s AND trip.Date = %s
    """
    mycursor.execute(query, (selected_destination, selected_date))
    customers = mycursor.fetchall()
    display_customers_window_specific(customers)


def display_customers_window_specific(customers):
    customers_window = Window(app, title="Customers on Selected Trip")
    if not customers:
        Text(customers_window, text="No customers found for this trip.")
    else:
        for customer in customers:
            customer_info = f"Name: {customer[0]} {customer[1]}, Email: {customer[2]}, Address: {customer[3]} {customer[4]}, {customer[5]}, {customer[6]}, Phone: {customer[7]}, Notes: {customer[8]}"
            Text(customers_window, text=customer_info)

# Function to fetch trips that are scheduled for a future date
def availabletrips():
    # Get the current date using datetime module
    today_date = datetime.datetime.now().date()
    
    # SQL query to select trips with dates greater than today's date
    query = """
    SELECT trip.TripID, destination.TripDestination, trip.Date 
    FROM trip 
    JOIN destination ON trip.DestinationID = destination.DestinationID 
    WHERE trip.Date > %s 
    ORDER BY trip.Date ASC
    """   
    # Execute the query with today's date as parameter to fetch future trips
    mycursor.execute(query, (today_date,))
    trips = mycursor.fetchall()
    
    # Call function to display the fetched trips in a new window
    display_available_trips_window(trips)

# Function to display the future trips in a GUI window
def display_available_trips_window(trips):
    # Create a new window titled 'Available Trips'
    available_trips_window = Window(app, title="Available Trips")
    
    # Check if there are no future trips
    if not trips:
        Text(available_trips_window, text="No available trips.")
    else:
        for trip in trips:
            # Format trip information into a readable string
            trip_info = f"Trip ID: {trip[0]}, Destination: {trip[1]}, Date: {trip[2]}"
            Text(available_trips_window, text=trip_info)
            
def postcodeadresses():
    # Create a window for postcode area lookup
    postcode_window = Window(app, title="Postcode Area Lookup")
    Text(postcode_window, text="Select a postcode area:")

    # Dropdown for user to select the first three letters of a postcode area
    postcode_area_dropdown = Combo(postcode_window, width=10)
    
    # Fetch unique first three letters of postcodes from the database and populate the dropdown
    query = "SELECT DISTINCT LEFT(Postcode, 3) AS PostcodeArea FROM customerdetails ORDER BY PostcodeArea ASC"
    mycursor.execute(query)
    postcode_areas = mycursor.fetchall()
    for area in postcode_areas:
        postcode_area_dropdown.append(area[0])  # Add each unique postcode area to the dropdown

    # Button to fetch and display addresses based on the selected postcode area
    fetch_addresses_button = PushButton(postcode_window, text="Find Addresses", command=lambda: fetch_addresses(postcode_area_dropdown.value))

def fetch_addresses(postcode_area):
    # SQL query to find addresses with the selected postcode area
    # Now includes fetching FirstName and LastName
    query = """
    SELECT FirstName, Surname, AddressLine1, AddressLine2 FROM customerdetails
    WHERE Postcode LIKE %s
    """
    like_pattern = f"{postcode_area}%"
    mycursor.execute(query, (like_pattern,))
    addresses = mycursor.fetchall()
    display_addresses_window(addresses)

def display_addresses_window(addresses):
    # Create a window to display matching addresses along with the person's name
    addresses_window = Window(app, title="Matching Addresses")
    if not addresses:
        Text(addresses_window, text="No addresses found for this postcode area.")
    else:
        for address in addresses:
            address_info = f"Name: {address[0]} {address[1]}, Address Line 1: {address[2]}, Address Line 2: {address[3]}"
            Text(addresses_window, text=address_info)

def incomedata():
    global income_window, trip_dropdown_for_income, income_display
    income_window = Window(app, title="Calculate Income")
    Text(income_window, text="Select a Trip:")

    trips = fetch_trips_for_income()
    trip_dropdown_for_income = Combo(income_window, options=trips, command=on_trip_selected_for_income, width=50)
    income_display = Text(income_window, text="Select a trip to see the income")

def fetch_trips_for_income():
    query = """
    SELECT t.TripID, d.TripDestination, t.Date
    FROM trip t
    JOIN destination d ON t.DestinationID = d.DestinationID
    ORDER BY t.TripID
    """
    mycursor.execute(query)
    trips = mycursor.fetchall()
    formatted_trips = [(f"{trip[0]} - {trip[1]} ({trip[2]})") for trip in trips]
    return formatted_trips

def on_trip_selected_for_income(selected_trip_info):
    # Extract TripID from the selected_trip_info
    selected_trip_id = selected_trip_info

    # Query to calculate total income, ensuring all scenarios are considered
    query = """
    SELECT t.TripID, IFNULL(SUM((b.NumberOfPeople + IFNULL(b.WheelchairZones, 0)) * t.Cost), 0) AS TotalIncome
    FROM trip t
    LEFT JOIN booking b ON b.TripID = t.TripID
    WHERE t.TripID = %s
    GROUP BY t.TripID
    """
    mycursor.execute(query, (selected_trip_id,))
    result = mycursor.fetchone()
    total_income = result[1] if result else 0  # Fetch TotalIncome from the result
    income_display.value = f"Total Income for Trip ID {selected_trip_id}: £{total_income}"

# Create a button to trigger the input boxes
insertdata_button = PushButton(app, text="Insert data into database", command=insertmenu)
seedata_button = PushButton(app, text="See data in database", command=seedata)
deletedata_button = PushButton(app, text="Delete data in database", command=deletedata)
specifictripdata_button = PushButton(app, text="Customer data on a specific trip", command=specifictripdata)
availabletrips_button = PushButton(app, text="Trips available for booking", command=availabletrips)
postcodeadresses_button = PushButton(app, text="Show addresses for customers in a postcode", command=postcodeadresses)
incomedata_button = PushButton(app, text="Calculate income of a specific trip", command=incomedata)
# Display the GUI window
app.display()

# Close the connection when the window is closed
mydb.close()
