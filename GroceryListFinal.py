#Name: Krystle Sivak
#Grocery List

#Shows an empty dictionary assigned to grocery_item
grocery_item = {}
#Shows an empty list assigned to grocery_history
grocery_history = []

#Shows that if the loop is true, it will continue
stop = 'go'
#Shows that by entering q, the loop will be false or not true and end
while stop != 'q':

#Input for name
  item_name = input('Item name: ')
#Input for number
  quantity = input('Quantity purchased: ')
#Input for price
  cost = input('Price per item: ')

#Key identifiers for name, number, and price 
#Number will have an integer for the quantity purchased
#Price will have a float for the cost
  grocery_item['name'] = item_name
  grocery_item['number'] = int(quantity)
  grocery_item['price'] = float(cost)

#Adds grocery items purchased to the grocery history list
  grocery_history.append(grocery_item.copy())

#Option for customer to either continue or quit
#Inputting c will allow customer to continue adding items
#Inputting q will allow customer to quit and stop the loop
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

#Sets the grand_total to zero
  grand_total = 0
#Creates a for loop 
for item in grocery_history:
 #The item_total will be calculated by multiplying the item number with the item price
  item_total = item['number'] * item['price']
#Adds the item_total and the grand_total
  grand_total = grand_total + item_total
  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
#Prints the receipt to show the price per item as well as the price for the total

#Sets the item_total to zero
item_total = 0

#Prints the grand total with a $ and two decimal points
print('Grand Total: $ %.2f' % grand_total)

