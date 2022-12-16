#Driver Receipt Report

import datetime
import FormatValues as FV


print("HAB Taxi Services")
print(f"Driver Receipt for {FV.FDateS(InvoiceDate)}")
print(f"Reasoning for Receipt:        {ReceiptReason}")
print("—-------------------------------------------------")
print(f"Rental ID: Driver Number: Car Number: Days Rented: ")
print(f"  {RentalID:>4d}        {DriverNum:>4d}         {CarNum:>4d}         {DaysRented:>4d}")
print("—-------------------------------------------------")
print(f"Rental Cost :                            {FV.FDollar2(RentalCost):>9f}")
print(f"HST Cost (15%):                          {FV.FDollar2(HST):>9f}")
print(f"Total Cost (Rental Cost Plus HST):       {FV.FDollar2(TotalCost):>9f}")
print(f"Monthly Standard Fee for Vehicle Owners: {FV.FDollar2(MonthlyStdFee):>9f}")
print(f"Amount Paid:                             {FV.FDollar2(AmountPaid):>9f}")
print(f"Transaction Cost:                        {FV.FDollar2(TransCost):>9f}")
print("                                          --------")
print(f"Balance Due:                             {FV.FDollar2(BalDue):>9f}")
print("                                          --------")
print(f"HST:                                     {FV.FDollar2(HST):>9f}")
print("                                          --------")
print(f"Total:                                   {FV.FDollar2(Total):>9f}")
print("—-------------------------------------------------")
print(f"Amount Paid:                             {FV.FDollar2(AmountPaid):>9f}")
print("                                          --------")
print(f"Amount Owing on Account:                 {FV.FDollar2(BalDue):>9f}")