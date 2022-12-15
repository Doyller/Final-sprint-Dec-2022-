# Enter a new Employee (Driver)

# EmployeeFile = Employee.dat
# DefaultsFile = Default.dat


DefaultsFile = open("Defaults.dat", "r")

NextTransactionNum = float(DefaultsFile.readline())
DriverNum = int(DefaultsFile.readline())
StandFee = float(DefaultsFile.readline())
DailyRentalFee = float(DefaultsFile.readline())
WklyRentalRate = float(DefaultsFile.readline())
HST = float(DefaultsFile.readline())

DefaultsFile.close()

# Stand fees and rental


# validation
AllowedChar = "ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'"

# Inputs
while True:
    JoinDate = input("Enter Date (YYYY-MM-DD) : ")
    if JoinDate == "":
        print("Date must not be blank. Please re-enter.")
    else:
        break

while True:
    EmpFirstN = input("Enter new employee first name: ").title()
    if EmpFirstN == "":
        print("first name Name must not be blank. Please re-enter.")
    elif set(EmpFirstN).issubset(AllowedChar) == False:
        print("first Name contains invalid characters - re-enter")
    else:
        break

while True:
    EmpLastN = input("Enter new employee last name: ").title()
    if EmpLastN == "":
        print("Last name must not be blank. Please re-enter.")
    elif set(EmpLastN).issubset(AllowedChar) == False:
        print("Last Name contains invalid characters - re-enter")
    else:
        break

while True:
    Address = input("Enter employee address: ")
    if Address == "":
        print("Address can not be blank. Please re-enter.")
    else:
        break

while True:
    PhoneNum = input("Enter phone number: ")
    if PhoneNum == "":
        print("Phone number cannot be blank - re-enter.")
    elif len(PhoneNum) != 10:
        print("Phone number must contain 10 digits - re-enter.")
    elif PhoneNum.isdigit() == False:
        print("Phone number must be 10 digits")
    else:
        break

while True:
    LicenseNum = input("Enter driver license Number: ")
    if LicenseNum == "":
        print("License number can't be blank - re- enter")
    elif LicenseNum.isdigit() == False:
        print("License number must be Numbers")
    else:
        break

while True:
    LicenseExpiry = input("Enter driver license expiry date (YYYY-MM-DD): ")
    if LicenseExpiry == "":
        print("License expiry date can't be blank - re- enter")
    else:
        break

while True:
    CompanyNum = input("Enter company number: ")
    if CompanyNum == "":
        print("Company number can't be blank - re- enter")
    else:
        break

while True:
    InsurancePolicy = input("Enter insurance policy Company: ")
    if InsurancePolicy == "":
        print("car make can't be blank - re- enter")
    else:
        break

while True:
    PolicyNum = input("Enter policy number: ")
    if PolicyNum == "":
        print("Policy number can't be blank - re- enter")
    elif PolicyNum.isdigit() == False:
        print("Policy number must be Numbers")
    else:
        break

while True:
    CarModel = ""
    CarStatus = input("Enter if Company vehicle (Y/N): ").upper()
    if CarStatus == "":
        print("can't be blank - re- enter")
    elif CarStatus == "Y":
        CarModel = (input("Enter Car model (1-4):"))
        break
    elif CarStatus == "N":
        CarModel = "NA"
        break

    # save Data to the Employee.dat file
    EmployeeFile = open("Employee.dat", "a")

    EmployeeFile.write("{}, ".format(JoinDate))
    EmployeeFile.write("{}, ".format(DriverNum))
    EmployeeFile.write("{}, ".format(EmpFirstN))
    EmployeeFile.write("{}, ".format(EmpLastN))
    EmployeeFile.write("{}, ".format(Address))
    EmployeeFile.write("{}, ".format(PolicyNum))
    EmployeeFile.write("{}, ".format(LicenseNum))
    EmployeeFile.write("{}, ".format(LicenseExpiry))
    EmployeeFile.write("{}, ".format(InsurancePolicy))
    EmployeeFile.write("{}, ".format(CompanyNum))
    EmployeeFile.write("{}, ".format(CarStatus))
    EmployeeFile.write("{},\n ".format(CarModel))

    EmployeeFile.close()

    DriverNum += 1

    DefaultsFile = open("Defaults.dat", "w")

    DefaultsFile.write(f"{NextTransactionNum}\n ")
    DefaultsFile.write(f"{DriverNum}\n ")
    DefaultsFile.write(f"{StandFee}\n ")
    DefaultsFile.write(f"{DailyRentalFee}\n ")
    DefaultsFile.write(f"{WklyRentalRate}\n ")
    DefaultsFile.write(f"{HST}\n ")

    DefaultsFile.close()

    # Loop for Doing another employee.
    # Entering "Y" keeps looping back to "Do you want to process more Employees? (Y / N): "
    # I feel like it's a simple problem and im just being dumb.
while True:
    Continue = input("Do you want to process more Employees? (Y / N): ").upper()
    if Continue == "N":
        break





