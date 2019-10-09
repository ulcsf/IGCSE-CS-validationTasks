#Aqua Park - Entry Fees Calculator - www.101computing.net/entry-fees-calculator-using-a-flowchart/ 

adultPrice = 15
childPrice = 11
discount = 5        #Discount as %age

while True:
    try:
        adultTickets = int(input("How many ADULT tickets do you require: "))
        while adultTickets < 0:
            print("You must enter a valid number")
            adultTickets = int(input("How many ADULT tickets do you require: "))
        break
    except ValueError:
        print("You must enter a whole number 0 and higher")
while True:
    try:
        childTickets = int(input("How many CHILD tickets do you require: "))
        while childTickets < 0:
            print("You must enter a valid number")
            childTickets = int(input("How many CHILD tickets do you require: "))
        break
    except ValueError:
        print("You must enter a whole number 0 and higher")

totalCost = (adultTickets * adultPrice) + (childTickets * childPrice)
if totalCost > 50:
    totalCost = totalCost * (1-(discount/100))
print("Your total cost is: £",round(float(totalCost),2))