import time

#SECTION 1
toppings = ["Pepperoni","Chicken","Extra cheese","Mushrooms","Spinach","Olives"]
baseSizes = ["Small","Medium","Large"]
baseTypes = ["Thin","Thick"]

customerSize = -1
customerType = -1
orderNumber = 100
newOrder = ""

while True:                                         
    #welcome message
    print("""   
    Hi, welcome to the Pizza Ordering Service.

    Please follow the on-screen prompts to place your order.

    Press return/enter to continue...
    """)
    input()                                         

    orderComplete = "N"                             
    
    while orderComplete == "N":                    
        custTopChoices = []                         
        print("What size pizza would you like?")
        for i in baseSizes:
            print(i)
        while True:
            print()
            customerSize = (input(">> ")).capitalize()
            if customerSize not in baseSizes:
                print("You must enter a valid option: ")
                print(baseSizes)
            else:
                break
        print("""
        **** Thank you. ****
        What type of base would you like?
        """)

#SECTION 2
        for i in baseTypes:                
            print(i)
        while True:
            print()
            customerType = (input(">> ")).capitalize()
            if customerType not in baseTypes:
                print("You must enter a valid option: ")
                print(baseTypes)
            else:
                break

#SECTION 3:
        extraToppings = "N"
        print("""
        ****  Thank you.  ****
        Your pizza comes with cheese and tomato.
        Would you like to add extra toppings?
        
        """)
        extraToppings = input("Enter Y or N: ").upper()         
        if extraToppings == "Y":
            print()
            print("You can add up to 3 additonal toppings.")
            while len(custTopChoices) < 3:
                print("You have added",len(custTopChoices),"toppings.")
                print("---")
                print("Please select a topping: ")
                for i in toppings:
                    print("*",i)
                print("N - end selection\n")
                choice = input("Enter your option or N to end selection: ").capitalize()
                print()
                if choice in toppings:
                    custTopChoices.append(choice)
                elif choice == "N":
                    break
                else:
                    print("** Sorry, that is not an option. Try again!** \n")
                    time.sleep(1)

# SECTION 4
        print("""Thank you. 
        Please review your choices and confirm your order: 

        *****YOUR ORDER ****""")
        print("Size:",customerSize)
        print("Type:",customerType)
        print("""Toppings:
        - Cheese
        - Tomato""")
        for i in custTopChoices:
            print("        -",i)
        orderComplete = input("""Is your order correct? 
        'Y' to complete your order
        'N' to re-enter you choices
        >> """).upper()
        
        if orderComplete == "N":
            print("Please re-enter your order")
            time.sleep(1)
        elif orderComplete == "Y":
            print("Thank you! Your order number is:", orderNumber)
            orderNumber += 1
            time.sleep(3)
            print("Your order will be ready soon. Please come back soon.")
            time.sleep(2)
    newOrder = input("Press ENTER to start a new order ").upper()

