#Printer Spacing Chart

import datetime
import FormatValues as FV

print("HAB Taxi Company")
print(f"Profit Listing from {FV.FDateS(ProfitStartDate)} to {FV.FDateS(ProfitEndDate)}")
print("-------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("Transaction ID.     Transaction Date.     Invoice Number.     Driver Number.     Item Number.     Quantity.     Revenue Amount.")
print("")
print(f"     {TransID:>4d}                  {FV.FDateS(TransDate)}                    {InvoiceNum}                  {DriverNum:>4d}               {ItemNum:>4d}          {Quantity:>3d}               {FV.FDollar2(RevenueAmount):>9f}")
print("")
print(f"     {TransID:>4d}                  {FV.FDateS(TransDate)}                    {InvoiceNum}                  {DriverNum:>4d}               {ItemNum:>4d}          {Quantity:>3d}               {FV.FDollar2(RevenueAmount):>9f}")
print("-------------------------------------------------------------------------------------------------------------------------------")
print("")
print(f"Revenues Listed:                                                                                                      {FV.FDollar2((RevenueAmount):>9f}")
print("                                                                                                                       --------")
print(f"HST:                                                                                                                  {FV.FDollar((HST):>9f}")
print("                                                                                                                       --------")
print(f"Total Revenue plus HST:                                                                                               {FV.FDollar2(RevenueAmount) + FV.FDollar2(HST):>9f}")
print("                                                                                                                       --------")
print(f"Calculated Profit:                                                                                                    {FV.FDollar2(Profit):>9f}")
