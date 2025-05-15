totalcost = 0
finalorder = {}
chickenbuckets = {'20pc': 49.99, '12pc': 29.99, '10pc': 24.99, '6pc': 14.99 }
burgers = {}
sides = {}
drinks = {}







line = input('Item and Quantity: ')
while line:
  order = line.split()
  item = order[0]
  quantity = order[1]
  finalorder[item] = int(quantity)
  line = input('Name and number: ')

print(finalorder)