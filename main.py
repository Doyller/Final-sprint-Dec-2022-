# Rental data report

import FormatValues as FV

DefaultsFile = open("Defaults.dat", "r")
DriverID = int(DefaultsFile.readline())
StandFee = float(DefaultsFile.readline())
DailyRentalFee = float(DefaultsFile.readline())
WklyRentalRate = float(DefaultsFile.readline())
HST = float(DefaultsFile.readline())

while True:
    RentOpt = input("Enter if the vehicle is being rented or an owned vehicle (O or R): ")
    if RentOpt == "R":
        PickUp = input("Enter when the vehicle was picked up (YYYY-MM-DD): ")
        CarNum = int(input("Enter which car was rented (1-4): "))
        NumDays = int(input("Enter how many days the car was rented for: "))
    else:
        break

    if NumDays <= 7:
        RentCost = NumDays * DailyRentalFee
    elif NumDays == 7:
        RentCost = WklyRentalRate
    else:
        break


    HST = RentCost * HST
    Total = HST + RentCost

    print("")
    print(f"HAB taxi service rental listing report")
    print(f"Was this a rented vehicle or was it an owner?: {RentOpt}")
    print("---------------------------------------------------------")
    print(f"Driver ID number:                              {DriverID:>4d}")
    print(f"Date of car rental:                            {PickUp}")
    print(f"Number of car that was rented:                 {CarNum:>1d}")
    print(f"Number of days vehicle was rented for:        {NumDays:>2d}")
    print("---------------------------------------------------------")
    print(f"Rental Cost:                                   {FV.FDollar2(RentCost)}")
    print("                                              ---------")
    print(f"HST Cost (@15%):                               {FV.FDollar2(HST)}")
    print("                                              ---------")
    print(f"Total cost after taxes:                        {FV.FDollar2(Total)}")

    f = open("Policies.dat", "a")
    f.write("{}, ".format(int(DriverID)))
    f.write("{}, ".format(RentOpt))
    f.write("{}, ".format(PickUp))
    f.write("{}, ".format(CarNum))
    f.write("{}, ".format(NumDays))
    f.write("{}\n, ".format(FV.FDollar2(Total)))
    f.close()
    print()
    print("Rental information processed abd saved.")
    DriverID += 1