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
welcomemes = "Welcome to Take it away, how can I help you today?"
#Creates and places window on screen
window = Tk()
font.families()
window.geometry("340x340")
window.title("Take it away - Login Page")
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background= "#e4042c") #Sets the background colour of the window

login_instruction_label = Label(window, 
    text="Please enter your email and password to continue", 
    bg="#ff0000", 
    fg="black", 
    font=("Arial", 10, "bold"), 
    relief=GROOVE, 
    bd=5,
    padx=10,
    pady=5,
    )


def login():
    """This function is called when the login button is clicked."""
    email = email_entry.get()
    password = password_entry.get()
    
    # Here you would typically handle the login logic, e.g., checking credentials
    if email and password:  # Simple check for non-empty fields
        print(f"Email: {email}, Password: {password}")
        login_instruction_label.config(text="Login successful!")
    else:
        login_instruction_label.config(text="Please enter valid credentials.")

frame = Frame(bg="#e4042c")

welcome_label = Label(frame, 
    text="Welcome to Take it away!", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 8, "bold"),
    relief=GROOVE,
    bd=5,)

email_label = Label(frame, 
    text = "Email:", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12))

password_label = Label(frame, 
    text = "Password:", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12))

email_entry = Entry(frame, font=("Arial", 12))
# 'show' changes the password input makes it look like * but doesnt change value of the entry
password_entry = Entry(frame, font=("Arial", 12), show='*') 

login_button = Button(frame, 
    text="Login", 
    bg="#e4042c", 
    fg="black", 
    font=("Arial", 12, "bold"), 
    command=login)



#Placing widgets on the screen
welcome_label.grid(row=0, column=0, columnspan=2, sticky="news" ,pady=35)
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=20)
login_instruction_label.grid(row=4, column=0,)



frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
window.mainloop()