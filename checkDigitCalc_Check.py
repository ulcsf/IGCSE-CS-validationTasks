'''
*********************************
Check digit Calculator
based on the calulation in IGCSE Computer Science text book
**********************************
'''
import time
userContinue = "N"
userChoice = "M"
oddDigits = 0
evenDigits = 0


while userChoice.upper() == "M":
    print("""   ***********************************************************
    Welcome to the check digit calculator and checking program
    ***********************************************************

    Please pick an option:

    1  -  Calculate a new check digit
    2  -  Check validity of an ISBN
    X  -  Exit

    """)

    userChoice = input()
    while userChoice.upper() != "X":

        if userChoice == "1":
            newCode = input("Enter the code that requires a check digit: ")
            while userContinue.upper() == "N":
                while not newCode.isdigit() or len(newCode) != 12:          # Begin validating the user input
                    print("You must enter 12 numbers!")
                    newCode = input("Enter the code that requires a check digit: ")
                print("You entered: ", newCode)
                userContinue = input("Is that correct? (Y/N): ")
            #Start of the calculation
            '''
            To calculate the check digit the odd positioned digits (i.e. position 1, 3, 5...) are added together
            Then the even postions are added together and multiplied by 3.
            These two values are added together and divided by 10
            If there is 0 remaining, 0 is the check digit.
            Otherwise the remainder is subtracted from 10
            '''
            for i in range(0,12,2):
                oddDigits = oddDigits + int(newCode[i])
            for i in range(1,12,2):
                evenDigits = evenDigits + int(newCode[i])

            digitsTotal = oddDigits + (evenDigits * 3)
            checkDigit = digitsTotal % 10

            #show the user the check digit
            if checkDigit == 0:
                print("Check Digit = 0")
            else:
                checkDigit = 10-checkDigit
                print("Check Digit = ", checkDigit)
                
            #save it as the new ISBN
            isbn = newCode + str(checkDigit)
            print()
            print("Your new ISBN is ", isbn)
            print()
            time.sleep(2)
            print("""Please select an option:

            1 - Calculate new check digit
            M - Return to menu""")
            userChoice = input()
            if userChoice.upper() == "M":
                break
            

print("Byeeee")