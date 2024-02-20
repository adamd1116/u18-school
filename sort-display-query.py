# Change values accordingly, or make a function

from guizero import *

BG_COLOUR = "#5373A6"

app = App(title="Silver Dawn Coaches Digital Booking System", height=300, width=550,layout="grid")
app.bg = BG_COLOUR

booking_window = Window(app, title = "Add a new booking", height=500, width=600)
booking_window.bg = BG_COLOUR
booking_window_title = Box(booking_window,width=600,height=100,align="top",border=True)
booking_window_message = Text(booking_window_title, text="Add a new booking",size=25)
# For each attribute/column, I create an empty list to store the separated data.
example_data = [(1,'Adam Dunleavy'),(2,'Pavel Peev')] # Example data, SQL returns data in tuples, so I have recreated this.
id_values = [] 
name_values = []

for x in example_data: # Each iteration, x is a separate tuple containing a row of data from the DB
    id_values.append(x[0]) # Adding values to their corresponding data. First column is ID so it is index 0, etc...
    name_values.append(x[1])
    
column1 = Box(booking_window,align="left",width=300,height="fill",border=True)
column2 = Box(booking_window,align="left",width=300,height="fill",border=True)

column1_title = Text(column1,text="Driver ID",size=10)
column2_title = Text(column2,text="Driver Name",size=10)

column1_data = Text(column1,text="",size=10)
column2_data = Text(column2,text="",size=10)

for x in id_values: # adding each individual value to the text, and converting to string so I can add a new line
    column1_data.append(str(x)+"\n")
    
for x in name_values:
    column2_data.append(str(x)+"\n")
    
app.display()