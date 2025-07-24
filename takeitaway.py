"""Hello, this is my takeaway program for a fast food service called take it away """
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk 
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
icon = PhotoImage(file="iconlogo.png")
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
        
        print (f"New customer: Name - {name}, Email - {email} " )
        login_window.destroy() 


# -------------------- Creating the login frame --------------------
login_frame = Frame(background = "#e4042c")  

# -------------------- Labels for the login page --------------------
welcome_label = Label(login_frame, 
    text="Welcome to Take it away!", 
    background= "#e4042c", 
    foreground= "black", 
    font=("Verdana", 9, "bold"),
    relief=GROOVE,
    border=5,)
 
email_label = Label(login_frame, 
    text = "Email:", 
    background="#e4042c", 
    foreground= "black", 
    font=("Verdana", 12))

password_label = Label(login_frame, 
    text = "Password:", 
    background= "#e4042c", 
    foreground= "black", 
    font=("Verdana", 12))

name_label = Label(login_frame,  
    text = "Name:", 
    background= "#e4042c", 
    foreground= "black", 
    font=("Verdana", 12))
    
login_instruction_label = Label(login_frame, 
    text="Please enter your email and password to continue.", 
    background= "#ff0000", 
    foreground= "black", 
    font=("Verdana", 10, "bold"), 
    relief=GROOVE,
    )

# -------------------- Entry widgets for user input --------------------

email_entry = ttk.Entry(login_frame, font=("Verdana", 12))
# 'show' changes the password input makes it look like * but doesnt change value of the entry
password_entry = ttk.Entry(login_frame, font=("Verdana", 12), show='*') 
name_entry = ttk.Entry(login_frame, font=("Verdana", 12))

login_button = Button(login_frame, 
    text="Login", 
    background= "#e4042c", 
    foreground= "black", 
    font=("verdana", 12, "bold"), 
    command=login)

# -------------------- Placing widgets on the screen --------------------
welcome_label.grid(row=0, column=0, columnspan=2, sticky="NSEW" ,pady=35)
name_entry.grid(row=1, column=1)
name_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
login_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="NSEW")
login_instruction_label.grid(row=5, column=0, columnspan=2, sticky="NSEW")
login_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

login_window.mainloop()

if login_window != None: 
    menu_window = Tk()  
    menu_window.geometry("950x600")  
    menu_window.title("Take it away - Menu")  
    menu_window.config(background="#355aa9")  
    menu_window.resizable(False, False)
    menu_window.bind("<Escape>", lambda event: menu_window.destroy()) 
    icon = PhotoImage(file="iconlogo.png")
 

 
# -------------------- Styling --------------------
style = ttk.Style()
style.theme_use("clam")  
style.configure("MainMenuFrame.TFrame", background="#1d284b")
style.configure("MenuFrame.TFrame", background="#355aa9")
style.configure("FoodDisplayFrame.TFrame", background="#111924")
style.configure("OrderFrame.TFrame", background="#4870b5")    
style.configure("FoodFrame.TFrame", background = "#93949a", relief = "GROOVE")
style.configure("SelectedFood.TFrame", background = "#d08f74")

style.configure('MenuLabel.TLabel',background = "#111924", font = ("Verdana", 10), foreground = "white", padding = (5, 5, 5, 5), width = 21 )
style.configure('orderTotalLabel.TLabel', background = "#111924", font = ("Verdana", 10, "bold"), foreground = "white", padding = (2, 2, 2, 2), anchor = "w" )
style.configure('orderTransaction.TLabel', background = "#93949a", font = ('Verdana', 12), foreground = "white", 
                wraplength = 170, anchor = "nw", padding = (3, 3, 3, 3))

# -------------------- Images --------------------

