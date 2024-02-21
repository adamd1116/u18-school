import guizero
from guizero import *

#mysql connection
import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "silver_dawn_db"

#connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

#cursor = connection.cursor()

#creating screens
#home (main app)
home = App(title = "Silver Dawn DB Home", bg = "#FF464C")
#adding logo
silverDawnLogo = (r"C:\Users\Adam\Pictures\shaggy.jpeg")
silverDawnLogoHome = Picture(home, image = silverDawnLogo)
#welcome text
Text(home, text = "Welcome to Silver Dawn DBMS", color = "white", font = "Segoe UI", size = 20)

#view
view = Window(home, title = "View", bg = "#FF464C")
view.hide()
def showView():
    view.show(wait=True)
Picture(view, image = silverDawnLogo, align = "top")
Text(view, text = "Choose table to view", color = "white", font = "Segoe UI", size = 20)

#insert
insert = Window(home, title = "insert", bg = "#FF464C")
insert.hide()
def showinsert():
    insert.show(wait=True)
Picture(insert, image = silverDawnLogo, align = "top")

#adding buttons to home screen
viewButton = PushButton(home, text = "View", command = showView, align="left", width = "fill")
viewButton.bg = "#FFFFFF"
viewButton.font = "Segoe UI"

insertButton = PushButton(home, text = "insert", command = showinsert, align = "right", width = "fill")
insertButton.bg = "#FFFFFF"
insertButton.font = "Segoe UI"

#creating table view screens
#customers
viewCustomers = Window(home, title = "viewCustomers", bg = "#FF464C")
viewCustomers.hide()
def showViewCustomers():
    viewCustomers.show(wait=True)



#destinations
viewDestinations = Window(home, title = "viewDestinations", bg = "#FF464C")
viewDestinations.hide()
def showViewDestinations():
    viewDestinations.show(wait=True)

#trips
viewTrips = Window(home, title = "viewTrips", bg = "#FF464C")
viewTrips.hide()
def showViewTrips():
    viewTrips.show(wait=True)

#bookings
viewBookings = Window(home, title = "viewBookings", bg = "#FF464C")
viewBookings.hide()
def showViewBookings():
    viewBookings.show(wait=True)

#adding buttons to view screen for each table
viewCustomersButton = PushButton(view, text = "Customers", command = showViewCustomers, align = "left", width= "fill")
viewCustomersButton.bg = "white"
viewCustomersButton.text_color = "#FF464C"
viewDestinationsButton = PushButton(view, text = "Destinations", command = showViewDestinations, align = "right", width= "fill")
viewDestinationsButton.bg = "white"
viewDestinationsButton.text_color = "#FF464C"
viewTripsButton = PushButton(view, text = "Trips", command = showViewTrips, align = "right", width= "fill")
viewTripsButton.bg = "white"
viewTripsButton.text_color = "#FF464C"
viewBookingsButton = PushButton(view, text = "Bookings", command = showViewBookings, align = "right", width= "fill")
viewBookingsButton.bg = "white"
viewBookingsButton.text_color = "#FF464C"

#back button
(PushButton(view, command = view.hide, text = "Back", align = "bottom")).text_color = "#FFFFFF"

#creating table inserting screens
#coaches
insertCoaches = Window(home, title = "insertCoaches", bg = "#FF464C")
insertCoaches.hide()
def showinsertCoaches():
    insertCoaches.show(wait=True)

#title for inserting coaches
Text(insertCoaches, align ="top", text = "insert Coaches", color = "white", font = "Segoe UI", size = 20)

#adding text boxes to enter coach details into
coachIDTextBox = TextBox(insertCoaches, align = "top", width = "fill", text = "Coach License ID")
coachIDTextBox.bg = "#FFFFFF"
coachSeatsTextBox = TextBox(insertCoaches, align = "top", width = "fill", text = "Seats number")
coachSeatsTextBox.bg = "#FFFFFF"

#function to add value from the text box into the drivers table
def addCoach():
    if (coachIDTextBox.value != "") and (coachSeatsTextBox.value != "") and ((coachSeatsTextBox.value).isnumeric):
        #cursor.execute(f"INSERT INTO coaches (CoachID, Seats) VALUES ('{coachIDTextBox.value}', {coachSeatsTextBox.value});")
        insertCoachesFeedback = Text(insertCoaches, text = "Success")
    else:
        insertCoachesFeedback = Text(insertCoaches, text = (f"No null values\nMySQL Error Code: {str(mysql.connector.Error)}"))
    #connection.commit()

#adding button to perform function
insertCoachesCommitButton = PushButton(insertCoaches, command = addCoach, text = "COMMIT")
insertCoachesCommitButton.bg = "#FFFFFF"

#back button
(PushButton(insertCoaches, command = insertCoaches.hide, text = "Back", align = "bottom")).text_color = "#FFFFFF"

#drivers
insertDrivers = Window(home, title = "insertDrivers", bg = "#FF464C")
insertDrivers.hide()
def showinsertDrivers():
    insertDrivers.show(wait=True)

