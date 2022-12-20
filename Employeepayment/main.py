# Recored Employee payment

def EmployeePayment():


    while True:

        DefaultsFile = open("Defaults.dat", "r")

        NextTransactionNum = float(DefaultsFile.readline())
        DriverNum = int(DefaultsFile.readline())
        StandFee = float(DefaultsFile.readline())
        DailyRentalFee = float(DefaultsFile.readline())
        WklyRentalRate = float(DefaultsFile.readline())
        HSTRATE = float(DefaultsFile.readline())

        DefaultsFile.close()

        EmpNumber = input("Enter employee number: ")
        if EmpNumber == "":
            print("Can't be blank - re enter")
            continue
        else:
            break

    while True:

        EmpNameF = input("Enter employee first name: ")
        if EmpNameF == "":
            print("Can't be blank - re enter")
            continue
        else:
            break

    while True:

        EmpNameL = input("Enter employee last name: ")
        if EmpNameL == "":
            print("Can't' be blank - re enter.")
            continue
        else:
            break

    while True:

        Address = input("Enter employee address:")
        if Address == "":
            print("Address can't' be blank - re enter.")
            continue
        else:
            break

    while True:
        PhoneNum = input("Enter employee phone number: ")
        if PhoneNum == "":
            print("Phone number can't' be blank - re enter.")
            continue
        elif PhoneNum.isdigit() == False:
            print("Phone number can only be numbers - re enter")
            continue
        else:
            break

    while True:
        CarType = input("Enter if company car (Y/N): ").upper()
        if CarType == "":
            print("Can't be blank - re enter")
            continue
        else:
            break

    while True:
        StandingFee = 0.0
        RentalChoice = ""
        if CarType == "Y":
            RentalChoice = input("Enter if Daily rental or Weekly (D/W): ").upper()
            break
        elif CarType == "N":
            StandingFee = StandFee
            break
        else:
            break

    while True:
        RentalChoicePrice = 0.0
        if RentalChoice == "D":
            RentalChoicePrice = DailyRentalFee
            break
        elif RentalChoice == "W":
            RentalChoicePrice = WklyRentalRate
            break
        else:
            break

    while True:
        DatePayment = input("Enter the date of the payment (YYYY/MM/DD)")
        if DatePayment == "":
            print("Can't be blank - re enter")
            continue
        else:
            break

    while True:
        PayAmt = float(input("Enter payment amount: "))
        if PayAmt == "":
            print("Can't be blank - re enter")
            continue
        else:
            break

    while True:
        ReasonPayment = input("Enter reason for payment: ")
        if ReasonPayment == "":
            print("Can't be blank - re enter")
            continue
        else:
            break

    while True:
        PaymentMethod = input("Enter payment method: ")
        if PaymentMethod == "":
            print("Can't be blank - re enter")
            continue
        else:
            break


    SubTotal = RentalChoicePrice + StandingFee + PayAmt
    HST = SubTotal * HSTRATE
    Total = SubTotal + HST

    # save Data to the EmployeePayment.dat file
    EmployeePaymentFile = open("EmployeePaymentFile.dat", "a")

    EmployeePaymentFile.write("{}, ".format(EmpNumber))
    EmployeePaymentFile.write("{}, ".format(EmpNameF))
    EmployeePaymentFile.write("{}, ".format(EmpNameL))
    EmployeePaymentFile.write("{}, ".format(Address))
    EmployeePaymentFile.write("{}, ".format(PhoneNum))
    EmployeePaymentFile.write("{}, ".format(DatePayment))
    EmployeePaymentFile.write("{}, ".format(RentalChoice))
    EmployeePaymentFile.write("{}, ".format(RentalChoicePrice))
    EmployeePaymentFile.write("{}, ".format(ReasonPayment))
    EmployeePaymentFile.write("{}, ".format(PaymentMethod))
    EmployeePaymentFile.write("{:,.2f}, ".format(PayAmt))
    EmployeePaymentFile.write("{:,.2f}, ".format(SubTotal))
    EmployeePaymentFile.write("{:,.2f}, ".format(HST))
    EmployeePaymentFile.write("{:,.2f},\n ".format(Total))

    EmployeePaymentFile.close()

    while True:

        Continue = input("Do you want to process more Employee payments? (Y / N): ").upper()
        if Continue == "Y":
            EmployeePayment()
        elif Continue == "N":
            break

EmployeePayment()