#Logo to set the theme of the menu
LogoImageObject = Image.open("Images/menu logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)


TopBannerImageObject = Image.open("Images/Top banner options/topimage2.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Deafult image for when no food is selected
PlaceholderimageObject = Image.open("Images/place holder v1.jpg").resize((350, 360))
PlaceholderImage = ImageTk.PhotoImage(PlaceholderimageObject)


# -------------------- Food Images --------------------

# Food images are smaller than the display image because they have an order button below
ChickenbucketImageObject = Image.open("Images/food images/Chicken bucket.png").resize((350, 330))
ChickenbucketImage = ImageTk.PhotoImage(ChickenbucketImageObject)


ChickenPieceImageObject = Image.open("Images/food images/Chicken pieces.png").resize((350, 330))
ChickenPieceImage = ImageTk.PhotoImage(ChickenPieceImageObject)

BurgerImageObject = Image.open("Images/food images/Chicken burger.png").resize((350, 330))
BurgerImage = ImageTk.PhotoImage(BurgerImageObject)

ChipsImageObject = Image.open("Images/food images/chippies.png").resize((350, 330))
ChipsImage = ImageTk.PhotoImage(ChipsImageObject)

SauceImageObject = Image.open("Images/food images/Sause.png").resize((350, 330))
SauceImage = ImageTk.PhotoImage(SauceImageObject)

DrinkImageObject = Image.open("Images/food images/El Drinco.png").resize((350, 330))
DrinkImage = ImageTk.PhotoImage(DrinkImageObject)


# -------------------- Frames --------------------
mainFrame = ttk.Frame(menu_window, width= 800, height = 580, style="MainMenuFrame.TFrame")
mainFrame.grid(row=0, column=0, sticky="NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, columnspan=3, sticky="NSEW")

menuFrame = ttk.Frame(mainFrame, style="MenuFrame.TFrame")
menuFrame.grid(row=1, column=0, padx = 3, pady = 3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="FoodDisplayFrame.TFrame")   
displayFrame.grid(row=1, column=1, padx = 3, pady = 3, sticky="NSEW")

OrderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
OrderFrame.grid(row=1, column=2, padx = 3, pady = 3, sticky="NSEW")



# -------------------- Food Frames --------------------
ChickenbucketFrame = ttk.Frame(menuFrame, style="FoodFrame.TFrame")
ChickenbucketFrame.grid(row=1, column=0, sticky="NSEW")

ChickenPieceFrame = ttk.Frame(menuFrame, style="FoodFrame.TFrame")
ChickenPieceFrame.grid(row=2, column=0, sticky="NSEW")

BurgerFrame = ttk.Frame(menuFrame, style="FoodFrame.TFrame")
BurgerFrame.grid(row=3, column=0, sticky="NSEW")

ChipsFrame = ttk.Frame(menuFrame, style="FoodFrame.TFrame")
ChipsFrame.grid(row=4, column=0, sticky="NSEW")

SauceFrame = ttk.Frame(menuFrame, style="FoodFrame.TFrame")
SauceFrame.grid(row=5, column=0, sticky="NSEW")

DrinkFrame = ttk.Frame(menuFrame, style="FoodFrame.TFrame")
DrinkFrame.grid(row=6, column=0, sticky="NSEW")

orderTitleLabel = ttk.Label(OrderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(OrderFrame, text = "ORDER ID : ")
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(OrderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(OrderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(OrderFrame, text = "ORDER")
orderButton.grid(row = 4, column = 0, sticky = "EW")


displayLabel = ttk.Label(displayFrame, image = PlaceholderImage, style="MenuLabel.TLabel")
displayLabel.configure(background = "#111924")
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)


addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER")
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE")
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

# -------------------- Food Labels --------------------
LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#111924")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = Label(topBannerFrame, image = TopBannerImage, background = "#111924")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")


MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(anchor = "center", font = ("Verdana", 14, "bold"))


ChickenbucketLabel = ttk.Label(ChickenbucketFrame, text="Chicken Buckets     $30", style="MenuLabel.TLabel")
ChickenbucketLabel.grid(row=0, column=0, padx=10, pady=10 ,sticky="w")

ChickenPieceLabel = ttk.Label(ChickenPieceFrame, text="Chicken Pieces      $5", style="MenuLabel.TLabel")
ChickenPieceLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

BurgerLabel = ttk.Label(BurgerFrame, text="Chicken Burgers    $10", style="MenuLabel.TLabel")
BurgerLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

ChipsLabel = ttk.Label(ChipsFrame, text="Crispy Chips         $3", style="MenuLabel.TLabel")
ChipsLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

SauceLabel = ttk.Label(SauceFrame, text="Saucy Sauces       $1", style="MenuLabel.TLabel")
SauceLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

DrinkLabel = ttk.Label(DrinkFrame, text="Fizzy Drinks         $2", style="MenuLabel.TLabel")
DrinkLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# -------------------- Food Display Buttons ---------------------
ChickenbucketDisplayButton = ttk.Button(ChickenbucketFrame, text ="Display")
ChickenbucketDisplayButton.grid(row = 0, column = 1, padx = 10)

ChickenPieceDisplayButton = ttk.Button(ChickenPieceFrame, text ="Display")
ChickenPieceDisplayButton.grid(row = 0, column = 1, padx = 10)

BurgerDisplayButton = ttk.Button(BurgerFrame, text ="Display")
BurgerDisplayButton.grid(row = 0, column = 1, padx = 10)

ChipsDisplayButton = ttk.Button(ChipsFrame, text ="Display")
ChipsDisplayButton.grid(row = 0, column = 1, padx = 10)

SauceDisplayButton = ttk.Button(SauceFrame, text ="Display")
SauceDisplayButton.grid(row = 0, column = 1, padx = 10)

DrinkDisplayButton = ttk.Button(DrinkFrame, text ="Display")
DrinkDisplayButton.grid(row = 0, column = 1, padx = 10)

# -------------------- Configuring Grids --------------------
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
OrderFrame.columnconfigure(0, weight = 1)
OrderFrame.rowconfigure(2, weight = 1)

menu_window.mainloop()