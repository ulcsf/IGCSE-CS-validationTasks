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

print("""
Hi, welcome to the Pizza Ordering Service.

Please follow the on-screen prompts to place your order.

Press return/enter to continue...
""")
input()

orderComplete = "N"                             #Flag to allow repetiton of the process 
while orderComplete == "N":                     #
    orderComplete = False
    print("""What size pizza would you like?
    Enter the option number:""")
    for i in range(0,len(baseSizes)):           #iterate through sizes to length of the list. 
        print(i, "-", baseSizes[i])
    customerSize = int(input())

    print("""Thank you. 
    What type of base would you like?
    Enter the option number:""")
    for i in range(0,len(baseTypes)):
        print(i, "-", baseTypes[i])
    customerType = int(input())

    extraToppings = "N"

    print("""Thank you. 
    Your pizza comes with cheese and tomato.
    Would you like to add extra toppings?""")
    extraToppings = input("Enter Y or N: ")

    if extraToppings == "Y":
        custTopChoices = []
        print("You can add up to 3 additonal toppings.")
        while len(custTopChoices) < 3:
            print("You have added",len(custTopChoices),"toppings.")
            print("Please select a topping: ")
            for i in range(0,len(toppings)):
                print(i, "-", toppings[i])
            print()
            print("N - end selection")
            choice = input("Enter your option or N to end selection: ")
            if choice.isnumeric():
                custTopChoices.append(int(choice))
            elif choice == "N":
                break

    print("""Thank you. 
    Please review your choices and confirm your order: 

    *****YOUR ORDER ****""")
    print("Size:",baseSizes[customerSize])
    print("Type:",baseTypes[customerType])
    print("""Toppings:
    - Cheese
    - Tomato""")
    for i in custTopChoices:
        print(" -",toppings[i])

    orderComplete = input("""Is your order correct? 
    'Y' to complete your order
    'N' to re-enter you choices
    >> """)
    
print("""
Thank you!
Your order number is: """)
