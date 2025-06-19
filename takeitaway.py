'''Hello, this is my takeaway program for a fast food service called take it away '''
from tkinter import*
from tkinter import font
totalcost = 0
finalorder = {}


#These are lists holding the items for the seperate catagories
bucketmenu = ['20pc', '12pc', '10pc', '6pc']
burgermenu = ['tower', 'zinger', 'grilled', 'crispy', 'mcchicken']
sidemenu = ['chips', 'potato and gravy', 'coleslaw', 'nuggets']
sausemenu = ['bbq', 'tomato', 'garlic aoli']
drinkmenu = ['coke', 'sprite', 'fanta', 'lmp']
fullmenu = ['20pc', '12pc', '10pc', '6pc', 'tower', 'zinger', 'grilled', 'crispy', 'mcchicken','chips', 'potato and gravy', 'coleslaw', 'nuggets','bbq', 'tomato', 'garlic aoli','coke', 'sprite', 'fanta', 'lmp']

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
font.families()
login_window.geometry("340x340")
login_window.title("Take it away - Login Page")
icon = PhotoImage(file="logo.png")
login_window.iconphoto(True, icon)
login_window.config(background= "#e4042c") #Sets the background colour of the window
login_window.resizable(False, False)  # Prevents resizing of the window
login_window.bind("<Return>", lambda event: login())  # Allows pressing Enter to trigger login
login_window.bind("<Escape>", lambda event: login_window.destroy())  # Allows pressing Escape to close the window
login_window.bind("<FocusIn>", lambda event: login_instruction_label.config(text="Please enter your email and password to continue."))  # Reset instruction label when the window gains focus
login_window.protocol("WM_DELETE_WINDOW", login_window.destroy)  # Ensures the window closes properly when the X button is clicked
# Function to handle login logic   


def login():
    """This function is called when the login button is clicked."""
    email = email_entry.get()
    password = password_entry.get()
    # Here you would typically handle the login logic, e.g., checking credentials
    if email and password:  # Simple check for non-empty fields
        print(f"Email: {email}, Password: {password}")
        menu_window = Tk()  # Create a new window for the menu
        menu_window.title("Take it away - Menu")
        menu_window.geometry("400x400")
        menu_window.config(background="#e4042c")
        # Create a label to display the welcome message
        name = name_entry.get()  # Get the name from the entry field
        menu_label = Label(menu_window, text=(f"Welcome to take it away {name}! "), bg="#e4042c", fg="black", font=("Arial", 12, "bold"))
        menu_label.pack(pady=20)
        # Here you would add the menu items and functionality
        # For now, just a placeholder label
        menu_items_label = Label(menu_window, text="Menu items will be displayed here.", bg="#e4042c", fg="black", font=("Arial", 10))
        menu_items_label.pack(pady=10)
        # Close the login window
        login_frame.destroy()
        login_window.destroy()  # Close the main window
           
    else:
        login_instruction_label.config(text="Please enter valid email and password to continue")
 # Ensure the login frame is destroyed when the menu window opens




# ----------Creating the login frame----------
login_frame = Frame(bg="#e4042c")  # Frame for the login page

# ----------Labels for the login page----------
welcome_label = Label(login_frame, 
    text="Welcome to Take it away!", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 9, "bold"),
    relief=GROOVE,
    bd=5,)

email_label = Label(login_frame, 
    text = "Email:", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12))

password_label = Label(login_frame, 
    text = "Password:", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12))

name_label = Label(login_frame,  
    text = "Name:", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12))
    
login_instruction_label = Label(login_frame, 
    text="Please enter your email and password to continue.", 
    bg="#ff0000", 
    fg="black", 
    font=("Arial", 10, "bold"), 
    relief=GROOVE,
    )


# ----------Entry widgets for user input----------

email_entry = Entry(login_frame, font=("Arial", 12))
# 'show' changes the password input makes it look like * but doesnt change value of the entry
password_entry = Entry(login_frame, font=("Arial", 12), show='*') 
name_entry = Entry(login_frame, font=("Arial", 12))

login_button = Button(login_frame, 
    text="Login", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12, "bold"), 
    command=login)







# ----------Placing widgets on the screen----------
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