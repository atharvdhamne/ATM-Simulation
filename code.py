#import necessary liblaries
import random

#greeting
print("Welcome to the Atharv's ATM simulator!")

user_pin = 1234
enter_pin = int(input("Enter the PIN:"))
balance = random.randrange(1,9999)


if user_pin != enter_pin:
    print("You entered wrong PIN, Please try next time")
    ATM = False
else:
    ATM = True

#print()

#menu = [" ","1.Check Balance","2.Deposit Money","3.Withdrawal Money","4.Change PIN","5.Exit"]
#int(input("Enter the PIN:"))

"""
#balance = 99999
balance = random.randrange(1,9999)

user_pin = 1234

entered_pin = int(input("Please enter your PIN: "))

if entered_pin != user_pin:
    print("Invalid PIN. Exiting.")
    atm_on = False
else:
    atm_on = True

while atm_on:
    print("Main Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Your current balance is $" + str(balance))

    elif choice == '2':
        amount = float(input("Enter the amount to deposit: $"))
        balance += amount
        print("$" + str(amount) + " deposited successfully.")

    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("$" + str(amount) + " withdrawn successfully.")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        atm_on = False

    else:
        print("Invalid choice. Please try again.")"""