# Extra report for additional expenses
import datetime
import FormatValues as FV

f = open("EfeatDefault.dat", "r")
GAS_PER_LT = float(f.readline())
WIN_WASH_PER = float(f.readline())
SEAS_TIRE_CHG = float(f.readline())
ROAD_ASSIST = float(f.readline())
REG_COST = float(f.readline())
f.close()

while True:
    InvDate = datetime.datetime.now()
    InvDateDsp = InvDate.strftime("%Y-%m-%d")
    FirstCarYear = input("Enter the year of vehicle 1: ")
    FirstCarMake = input("Enter the make of vehicle 1: ")
    FirstCarModel = input("Enter the model of vehicle 1: ")
    FirstCarInsCost = float(input("Enter the yearly cost of insurance: "))
    SecondCarYear = input("Enter the year of vehicle 2: ")
    SecondCarMake = input("Enter the make of vehicle 2: ")
    SecondCarModel = input("Enter the model of vehicle 2: ")
    SecondCarInsCost = float(input("Enter the yearly cost of insurance: "))
    ThirdCarYear = input("Enter the year of vehicle 3: ")
    ThirdCarMake = input("Enter the make of vehicle 3: ")
    ThirdCarModel = input("Enter the model of vehicle 3: ")
    ThirdCarInsCost = float(input("Enter the yearly cost of insurance: "))
    FourthCarYear = input("Enter the year of vehicle 4: ")
    FourthCarMake = input("Enter the make of vehicle 4: ")
    FourthCarModel = input("Enter the model of vehicle 4: ")
    FourthCarInsCost = float(input("Enter the yearly cost of insurance: "))
    AmtWinWash = int(input("Enter the amount of windshield wash used :"))
    SeasonalTire = input("Enter whether tires will be changed (Y or N): ")
    CarOneLt = float(input("Enter the litres needed to fill car 1: "))
    CarTwoLt = float(input("Enter the litres needed to fill car 2: "))
    CarThreeLt = float(input("Enter the litres needed to fill car 3: "))
    CarFourLt = float(input("Enter the litres needed to fill car 4: "))
    CarOneFills = float(input("Enter how many times car 1 was filled this month: "))
    CarTwoFills = float(input("Enter how many times car 2 was filled this month: "))
    CarThreeFills = float(input("Enter how many times car 3 was filled this month: "))
    CarFourFills = float(input("Enter how many times car 4 was filled this month: "))
    RegDue = input("Enter whether registration will be paid this month(Y or N): " )

    if SeasonalTire == "Y":
        TireCost = SEAS_TIRE_CHG * 4
    else:
        TireCost = 0

    TotMonIns = (FirstCarInsCost + SecondCarInsCost + ThirdCarInsCost + FourthCarInsCost)/12
    RoadAssistCost = (ROAD_ASSIST * 4)/12
    OneGas = (CarOneLt * CarOneFills) * GAS_PER_LT
    TwoGas = (CarTwoLt * CarTwoFills) * GAS_PER_LT
    ThreeGas = (CarThreeLt * CarThreeFills) * GAS_PER_LT
    FourGas = (CarFourLt * CarFourFills) * GAS_PER_LT
    TotGas = OneGas + TwoGas + ThreeGas + FourGas
    WinWashCost = AmtWinWash * WIN_WASH_PER

    if RegDue == "Y":
        RegTotal = REG_COST * 4
        print(f"Cost of yearly registration: {FV.FDollar2(RegTotal)}")
    else:
        RegTotal = 0

    MonCost = TotMonIns + RoadAssistCost + RegTotal + TireCost + TotGas + WinWashCost
    HST = MonCost * 0.15
    TotMonCost = MonCost + HST
    print("---------------------------------------------------------------------------------------")
    print("HAB taxi service extra expenses report")
    print(f"{InvDateDsp}")
    print("Car Year   Car Model   Car Make   Number of fills")
    print("---------------------------------------------------------------------------------------")
    print(f"{FirstCarYear:>4s} {FirstCarMake:<10s}   {FirstCarModel:<10s}     {CarOneFills:<2f}")
    print(f"{SecondCarYear:>4s} {SecondCarMake:<10s}   {SecondCarModel:<10s}     {CarTwoFills:<2f}")
    print(f"{ThirdCarYear:>4s} {ThirdCarMake:<10s}   {ThirdCarModel:<10s}     {CarThreeFills:<2f}")
    print(f"{FourthCarYear:>4s} {FourthCarMake:<10s}   {FourthCarModel:<10s}     {CarFourFills:<2f}")
    print("---------------------------------------------------------------------------------------")
    print(f"Monthly gas cost for vehicle 1:   {FV.FDollar2(OneGas)}")
    print(f"Monthly gas cost for vehicle 2:   {FV.FDollar2(TwoGas)}")
    print(f"Monthly gas cost for vehicle 3:   {FV.FDollar2(ThreeGas)}")
    print(f"Monthly gas cost for vehicle 4:   {FV.FDollar2(FourGas)}")
    print(f"Total monthly gas cost:           {FV.FDollar2(TotGas)}")
    if SeasonalTire == "Y":
        print(f"Cost of seasonal tire change: {FV.FDollar2(TireCost)}")
    else:
        break
    if RegDue == "Y":
        print(f"Cost of yearly registration: {FV.FDollar2(RegTotal)}")
    else:
        break
    print(f"Total monthly cost of roadside assistance: {FV.FDollar2(RoadAssistCost)}")
    print(f"Total monthly cost of windshield wash:     {FV.FDollar2(WinWashCost)}")
    if SeasonalTire == "Y":
        print(f"Cost of seasonal tire change:      {FV.FDollar2(TireCost)}")
    else:
        break
    if RegDue == "Y":
        print(f"Cost of yearly registration:       {FV.FDollar2(RegTotal)}")
    else:
        break
    print(f"Monthly cost pre tax:                     {FV.FDollar2(MonCost)}")
    print(f"HST cost:                                 {FV.FDollar2(HST)}")
    print(f"Total monthly cost:                       {FV.FDollar2(TotMonCost)}")
    print()

    f = open("ExtraFeat.dat", "a")
    f.write("{}, ".format(InvDateDsp)
    f.write("{}, ".format(FirstCarYear))
    f.write("{}, ".format(FirstCarMake))
    f.write("{}, ".format(FirstCarModel))
    f.write("{}, ".format(CarOneFills))
    f.write("{}, ".format(SecondCarYear))
    f.write("{}, ".format(SecondCarMake))
    f.write("{}, ".format(SecondCarModel))
    f.write("{}, ".format(CarTwoFills))
    f.write("{}, ".format(ThirdCarYear))
    f.write("{}, ".format(ThirdCarMake))
    f.write("{}, ".format(ThirdCarModel))
    f.write("{}, ".format(CarThreeFills))
    f.write("{}, ".format(FourthCarYear))
    f.write("{}, ".format(FourthCarMake))
    f.write("{}, ".format(FourthCarModel))
    f.write("{}, ".format(CarFourFills))
    f.write("{}, ".format(OneGas))
    f.write("{}, ".format(TwoGas))
    f.write("{}, ".format(ThreeGas))
    f.write("{}, ".format(FourGas))
    f.write("{}, ".format(TotGas))
    f.write("{}, ".format(TireCost))
    f.write("{}, ".format(RegTotal))
    f.write("{}, ".format(RoadAssistCost))
    f.write("{}, ".format(WinWashCost))
    f.write("{}\n ".format(TotMonCost))
    f.close()
    print()
    print("Monthly report processed and saved.")