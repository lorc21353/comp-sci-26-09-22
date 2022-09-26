from tkinter import * #import tkinter which is a python gui library
from tkinter import ttk

pageNumber = int() # create an int called pagenumber

IDs = [40200, 200, 25, 2300] # create a list called IDs

def maths(*args): # create a function called maths 
    global frame # get the global var frame
    stockCheck = str() # create a string called stockcheck
    
    try: # try the code inside, run except if an error is encountered m
        pt = str(num.get()) # set the string pt to the value of the variabel num from the user input box
        pt1 = int(pt[1:3]) # split the string into the ints it contains 
        pt2 = int(pt[4:6])
        pt3 = int(pt[7:9])
        
        ID = pt1-pt2-pt3 # get the array id of the item from its end id 
        price = IDs[ID] # set the price variable to the id of the list IDs
        if price > 10000: # check if price is greater than 10k and sets stockcheck to a string if it is 
            stockCheck = "That item is too expensive for order, please see a tender"
        elif price >= 500 and price <= 10000: # checks if price is between 500 and 10k inclusive 
            stockCheck = "In order to purchase that item you must attain quotes from three different providers"
        elif price < 500: # checks if price is less than 500 
            stockCheck = "You may order that item"
        
    except: # if there was an error eg a wrong code typed then set stockcheck accordingly 
        stockCheck = "Invalid Entry Please try again."
    ttk.Label(frame, text = stockCheck).grid(column=3, row=5, sticky=W) # create a label inside the window frame that displays the string stockcheck

def pageTwo(): # function called page 2
    global frame # get the global frame
    frame.destroy() # delete frame
    frame = ttk.Frame(root, padding="5 5 12 12") # remake frame 
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    ttk.Button(frame, text="Product list", command=pageOne).grid(column=3, row=1, sticky=W) # make a button inside of frame that says the text on it and runs the pageOne fuction when clicked
    ttk.Label(frame, text="Please enter the item identification code.").grid(column=3, row=2, sticky=W) # create label in frame that displays some text
    global num # declare the global num
    num = StringVar() # set num to a stringvar
    number = ttk.Entry(frame, textvariable=num).grid(column=3, row=3, sticky=W) # make a text box that the user can type into inside of frame 
    ttk.Button(frame, text="Check Purchasability", command=maths).grid(column=3, row=4, sticky=W) # make a button that runs the function maths when pressed

def pageOne(): # function called page one
    global frame # get the global frame
    frame.destroy() # delete frame 
    frame = ttk.Frame(root, padding="5 5 12 12") # recreate frame
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    ttk.Button(frame, text="Check Purchasability", command=pageTwo).grid(column=3, row=1, sticky=W) # make button at the top of the page that runs pageTwo when pressed
    ttk.Label(frame, text="Robotic arm, Cost: €40,200, ID: #30-15-15").grid(column=3, row=2, sticky=W) # display the text 
    ttk.Label(frame, text="Camera, Cost: €200, ID: #75-21-53").grid(column=3, row=3, sticky=W)
    ttk.Label(frame, text="1TB hardrive, Cost: €25, ID: #45-11-32").grid(column=3, row=4, sticky=W)
    ttk.Label(frame, text="TIG Welder, Cost €2,300, ID: #95-63-29").grid(column=3, row=5, sticky=W)

root = Tk() # create the root of the window 
root.title("Rogerson's Robotics") # set the window title
root.geometry("450x200") # set the size of the window
frame = ttk.Frame(root, padding="5 5 12 12") # create frame 
frame.grid(column=0, row=0, sticky=(N, W, E, S))
pageOne() # call pageOne function

root.mainloop() # run the loop for the GUI display so the window doesnt just close after starting 
