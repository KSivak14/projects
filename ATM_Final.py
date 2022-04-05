import sys

#Name: Krystle Sivak
#ATM Script

#Sets a value to the user's account balance variable
account_balance = float(500.25)

#Defines the variable current balance
#Prints the current balance with a dollar sign and two decimal points
def current_balance (acct_balance):
	print('Your current balance is: $%.2f' % acct_balance)
	return acct_balance

#Defines the variable deposit amount
#Will ask the user how much money they want to deposit into account
#Will print their deposit amount and their current balance after deposit 
def deposit_amount (deposit):
	deposit_amount = float(input('How much would you like to deposit?\n'))
	ending_balance = deposit_amount + deposit
	print('Your deposit is $%.2f, your current balance is now $%.2f' % (deposit_amount, ending_balance))
	return ending_balance
  
#Defines the variable withdrawal amount
#Will ask the user how much money they want to withdraw from their account
#Will display a message about not having enough funds in account if the user tries to withdraw more money than they have in account
#If user has enough funds for withdrawal, the new balance will be displayed
def withdrawal_amount (withdrawal):
	withdrawal_amount = float(input('How much would you like to withdrawal?\n'))
	if withdrawal_amount > withdrawal:
		print('$%.2f is greater than your account balance of $%.2f' % (withdrawal_amount, withdrawal))
		return withdrawal
	else:
		new_balance = withdrawal - withdrawal_amount
		print('Your withdrawal is $%.2f, Your new balance is $%.2f' % (withdrawal_amount, new_balance))
		return new_balance
  
#Will ask the user what they would like to do
#Prints a message for the user to input D to deposit, W to withdraw, B to check balance, or Q to quit
print('Press D to deposit, W to withdraw, B to see current balance, or Q to quit\n')
userchoice = input ("What would you like to do?\n")

#Creates statements for each user input 
#If user enters Q the script will end and print a thank you message 
if (userchoice == 'D'):
	deposit_amount(account_balance)
elif (userchoice == 'W'):
	withdrawal_amount (account_balance)
elif (userchoice == 'B'):
	current_balance (account_balance)
elif (userchoice == 'Q'):
	print('Thank you for banking with us.')
