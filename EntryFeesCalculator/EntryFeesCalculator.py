#Aqua Park - Entry Fees Calculator - www.101computing.net/entry-fees-calculator-using-a-flowchart/ 

adultPrice = 15
childPrice = 11
discount = 5        #Discount as %age

adultTickets = input("How many ADULT tickets do you require: ")
childTickets = input("How many CHILD tickets do you require: ")
totalCost = (int(adultTickets) * adultPrice) + (int(childTickets) * childPrice)
if totalCost > 50:
    totalCost = totalCost * (1-(discount/100))
print("Your total cost is: £",round(float(totalCost),2))