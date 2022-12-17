# Enter Revenues

# imports
import datetime

AllCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'"

# Constants
HST_RATE = 0.15
STANDFEE_RATE = 175.00

# inputs

while True:
    TransID = input("Enter the transaction ID: ")
    if TransID == "":
        print("Transaction ID invalid. Please re-enter. ")
    else:
        break

while True:
    TransDate = input("Enter Transaction date YYYY-MM-DD: ")
    if TransDate == "":
        print("Transaction Date invalid, please re-enter.")
    else:
        break

while True:
    DriverID = input("Enter the Driver ID: ")
    if DriverID == "":
        print("Driver ID cannot be blank, please re-enter.")
    else:
        break

while True:
    TransAmt = float(input("Enter the transaction amount: "))
    if TransAmt == "":
        print("Transaction amount cannot be blank, please re-enter.")
    else:
        break

# Calculations

HST = TransAmt * HST_RATE
TotCost = TransAmt + HST
StandFee = STANDFEE_RATE

# Create revenues file

RevenueFile = open("Revenues.dat", "a")

RevenueFile.write("{}, ".format(TransDate))
RevenueFile.write("{}, ".format(TransID))
RevenueFile.write("{}, ".format(DriverID))
RevenueFile.write("{}, ".format(TransAmt))
RevenueFile.write("{}, ".format(HST))
RevenueFile.write("{}, ".format(TotCost))
RevenueFile.write("{}, ".format(StandFee))

RevenueFile.close()

while True:
    Continue = input("Would you like to enter another Revenue? Y/N: ").upper()
    if Continue == "N":
        break




