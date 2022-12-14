# main branch. used for calling our functions within other files.
# authors: A.Singleton S.Fifeild I.Doyle M.Mouland J.Lodge
# start: 2022-10-21
#####################################################

#####################################################
# imports
# we will use this as the main branch of our program.
# import somethingOldSomethingNew
# import coolStuff
# import employeeTravelClaim
# import funInterviewQuestion
# import datetime

#####################################################
# Functions

"""
displayMenu() displays to user a menu of executables
they can use in our program
"""


def DisplayMenu():
    print(f"""

        {"m    m   mm   mmmmm":^40}
        {"#    #   ##   #    #":^40}
        {'#mmmm#  #  #  #mmmm"':^40}
        {"#    #  #mm#  #    #":^40}
        {'#    # #    # #mmmm"':^40}

        {"Company Services System":^40}
        ----------------------------------------
        {"1. Enter a new Employee":<40}
        {"2. Enter Company Revenues":<40}
        {"3. Enter Company Expenses":<40}
        {"4. Track Car Rentals":<40}
        {"5. Record Employee Payment":<40}
        {"6. Print Company Profit Listing":<40}
        {"7. Print Driver Financial Listing":<40}
        {"8. Your Report - we will create this.":<40}
        {"9. Exit program ":<40}

    """)
    return input("Enter Option: ")

#####################################################
# process display menu receive user input
Run = True
while Run:  # Main loop

    while True:
        tmp = DisplayMenu()
        if tmp == "1":

        elif tmp == "2":

        elif tmp == "3":

        elif tmp == "4":

        elif tmp == "5":

        elif tmp == "6":

        elif tmp == "7":

        elif tmp == "8":

        elif tmp == "9":

        else:
            input("invalid input, Please enter a valid option - press enter to continue...")