#title for inserting drviers
Text(insertDrivers, align ="top", text = "insert Drivers", color = "white", font = "Segoe UI", size = 20)

#adding text box to enter driver name into
driverTextBox = TextBox(insertDrivers, align = "top", width = "fill", text = "Driver Name")
driverTextBox.bg = "#FFFFFF"

#function to add value from the text box into the drivers table
def addDriver():
    if driverTextBox.value != "":
        #cursor.execute(f"INSERT INTO drivers (Driver) VALUES ('{driverTextBox.value}');")
        insertDriversFeedback = Text(insertCoaches, text = "Success")
    else:
        insertDriversFeedback = Text(insertDrivers, text = (f"No null values\nMySQL Error Code: {str(mysql.connector.Error)}"))
    #connection.commit()

#adding button to perform function
insertDriversCommitButton = PushButton(insertDrivers, command = addDriver, text = "COMMIT")
insertDriversCommitButton.bg = "#FFFFFF"

#back button
(PushButton(insertDrivers, command = insertDrivers.hide, text = "Back", align = "bottom")).text_color = "#FFFFFF"

#customers
insertCustomers = Window(home, title = "insertCustomers", bg = "#FF464C")
insertCustomers.hide()
def showinsertCustomers():
    insertCustomers.show(wait=True)

#title for inserting drviers
Text(insertCustomers, align ="top", text = "insert Customers", color = "white", font = "Segoe UI", size = 20)

#adding text boxes to enter customer details into
customerFirstNameTextBox = TextBox(insertCustomers, width = "fill", text = "Customer First Name")
customerFirstNameTextBox.bg = "#FFFFFF"
customerSurnameTextBox = TextBox(insertCustomers, width = "fill", text = "Customer Surname")
customerSurnameTextBox.bg = "#FFFFFF"
customerEmailTextBox = TextBox(insertCustomers, width = "fill", text = "Customer Email")
customerEmailTextBox.bg = "#FFFFFF"
customerAddLine1TextBox = TextBox(insertCustomers, width = "fill", text = "Address Line 1")
customerAddLine1TextBox.bg = "#FFFFFF"
customerAddLine2TextBox = TextBox(insertCustomers, width = "fill", text = "Address Line 2")
customerAddLine2TextBox.bg = "#FFFFFF"
customerCityTextBox = TextBox(insertCustomers, width = "fill", text = "City")
customerCityTextBox.bg = "#FFFFFF"
customerPostcodeTextBox = TextBox(insertCustomers, width = "fill", text = "Postcode")
customerPostcodeTextBox.bg = "#FFFFFF"
customerPhoneNumberTextBox = TextBox(insertCustomers, width = "fill", text = "PhoneNumber")
customerPhoneNumberTextBox.bg = "#FFFFFF"
customerSpecialNotesTextBox = TextBox(insertCustomers, width = "fill", text = "Special Notes (Optional)")
customerSpecialNotesTextBox.bg = "#FFFFFF"

#function to add value from the text boxes into the customers table
def addCustomer():
    if all(f'{customerFirstNameTextBox.value}',f'{customerSurnameTextBox.value}',f'{customerEmailTextBox.value}',f'{customerAddLine1TextBox.value}',f'{customerAddLine2TextBox.value}',f'{customerCityTextBox.value}',f'{customerPostcodeTextBox.value}',f'{customerPhoneNumberTextBox.value}') != "":
        insertStatement = "INSERT INTO customers (FirstName,Surname,Email,AddressLine1,AddressLine2,City,Postcode,PhoneNumber,SpecialNotes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        insertValues = (f'{customerFirstNameTextBox.value}',f'{customerSurnameTextBox.value}',f'{customerEmailTextBox.value}',f'{customerAddLine1TextBox.value}',f'{customerAddLine2TextBox.value}',f'{customerCityTextBox.value}',f'{customerPostcodeTextBox.value}',f'{customerPhoneNumberTextBox.value}',f'{customerSpecialNotesTextBox.value}')
        #cursor.execute(insertStatement,insertValues)
        #connection.commit()
        insertCoachesFeedback = Text(insertCoaches, text = "Success")
    else:
        insertCoachesFeedback = Text(insertCoaches, text = f"MySQL Error Code: {str(mysql.connector.Error)}")

#adding button to perform function
insertCustomersCommitButton = PushButton(insertCustomers, command = addCustomer, text = "COMMIT")
insertCustomersCommitButton.bg = "#FFFFFF"

#back button
(PushButton(insertCustomers, command = insertCustomers.hide, text = "Back", align = "bottom")).text_color = "#FFFFFF"

#destinations
insertDestinations = Window(home, title = "insertDestinations", bg = "#FF464C")
insertDestinations.hide()
def showinsertDestinations():
    insertDestinations.show(wait=True)

#title for inserting destinations
Text(insertDestinations, align ="top", text = "insert Destinations", color = "white", font = "Segoe UI", size = 20)

#adding text box to enter driver name into
destinationTextBox = TextBox(insertDestinations, align = "top", width = "fill", text = "Destination")
destinationTextBox.bg = "#FFFFFF"

