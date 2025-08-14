"""Hello, this is my takeaway program for a fast food service called take it away """

# Importing nescessary libraries
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk 
import random
from datetime import date
from datetime import datetime

# -------------------- Global Variables --------------------
Foodprices = {"Chicken Bucket": 30, "Chicken Pieces": 5, "Chicken Burger": 10, "Crispy Chips": 3, "Saucy Sauce": 1, "Fizzy Drink": 2}
new_reciept = ""

def disable():
    pass

#Creates and places window on screen
login_window = Tk()
IconImageObject = Image.open("Images/iconlogo.png")
IconImage = ImageTk.PhotoImage(IconImageObject)
login_window.geometry("340x340")
login_window.title("Take it away - Login Page")
login_window.iconphoto(True, IconImage)  # Set the window icon

#Add background colour, make the window not resizable, bind basic key commands, and disable close button for user.
login_window.config(background= "#355aa9") 
login_window.resizable(False, False)
login_window.bind("<Return>", lambda event: login()) 
login_window.bind("<End>", lambda event: login_window.destroy())
login_window.bind("<FocusIn>", lambda event: login_instruction_label.config(text="Please enter your email and password"))
login_window.protocol("WM_DELETE_WINDOW", disable)

# Login function checks if user is entring correct information and closes if info is correct 
def login():
    email = email_entry.get()
    password = password_entry.get()
    name = name_entry.get()
    if email and password == "":
        login_instruction_label.config(text="Please enter email and password")
    elif "@" not in email or "." not in email: 
        login_instruction_label.config(text="Please enter a correct email address.")
    elif len(password) < 6:  
        login_instruction_label.config(text="Password be at least 6 letters long.")
    else:
        login_window.destroy() 
        print(f"Login successful for {name} with email {email}.") 


# -------------------- Creating the login frame --------------------
login_frame = Frame(background = "#355aa9")  

# -------------------- Labels for the login page --------------------
welcome_label = Label(login_frame, 
    text="Welcome to Take it away!", 
    background= "#355aa9", 
    foreground= "black", 
    font=("Verdana", 9, "bold"),
    relief=GROOVE,
    border=5,)
 
email_label = Label(login_frame, 
    text = "Email:", 
    background="#355aa9", 
    foreground= "black", 
    font=("Verdana", 12))

password_label = Label(login_frame, 
    text = "Password:", 
    background= "#355aa9", 
    foreground= "black", 
    font=("Verdana", 12))

name_label = Label(login_frame,  
    text = "Name:", 
    background= "#355aa9", 
    foreground= "black", 
    font=("Verdana", 12))
    
