
import datetime
import FormatValuse as FV

#formats used
def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr

f = open("Defaults.dat", "r")
NEXT_TRANSACTION_NUM= int(f.readline())
NEXT_DRIVER_NUM= float(f.readline())
MONTHLY_STD_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())
f.close()

#expenses
InvoiceNum = input("Enter the invoice number: ")
InvoiceDate =str(FDateS(datetime.datetime.now()))
DriverNum = NEXT_DRIVER_NUM
ItemNum = input("Enter the item number: ")
NumItems = input("Enter the number of items: ")
Description = input("Enter a description: ")
Cost = input("Enter the cost of the item: ")
Quantity = input("How many items are needed?: ")
ItemTotal = (Quantity * Cost)
HST = Itemtotal * HST_RATE
Subtotal = HST + ItemTotal

#revenue
TransID =
TransDate =
TransDescrip =
DriverID =
TransAmt =
HST =
TotCost =
StandFee =

#payment
PaymentID =
DriverID =
DatePayment =
PayAmt =
ReasonPayment =
PayMethod =
HST = HST_RATE * TotCost
Total =

#rental
RentalID =
DriverNum =
PickUp =
CarNum =
DayCar =
WeekCar =
NumDays =
HST = HST_RATE * TotCost
Total =

#car
LicensePlate = input("Enter license plate: ")
Owner = input("Enter car owner name: ")
