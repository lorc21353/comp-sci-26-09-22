from tkinter import *
from tkinter import ttk

pageNumber = int()

IDs = [40200, 200, 25, 2300]

def maths(*args):
    global frame
    stockCheck = str()
    
    try:
        pt = str(num.get())
        pt1 = int(pt[1:3])
        pt2 = int(pt[4:6])
        pt3 = int(pt[7:9])
        
        ID = pt1-pt2-pt3
        price = IDs[ID]
        if price > 10000:
            stockCheck = "That item is too expensive for order, please see a tender"
        elif price >= 500 and price <= 10000:
            stockCheck = "In order to purchase that item you must attain quotes from three different providers"
        elif price < 500:
            stockCheck = "You may order that item"
        
    except:
        stockCheck = "Invalid Entry Please try again."
    ttk.Label(frame, text = stockCheck).grid(column=3, row=5, sticky=W)

def pageTwo():
    global frame
    frame.destroy()
    frame = ttk.Frame(root, padding="5 5 12 12")
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    ttk.Button(frame, text="Product list", command=pageOne).grid(column=3, row=1, sticky=W)
    ttk.Label(frame, text="Please enter the item identification code.").grid(column=3, row=2, sticky=W)
    global num
    num = StringVar()
    number = ttk.Entry(frame, textvariable=num).grid(column=3, row=3, sticky=W)
    ttk.Button(frame, text="Check Purchasability", command=maths).grid(column=3, row=4, sticky=W)

def pageOne():
    global frame
    frame.destroy()
    frame = ttk.Frame(root, padding="5 5 12 12")
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    ttk.Button(frame, text="Check Purchasability", command=pageTwo).grid(column=3, row=1, sticky=W)
    ttk.Label(frame, text="Robotic arm, Cost: €40,200, ID: #30-15-15").grid(column=3, row=2, sticky=W)
    ttk.Label(frame, text="Camera, Cost: €200, ID: #75-21-53").grid(column=3, row=3, sticky=W)
    ttk.Label(frame, text="1TB hardrive, Cost: €25, ID: #45-11-32").grid(column=3, row=4, sticky=W)
    ttk.Label(frame, text="TIG Welder, Cost €2,300, ID: #95-63-29").grid(column=3, row=5, sticky=W)

root = Tk()
root.title("Rogerson's Robotics")
root.geometry("450x200")
frame = ttk.Frame(root, padding="5 5 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
pageOne()

root.mainloop()