#function to add value from the text box into the Destinations table
def addDestination():
    if destinationTextBox.value != "":
        #cursor.execute(f"INSERT INTO Destinations (Destination) VALUES ('{destinationTextBox.value}');")
        insertDestinationsFeedback = Text(insertDestinations, text = "Success")
    else:
        insertDestinationsFeedback = Text(insertDestinations, text = (f"MySQL Error Code: {str(mysql.connector.Error)}"))
    #connection.commit()

#adding button to perform function
insertDestinationsCommitButton = PushButton(insertDestinations, command = addDestination, text = "COMMIT")
insertDestinationsCommitButton.bg = "#FFFFFF"

#back button
(PushButton(insertDestinations, command = insertDestinations.hide, text = "Back", align = "bottom")).text_color = "#FFFFFF"

#trips
insertTrips = Window(home, title = "insertTrips", bg = "#FF464C")
insertTrips.hide()
def showinsertTrips():
    insertTrips.show(wait=True)

#title for inserting Trips
Text(insertTrips, align ="top", text = "insert Trips", color = "white", font = "Segoe UI", size = 20)

"""
#cursor.execute("SELECT DestinationID FROM destinations")
destinationIDRecords = cursor.fetchall()
destinationIDValues = [record[0] for record in destinationIDRecords]

#adding dropdown for destination id
Text(insertTrips, text = "DestinationID", color = "#FFFFFF")
destinationIDDropdown = Combo(insertTrips, options = (destinationIDValues))
destinationIDDropdown.bg = "#FFFFFF"

cursor.execute("SELECT CoachID FROM coaches")
coachIDRecords = cursor.fetchall()
coachIDValues = [record[0] for record in coachIDRecords]

#adding dropdown for coach id
Text(insertTrips, text = "CoachID", color = "#FFFFFF")
coachIDDropdown = Combo(insertTrips, options = (coachIDValues))
coachIDDropdown.bg = "#FFFFFF"

cursor.execute("SELECT DriverID FROM drivers")
driverIDRecords = cursor.fetchall()
driverIDValues = [record[0] for record in driverIDRecords]

#adding dropdown for driver id
Text(insertTrips, text = "DriverID", color = "#FFFFFF")
driverIDDropdown = Combo(insertTrips, options = (driverIDValues))
driverIDDropdown.bg = "#FFFFFF"
"""

#date textbox
Text(insertTrips, text = "Date (follow format YYYY-MM-DD)", color = "#FFFFFF")
tripDateTextBox = TextBox(insertTrips, text = "YYYY-MM-DD")
tripDateTextBox.bg = "#FFFFFF"

#function to add value from the text box into the Trips table
def addTrip():
    if destinationTextBox.value != "":
        try:
            """cursor.execute(f"INSERT INTO Trips (DestinationID, Date, DriverID, CoachID) VALUES "
                           f"('{destinationIDDropdown.value}', "
                           f"'{tripDateTextBox.value}', "
                           f"'{driverIDDropdown.value}', "
                           f"'{coachIDDropdown.value}')")
            insertTripsFeedback = Text(insertTrips, text="Success")"""
            print("e")
        except:
            #insertTripsFeedback = Text(insertTrips, text=f"MySQL Error Code: {str(e)}")
            print("o")
    else:
        insertTripsFeedback = Text(insertTrips, text="Destination is required")
    #connection.commit()


#adding button to perform function
insertTripsCommitButton = PushButton(insertTrips, command = addTrip, text = "COMMIT")
insertTripsCommitButton.bg = "#FFFFFF"

#back button
(PushButton(insertTrips, command = insertTrips.hide, text = "Back", align = "bottom")).text_color = "#FFFFFF"

#adding buttons to insert screen
insertCoachesButton = PushButton(insert, text = "insert Coaches", command = showinsertCoaches, align = "left", width = "fill")
insertCoachesButton.bg = "#FFFFFF"
insertCoachesButton.font = "Segoe UI"
insertDriversButton = PushButton(insert, text = "insert Drivers", command = showinsertDrivers, align = "left", width = "fill")
insertDriversButton.bg = "#FFFFFF"
insertDriversButton.font = "Segoe UI"
insertCustomersButton = PushButton(insert, text = "insert Customers", command = showinsertCustomers, align = "left", width = "fill")
insertCustomersButton.bg = "#FFFFFF"
insertCustomersButton.font = "Segoe UI"
insertDestinationsButton = PushButton(insert, text = "insert Destinations", command = showinsertDestinations, align = "right", width = "fill")
insertDestinationsButton.bg = "#FFFFFF"
insertDestinationsButton.font = "Segoe UI"
insertTripsButton = PushButton(insert, text = "insert Trips", command = showinsertTrips, align = "right", width = "fill")
insertTripsButton.bg = "#FFFFFF"
insertTripsButton.font = "Segoe UI"
#insertBookingsButton = PushButton(insert, text = "insert Bookings", command = showinsertBookings, align = "left")
#insertBookingsButton.bg = "#FFFFFF"
#insertBookingsButton.font = "Segoe UI"

#displaying home screen
home.display()
#end of code