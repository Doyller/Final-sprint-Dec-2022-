#Expenses

def Expenses():

    while True:
        DefaultsFile = open("Defaults.dat", "r")

        NextTransactionNum = float(DefaultsFile.readline())
        DriverNum = int(DefaultsFile.readline())
        StandFee = float(DefaultsFile.readline())
        DailyRentalFee = float(DefaultsFile.readline())
        WklyRentalRate = float(DefaultsFile.readline())
        HSTRATE = float(DefaultsFile.readline())

        DefaultsFile.close()

        InVoiceNum = input("Enter the invoice number: ")
        if InVoiceNum == "":
            print("The invoice number can't' be blank - re enter.")
            continue
        elif InVoiceNum.isdigit() == False:
            print("The invoice number can only be numbers - re enter")
            continue
        else:
            break

    while True:

        InvoiceDate = input("Enter Invoice date(YYYY-MM-DD): ")
        if InvoiceDate == "":
            print("Invoice date can't be blank - re enter ")
            continue
        else:
            break

    while True:

        DriverNum = input("Enter driver number: ")
        if DriverNum == "":
            print("Drive number can't be blank - re enter ")
            continue
        elif DriverNum.isdigit() == False:
            print("The Driver number can only be numbers - re enter")
            continue
        else:
           break

    while True:

        Itemnum = (input("Enter item number : "))
        if Itemnum == "":
            print("Item number can't be blank - re enter ")
            continue
        elif Itemnum.isdigit() == False:
            print("The item number can only be numbers - re enter")
            continue
        else:
            break

    while True:

        ItemDescription = input("Enter item description: ")
        if ItemDescription == "":
            print("Item description can't be blank - re enter")
            continue
        else:
            break

    while True:

        ItemCost = float(input("Enter item cost: "))
        if ItemCost == "":
            print("Item cost can't be blank - re enter ")
            continue
        else:
            break

    while True:

        Quantity = int(input("Enter the Quantity of items: "))
        if Quantity == "":
            print("Quantity can't be blank - re enter")
            continue
        else:
            break

    #cal
    ItemTotal = ItemCost * Quantity
    HSTExpenses = HSTRATE * ItemTotal
    TotalExpenses = ItemTotal + HSTExpenses

    # save Data to the Expenses.dat file
    EmployeeFile = open("Expenses.dat", "a")

    EmployeeFile.write("{}, ".format(InVoiceNum))
    EmployeeFile.write("{}, ".format(InvoiceDate))
    EmployeeFile.write("{}, ".format(DriverNum))
    EmployeeFile.write("{}, ".format(Itemnum))
    EmployeeFile.write("{}, ".format(ItemDescription))
    EmployeeFile.write("{:,.2f}, ".format(ItemCost))
    EmployeeFile.write("{}, ".format(Quantity))
    EmployeeFile.write("{:,.2f}, ".format(ItemTotal))
    EmployeeFile.write("{:,.2f}, ".format(HSTExpenses))
    EmployeeFile.write("{:,.2f},\n ".format(TotalExpenses))

    EmployeeFile.close()

    while True:

        Continue = input("Do you want to process more Expenses? (Y / N): ").upper()
        if Continue == "Y":
            Expenses()
        elif Continue == "N":
            break

Expenses()