"""Hello, this is my takeaway program for a fast food service called take it away """
from tkinter import*
from tkinter import ttk
from tkinter import font
import os
#These are lists holding the items for the seperate catagories
bucketmenu = ['20pc', '12pc', '10pc', '6pc']
burgermenu = ['tower', 'zinger', 'grilled', 'crispy', 'mcchicken']
sidemenu = ['chips', 'potato and gravy', 'coleslaw', 'nuggets']
sausemenu = ['bbq', 'tomato', 'garlic aoli']
drinkmenu = ['coke', 'sprite', 'fanta', 'lmp']
fullmenu = [bucketmenu + burgermenu + sidemenu + sausemenu + drinkmenu]

#These are dictionaries holding the price of all the items 
bucketprice = {'20pc': 49.99, '12pc': 29.99, '10pc': 24.99, '6pc': 14.99 }
burgerprice = {'tower': 14.99,'zinger': 12.99, 'grilled': 11.99, 'crispy': 8.99, 'mcchicken': 4.99 }
sideprice = {'chips': 4.99, 'potato and gravy': 4.99, 'coleslaw': 3.99, 'nuggets': 6.99 }
sauseprice = {'bbq': 0.99, 'tomato': 0.99, 'garlic aoli': 0.99}
drinkprice = {'coke': 2.50, 'sprite': 2.50, 'fanta': 2.50, 'lmp': 2.50}

alergies = {}
alergymes = "This item contains ingredients that could cause alergens"
#Creates and places window on screen
login_window = Tk()
icon = PhotoImage(file="logo.png")
login_window.geometry("340x340")
login_window.title("Take it away - Login Page")
login_window.iconphoto(True, icon)  # Set the window icon


login_window.config(background= "#e4042c") 
login_window.resizable(False, False)
login_window.bind("<Return>", lambda event: login()) 
login_window.bind("<Escape>", lambda event: login_window.destroy())
login_window.bind("<FocusIn>", lambda event: login_instruction_label.config(text="Please enter your email and password"))


def login():
    email = email_entry.get()
    password = password_entry.get()
    name = name_entry.get()
    if "@" not in email or "." not in email:  
        login_instruction_label.config(text="Please enter a correct email address.")
    elif len(password) < 6:  
        login_instruction_label.config(text="Password be at least 6 letters long.")
    elif email and password == "":
        login_instruction_label.config(text="Please enter valid email and password to continue")
    else:
        login_instruction_label.config(text=f"Welcome {name}! You are now logged in.")
        
        print (f"New customer. Name - {name}, Email - {email} " )
        login_window.destroy() 


# -------------------- Creating the login frame --------------------
login_frame = Frame(bg="#e4042c")  

# -------------------- Labels for the login page --------------------
welcome_label = Label(login_frame, 
    text="Welcome to Take it away!", 
    bg="#e4042c", 
    fg="black", 
    font=("Verdana", 9, "bold"),
    relief=GROOVE,
    bd=5,)
 
email_label = Label(login_frame, 
    text = "Email:", 
    bg="#e4042c", 
    fg="black", 
    font=("Verdana", 12))

password_label = Label(login_frame, 
    text = "Password:", 
    bg="#e4042c", 
    fg="black", 
    font=("Verdana", 12))

name_label = Label(login_frame,  
    text = "Name:", 
    bg="#e4042c", 
    fg="black", 
    font=("Verdana", 12))
    
login_instruction_label = Label(login_frame, 
    text="Please enter your email and password to continue.", 
    bg="#ff0000", 
    fg="black", 
    font=("Verdana", 10, "bold"), 
    relief=GROOVE,
    )

# -------------------- Entry widgets for user input --------------------

email_entry = Entry(login_frame, font=("Verdana", 12))
# 'show' changes the password input makes it look like * but doesnt change value of the entry
password_entry = Entry(login_frame, font=("Verdana", 12), show='*') 
name_entry = Entry(login_frame, font=("Verdana", 12))

login_button = Button(login_frame, 
    text="Login", 
    bg="#e4042c", 
    fg="black", 
    font=("verdana", 12, "bold"), 
    command=login)

# -------------------- Placing widgets on the screen --------------------
welcome_label.grid(row=0, column=0, columnspan=2, sticky="news" ,pady=35)
name_entry.grid(row=1, column=1)
name_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
login_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="news")
login_instruction_label.grid(row=5, column=0, columnspan=2, sticky="news")
login_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")

login_window.mainloop()

if login_window != None: 
    menu_window = Tk()  
    menu_window.geometry("800x600")  
    menu_window.title("Take it away - Menu")  
    menu_window.config(background="#e4042c")  
    menu_window.resizable(False, False)
    menu_window.bind("<Escape>", lambda event: menu_window.destroy()) 
    icon = PhotoImage(file="logo.png")
 

 
# -------------------- Styling --------------------
style = ttk.Style()
style.theme_use("clam")  # Using the clam theme for a modern look
style.configure("MainMenuFrame.TFrame", background="#1d284b")
style.configure("MenuFrame.TFrame", background="#355aa9")
style.configure("FoodDisplayFrame.TFrame", background="#111924")
style.configure("OrderFrame.TFrame", background="#4870b5")
style.configure("FoodFrame.TFrame", background = "#93949a", relief = "raised")
style.configure("SelectedFood.TFrame", background = "#d08f74")

style.configure('MenuLabel.TLabel',background = "#111924", font = ("Verdana", 13), foreground = "white", padding = (5, 5, 5, 5), width = 21 )
style.configure('orderTotalLabel.TLabel', background = "#111924", font = ("Verdana", 10, "bold"), foreground = "white", padding = (2, 2, 2, 2), anchor = "w" )
style.configure('orderTransaction.TLabel', background = "#93949a", font = ('Verdana', 12), foreground = "white", wraplength = 170, anchor = "nw", padding = (3, 3, 3, 3) )

# -------------------- Widgets --------------------
mainFrame = ttk.Frame(menu_window, width= 800, height = 500, style="MainMenuFrame.TFrame")



#Kia Ora Luka

RestaurantBannerLabel = Label(topBannerFrame, image = TopBannerImage, background = "#111924")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "news")




menu_window.mainloop()