""" Hello, this is my takeaway program for a fast food service called 'take it away' """
totalcost = 0
finalorder = {}

#These are lists holding the items for the seperate catagories
bucketmenu = ['20pc', '12pc', '10pc', '6pc']
burgermenu = ['tower', 'zinger', 'grilled', 'crispy', 'mcchicken']
sidemenu = ['chips', 'potato and gravy', 'coleslaw', 'nuggets']
sausemenu = ['bbq', 'tomato', 'garlic aoli']
drinkmenu = ['coke', 'sprite', 'fanta', 'lmp']
fullmenu = [
  '20pc', '12pc', '10pc', '6pc', 
  'tower', 'zinger', 'grilled', 'crispy', 'mcchicken',
  'chips', 'potato and gravy', 'coleslaw', 'nuggets',
  'bbq', 'tomato', 'garlic aoli',
  'coke', 'sprite', 'fanta', 'lmp'
  ]

#These are dictionaries holding the price of all the items 
bucketprice = {'20pc': 49.99, '12pc': 29.99, '10pc': 24.99, '6pc': 14.99 }
burgerprice = {'tower': 14.99,'zinger': 12.99, 'grilled': 11.99, 'crispy': 8.99, 'mcchicken': 4.99 }
sideprice = {'chips': 4.99, 'potato and gravy': 4.99, 'coleslaw': 3.99, 'nuggets': 6.99 }
sauseprice = {'bbq': 0.99, 'tomato': 0.99, 'garlic aoli': 0.99}
drinkprice = {'coke': 2.50, 'sprite': 2.50, 'fanta': 2.50, 'lmp': 2.50}

alergies = {}
alergymes = "This item contains ingredients that could cause alergens"

welcomemes = input("Hello, welcome to Take it Away what can I help you with? \n").lower()
if welcomemes == 'menu':
  print(fullmenu)