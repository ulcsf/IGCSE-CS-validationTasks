import time
'''
TASK 1 – Design your pizza. 
The customer is given choices of size, base and additional toppings (number and type) as stated above. 
Only valid choices can be accepted. The customer is asked to confirm their order or alter their 
choices or not proceed. If the customer confirms their order they are given a unique order number.
'''
#Lists to the options for the user 
toppings = ["Pepperoni","Chicken","Extra cheese","Mushrooms","Spinach","Olives"]
baseSizes = ["Small","Medium","Large"]
baseTypes = ["Thin","Thick"]

customerSize = -1
customerType = -1
#custTopChoices = []

pizzasOrdered = 0
baseSizeOrders = [0, 0, 0]
baseTypeOrders = [0, 0]
toppingOrders = [0, 0, 0, 0, 0, 0]


orderNumber = 100
newOrder = ""

#while newOrder != "X":                          #Begin the 'main loop' for this code. 
while True:                                         # Why have I used this instead of the "while" above?  Which method do you think is better?
    print("""   
    Hi, welcome to the Pizza Ordering Service.

    Please follow the on-screen prompts to place your order.

    Press return/enter to continue...
    """)
    input()                                         #Pause the program whilst waiting for the user to press enter

    orderComplete = "N"                             #Flag to allow repetiton of the process 
    while orderComplete == "N":                     # Begin the mian ordering process
        custTopChoices = []                         #Clear customer toppin choices list - needed otherwise the new customer gets a copy of the old items!
        #BEGIN SIZE SELECTION:
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
        #BEGIN BASE TYPE SELECTION:
        for i in baseTypes:               #iterate through types to length of the list. 
            print(i)
        while True:
            print()
            customerType = (input(">> ")).capitalize()
            if customerType not in baseTypes:
                print("You must enter a valid option: ")
                print(baseTypes)
            else:
                break
        #BEGIN TOPPING SELECTION:
        extraToppings = "N"
        print("""
        ****  Thank you.  ****
        Your pizza comes with cheese and tomato.
        Would you like to add extra toppings?
        
        """)
        extraToppings = input("Enter Y or N: ").upper()         #The user might not want extra toppings...so why not ask them?!
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

            pizzasOrdered += 1

            if customerSize == "Small":
                baseSizeOrders[0] += 1
            elif customerSize == "Medium":
                baseSizeOrders[1] += 1
            elif customerSize == "Large":
                baseSizeOrders[2] += 1

            if customerType == "Thin":
                baseTypeOrders[0] += 1
            elif customerType == "Thick":
                baseTypeOrders[1] += 1

            for topping in custTopChoices:
                if topping == "Pepperoni":
                    toppingOrders[0] +=1
                elif topping == "Chicken":
                    toppingOrders[1] +=1
                elif topping == "Extra cheese":
                    toppingOrders[2] +=1
                elif topping == "Mushrooms":
                    toppingOrders[3] +=1
                elif topping == "Spinach":
                    toppingOrders[4] +=1
                elif topping == "Olives":
                    toppingOrders[5] +=1

    print("Number of pizzas ordered:", pizzasOrdered)
    print("Base Sizes: ")
    for i in range(0, len(baseSizeOrders)):
        print(baseSizes[i], "-", baseSizeOrders[i])

    print("\nBase Types: ")
    for i in range(0, len(baseTypeOrders)):
        print(baseTypes[i], "-", baseTypeOrders[i])

    print("\nToppings: ")
    for i in range(0, len(toppings)):
        print(toppings[i], "-", toppingOrders[i])




    newOrder = input("Press ENTER to start a new order ").upper()
    
    #if newOrder == "X":
    #    break

