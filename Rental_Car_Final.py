import sys
'''
Section 1: Collect customer input
'''
#Name: Krystle Sivak
#Class: IT 140
#Project: Rental Car Billing Final

#By inputting B, D, or W this script will print the rental code and rental period
#B = Budget
#D = Daily
#W = Weekly
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

#If user inputs B or D the script will ask for number of days rented
#If user inputs W the script will ask for number of weeks rented
if rentalCode == 'B' or rentalCode == 'D':
  rentalPeriod = input("Number of Days Rented:\n")
else:
  rentalPeriod = input("Number of Weeks Rented:\n")

#Prints the rental code and rental period
print('Your rental code is: ' + str(rentalCode))
print('Your rental period is: ' +str(rentalPeriod))

#Assigns numeric value to the variables
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00 

#By inputting B, D, or W the script will print the base charge for the customer
#The base charge will be the rental period times the type of charge
#The price of each charge can be found above 
if rentalCode == 'B':
  baseCharge = float(rentalPeriod) * float(budgetCharge)
elif rentalCode == 'D':
  baseCharge = float(rentalPeriod) * float(dailyCharge)
elif rentalCode == 'W':
  baseCharge = float(rentalPeriod) * float(weeklyCharge)

#This will print the base charge with two decimal points
print('Your base charge is: ' + format(baseCharge, ',.2f'))

print()
#Customer will input the odometer reading the car has when recieved
odoStart = input("Starting Odometer Reading:\n")

#Customer will input the odometer reading after they are done driving the car
odoEnd = input("Ending Odometer Reading:\n")

#This will calculate the number of miles driven by the customer
totalMiles = int(odoEnd) - int(odoStart)

#Prints starting odometer reading, ending odometer reading, and total miles
print('Your starting odometer reading is: ' +str(odoStart))
print('Your ending odometer reading is: ' + str(odoEnd))
print('Your total miles are: ' + str(totalMiles))

#Assigns a starting value to the variables
mileCharge = 0
averageDayMiles = 0
averageWeekMiles = 0

#If customer inputs B as the rental code the total miles will be multiplied by 0.25
if rentalCode == 'B':
  mileCharge = totalMiles * 0.25

#If customer inputs D as the rental code the total miles are divided by the rental period
if rentalCode == 'D':
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  
#If customer uses less than or exactly 100 miles a day there will be no additional charges needed
#If customer uses more than 100 miles a day there will be an additional fee of their extra miles multiplied by 0.25
if averageDayMiles <= 100:
  mileCharge = 0
elif averageDayMiles > 100:
  extraMiles = averageDayMiles - 100
  mileCharge = extraMiles * 0.25

#If customer inputs W as the rental code the total miles are divided by the rental period
if rentalCode == 'W':
  averageWeekMiles = int(totalMiles) / int(rentalPeriod)

#If customer uses more than 900 miles a week 100 will be multiplied by the rental period
#If customer does not use more than 900 miles a week there will be no additional mile charges
if averageWeekMiles > 900:
  mileCharge = 100.00 * int(rentalPeriod)
else:
  mileCharge = 0

#This will print the mile charge with two decimal points
print(format(mileCharge, ',.2f'))

amtDue = baseCharge + mileCharge

#This will print a summary for the customer
print('Rental Summary')
print('Rental Code: '+ str(rentalCode))
print('Rental Period: '+ str(rentalPeriod))
print('Starting Odometer: '+ str(odoStart))
print('Ending Odometer: '+ str(odoEnd))
print('Miles Driven: '+ str(totalMiles))
print('Amount Due: '+ str(amtDue))