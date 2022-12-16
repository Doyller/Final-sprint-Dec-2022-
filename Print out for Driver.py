#Print Out For Driver

import datetime
import FormatValues as FV

print("       Driver Financial listing")
print("—-----------------------------------")
print(f"Driver Number:                  {DriverNum:>4d}")
print(f"Start date:                {FV.FDateS(InvoiceDate):>9}")
print(f"End date:                  {FV.FDateS(EndDate):>9}")
print(f"Daily Rental Fee:          {FV.FDollar2(DailyRentFee):>9f}")
print(f"Weekly Rental Fee:         {FV.FDollar2(WeekRentFee):>9f}")
print("                             --------")
print(f"Monthly Standard Fee:      {FV.FDollar2(MonthStandFee):>9f}")
print(f"Transaction Cost:          {FV.FDollar2(Cost):>9f}")
print(f"Balance Due:               {FV.FDollar2(Due):>9f}")
print("                             --------")
print(f"HST:                       {FV.FDollar2(HST):>9f}")
print(f"Total:                     {FV.FDollar2(Total):>9f}")
