""" Hello, this is my takeaway program for a fast food servoce called 'take it away' """
totalcost = 0
finalorder = {}
chickenbuckets = {'20pc': 49.99, '12pc': 29.99, '10pc': 24.99, '6pc': 14.99 }
burgers = {'tower': 14.99,'zinger': 12.99, 'mcspicy': 11.99, 'mcchicken': 8.99, '': 4.99 }
sides = {'chips': 4.99, 'potato and gravy': 4.99, 'coleslaw': 3.99, 'nuggets': 6.99 }
drinks = {'coke': 2.50, 'sprite': 2.50, 'fanta': 2.50, 'lmp': 2.50}
sauses = {'bbq': 0.99, 'tomato': 0.99, 'garlic aoli': 0.99}

alergymes = "This item contains ingredients that could cause alergens"



line = input('Item and Quantity: ')
while line:
  order = line.split()
  item = order[0]
  quantity = order[1]
  finalorder[item] = int(quantity)
  line = input('Name and number: ')

print(finalorder)