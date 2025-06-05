'''Hello, this is my takeaway program for a fast food service called take it away '''
from tkinter import*
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

window.geometry("500x500")
window.title("Take it away program")
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background= "#cc5200")


wellabel = Label(window, 
    text=welcomemes, 
    bg="#ff0000", 
    fg="black", 
    font=("Arial", 10, "bold"), 
    relief=RAISED, 
    bd=5,
    padx=10,
    pady=5,
    )
wellabel.grid(row=0, column=0)

Emaillabel = Label(window, Text="email: ")
Emaillabel.grid(row=1, column=0)

#Creates and places the entry boxes for email
EmailEntry = Entry(window,
    width=30,
    font=('Arial', 10, 'bold'),
    bg='white',
    fg='black',
    )  
#email.insert(0, 'Enter your email here')
EmailEntry.grid(row=2, column=0)

#Creates and places the entry box for password
PasswordEntry = Entry(window,
    width=30,
    font=('Arial', 10, 'bold'),
    bg='white',
    fg='black',
    show='*'
    )
#password.insert(0, 'Enter your password here')
PasswordEntry.grid(row=3, column=0)



def delete():
    EmailEntry.delete(0, END)
    PasswordEntry.delete(0, END)
    login_instruction_label.config(text="Please enter your email and password to continue",
    font=('Arial', 10, 'bold'))
def Submit():
    Email_text = EmailEntry.get()
    password_text = PasswordEntry.get()
    if Email_text and password_text:
        login_instruction_label.config(text=f"Welcome {Email_text}!")
        print(f"Email: {Email_text}, Password: {password_text}"),
        COMMAND=delete
    else:
        login_instruction_label.config(text="Please enter both email and password.",
        font=('Arial', 10, 'bold'))

submit = Button(window,
    text='Submit',
    font=('Arial', 10, 'bold'),
    bg='#ff6200',
    fg='black',
    activebackground='#FF0000',
    activeforeground='black',
    command=Submit,)

submit.grid(row=4, column=0, padx=10, pady=5)

login_instruction_label = Label(window, 
    text="Please enter your email and password to continue", 
    bg="#ff0000", 
    fg="black", 
    font=("Arial", 10, "bold"), 
    relief=RAISED, 
    bd=5,
    padx=10,
    pady=5,
    )
login_instruction_label.grid(row=5, column=0,)




#This is the function that will be called when the button is clicked
#count = 0
#def click():
    #global count
    #count+=1
    #login_instruction_label.config(text=count)
#button = Button(window,text='Click me!!!')
#button.config(command=click) 
#button.config(font=('Ink Free',10,'bold'))
#button.config(bg='#ff6200')
#button.config(fg='#fffb1f')
#button.config(activebackground='#FF0000')
#button.config(activeforeground='#fffb1f')
#image = PhotoImage(file='point_emoji.png')
#button.config(image=image)
#button.config(compound='')
#button.pack()
#label = Label(window,text=count)
#label.config(font=('Monospace',40))
#label.pack()


window.mainloop()



#if welcomemes == 'menu':
    #for menu in fullmenu:
        #print(menu)
  
#print(*fullmenu, sep =', ')