login_instruction_label = Label(login_frame, 
    text="Please enter your email and password to continue.", 
    background= "#355aa9", 
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
    background= "#355aa9", 
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

# ------------------------------ MENU WINDOW ------------------------------

# After logging in, if statment checks if they are then crates a new window for the menu
if login_window != None: 
    menu_window = Tk()  
    menu_window.geometry("940x546")  
    menu_window.title("Take it away - Menu")  
    menu_window.config(background="#355aa9")  
    menu_window.resizable(False, False)
    menu_window.bind("<End>", lambda event: menu_window.destroy()) 
    menu_window.protocol("WM_DELETE_WINDOW", disable)
 
# -------------------- Styling --------------------
# Creating styles for the frames to make them more appealing and easier for the users to read
style = ttk.Style() 
style.configure("MainMenuFrame.TFrame", background="#1d284b")
style.configure("MenuFrame.TFrame", background="#355aa9")
style.configure("FoodDisplayFrame.TFrame", background="#111924")
style.configure("OrderFrame.TFrame", background="#4870b5")    
style.configure("FoodFrame.TFrame", background = "#93949a", relief = GROOVE)
style.configure("SelectedFood.TFrame", background = "#98FBCB", relief = GROOVE)

style.configure('MenuLabel.TLabel',background = "#111924", font = ("Verdana", 10), foreground = "white", padding = (7, 5, 5, 7), width = 21 )
style.configure('orderTotalLabel.TLabel', background = "#111924", font = ("Verdana", 10, "bold"), foreground = "white", padding = (2, 2, 2, 2), anchor = "w" )
style.configure('orderTransaction.TLabel', background = "#93949a", font = ('Verdana', 12), foreground = "white", 
                wraplength = 200, anchor = "nw", padding = (3, 3, 3, 3))

# -------------------- Functions --------------------
# Functions for displaying individual food items and updating the display label with the correct image and text
def displaychickenbucket():
    ChickenbucketFrame.configure(relief = GROOVE, style = "SelectedFood.TFrame")
    
    # Reset all other food frames to default style
    ChickenPieceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    BurgerFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChipsFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    SauceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    DrinkFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    displayLabel.configure(image = ChickenbucketImage, text = "Chicken Bucket", style = "MenuLabel.TLabel",
                           compound = "bottom", foreground= "white", padding = (5, 5, 5, 5))
    
def displaychickenpiece():

    ChickenPieceFrame.configure(relief = GROOVE, style = "SelectedFood.TFrame")

    ChickenbucketFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    BurgerFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChipsFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    SauceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    DrinkFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    displayLabel.configure(image = ChickenPieceImage, text = "Chicken Pieces", style = "MenuLabel.TLabel",
                           compound = "bottom", foreground= "white", padding = (5, 5, 5, 5))
    
def displaychickenburger():
    BurgerFrame.configure(relief = GROOVE, style = "SelectedFood.TFrame")

    ChickenbucketFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChickenPieceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChipsFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    SauceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    DrinkFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    displayLabel.configure(image = BurgerImage, text = "Chicken Burger", style = "MenuLabel.TLabel",
                           compound = "bottom", foreground= "white", padding = (5, 5, 5, 5))
    
def displayChips():
    ChipsFrame.configure(relief = GROOVE, style = "SelectedFood.TFrame")

    ChickenbucketFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChickenPieceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    BurgerFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    SauceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    DrinkFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    displayLabel.configure(image = ChipsImage, text = "Crispy Chips", style = "MenuLabel.TLabel",
                           compound = "bottom", foreground= "white", padding = (5, 5, 5, 5))
    
def displaySauce():
    SauceFrame.configure(relief = GROOVE, style = "SelectedFood.TFrame")   

    ChickenbucketFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChickenPieceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    BurgerFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChipsFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    DrinkFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    displayLabel.configure(image = SauceImage, text = "Saucy Sauce", style = "MenuLabel.TLabel",
                           compound = "bottom", foreground= "white", padding = (5, 5, 5, 5))
    
def displayDrink():
    DrinkFrame.configure(relief = GROOVE, style = "SelectedFood.TFrame")

    ChickenPieceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChickenbucketFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    BurgerFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    ChipsFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    SauceFrame.configure(relief = GROOVE, style = "FoodFrame.TFrame")
    displayLabel.configure(image = DrinkImage, text = "Fizzy Drink", style = "MenuLabel.TLabel",
                           compound = "bottom", foreground= "white", padding = (5, 5, 5, 5))

# Add function that allows user to add food to their order and updates the total price
def add():
    current_order = orderTransaction.cget("text")
    if displayLabel.cget("text") == "":
        orderTransaction.configure(text="Please select a food item to add to your order.")
        return
    selected_food = displayLabel.cget("text") + " - $" + str(Foodprices[displayLabel.cget("text")])

    if current_order.strip():
        order = current_order + "\n" + selected_food
    else:
        order = selected_food
    orderTransaction.configure(text=order)
    
    # Update the total price
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    # Check if order_total is a digit, if not set it to 0
    order_total = int(order_total) if order_total.isdigit() else 0
    updated_total = order_total + Foodprices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

# Remove function that allows user to remove unwanted food from their order where ever it is. eg first item or middle of the order
def remove():
    current_order = orderTransaction.cget("text")
    displayed_food = displayLabel.cget("text")  

    if current_order.strip():
        order_lines = current_order.split("\n")
        
        # Find and remove the line that matches the displayed food
        for line in order_lines:
            if line.startswith(displayed_food):
                order_lines.remove(line)
                # Update total price by subtracting the price of the displayed food and replacing the $ with nothing so it can be transformed into an integer
                order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
                order_total = order_total.replace("$", "")
                updated_total = int(order_total) - Foodprices[displayed_food]
                orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")                
                break 

        # Join the remaining lines back into a single string
        updated_order = "\n".join(order_lines)
        orderTransaction.configure(text=updated_order)
    else:
        orderTransaction.configure(text="")

#Generates a random order ID for the user to identify their order
def generate_order_id():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    order_id = "TIA - "
    random_letters = ""
    random_numbers = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_numbers += str(random.choice(numbers))

    order_id += random_letters + random_numbers
    return order_id


# Function that creates a reciept file with the user's order details, eg price, date/time, etc
def order():
    new_reciept = orderIDLabel.cget("text")
    new_reciept = new_reciept.replace("ORDER ID : ", "")
    total_transaction = orderTransaction.cget("text").split("\n") 
    total_transaction = [item.strip() for item in total_transaction if item.strip()]

    order_day = date.today()
    order_time = datetime.now()

    #Create a reciept file with user's total order price and date times
    with open(new_reciept, "w") as file:
        file.write("Take it away" + "\n")
        file.write(new_reciept + "\n")
        file.write("----------------------------------------------------" + "\n")
        file.write(order_day.strftime("%x") + "\n")
        file.write(order_time.strftime("%H:%M:%p") + "\n\n")
        file.write("Items Ordered:"+ "\n")
        for item in total_transaction:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text") + "\n")
    
    #Reset the order display for the next customer. 
    order_comfirmation = ("Your order reciept is"+ "\n" + new_reciept + "\n")
    orderTotalLabel.configure(text = "Total : $0")
    orderIDLabel.configure(text = "ORDER ID : " + generate_order_id())
    orderTransaction.configure(text = order_comfirmation)
  
# -------------------- Images --------------------

#Logo to set the theme of the menu
LogoImageObject = Image.open("Images/menu logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Images/Top banner options/topimage2.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Deafult image for when no food is selected
PlaceholderimageObject = Image.open("Images/place holder v3.jpg").resize((350, 368))
PlaceholderImage = ImageTk.PhotoImage(PlaceholderimageObject)

# -------------------- Food Images --------------------

# Food images just smaller than display image beacause of the food name above the image
ChickenbucketImageObject = Image.open("Images/food images/Chicken bucket.png").resize((350, 350))
ChickenbucketImage = ImageTk.PhotoImage(ChickenbucketImageObject)

ChickenPieceImageObject = Image.open("Images/food images/Chicken pieces.png").resize((350, 350))
ChickenPieceImage = ImageTk.PhotoImage(ChickenPieceImageObject)

BurgerImageObject = Image.open("Images/food images/Chicken burger.png").resize((350, 350))
BurgerImage = ImageTk.PhotoImage(BurgerImageObject)

ChipsImageObject = Image.open("Images/food images/chippies.png").resize((350, 350))
ChipsImage = ImageTk.PhotoImage(ChipsImageObject)

SauceImageObject = Image.open("Images/food images/Sause.png").resize((350, 350))
SauceImage = ImageTk.PhotoImage(SauceImageObject)

DrinkImageObject = Image.open("Images/food images/El Drinco.png").resize((350, 350))
DrinkImage = ImageTk.PhotoImage(DrinkImageObject)

# -------------------- Frames --------------------

# Each individual frame is created for all of the sections like order frame displaying total order and menu frame displaing foods
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
# Each food has its own frame to display different food item and prices, while also being able to be individually manipulated
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

# Puts the randomly generated order ID on the screen for the user to see
orderIDLabel = ttk.Label(OrderFrame, text = "ORDER ID : " + generate_order_id())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(OrderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(OrderFrame, text = "TOTAL : $0", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(OrderFrame, text = "ORDER", command= order)
orderButton.grid(row = 4, column = 0, sticky = "EW")

displayLabel = ttk.Label(displayFrame, image = PlaceholderImage, style="MenuLabel.TLabel")
displayLabel.configure(background = "#111924")
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
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
# Buttons for displaying food items with individual functions 
ChickenbucketDisplayButton = ttk.Button(ChickenbucketFrame, text ="Display", command= displaychickenbucket)
ChickenbucketDisplayButton.grid(row = 0, column = 1, padx = 10)

ChickenPieceDisplayButton = ttk.Button(ChickenPieceFrame, text ="Display", command= displaychickenpiece)
ChickenPieceDisplayButton.grid(row = 0, column = 1, padx = 10)

BurgerDisplayButton = ttk.Button(BurgerFrame, text ="Display" , command= displaychickenburger)
BurgerDisplayButton.grid(row = 0, column = 1, padx = 10)

ChipsDisplayButton = ttk.Button(ChipsFrame, text ="Display", command= displayChips)
ChipsDisplayButton.grid(row = 0, column = 1, padx = 10)

SauceDisplayButton = ttk.Button(SauceFrame, text ="Display", command= displaySauce)
SauceDisplayButton.grid(row = 0, column = 1, padx = 10)

DrinkDisplayButton = ttk.Button(DrinkFrame, text ="Display", command= displayDrink)
DrinkDisplayButton.grid(row = 0, column = 1, padx = 10)

# -------------------- Configuring Grids --------------------
# Configuring the grid weights to make frames expand and fill even amounts of avalible space
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