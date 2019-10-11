#Is My Credit Card Number Valid? - www.101computing.net/is-my-credit-card-valid/

cardNumber = input("Enter a 16-digit card number (without spaces):")
print(cardNumber)

#Complete the code here to implement the Luhn Algorithm
cardNumber = cardNumber.replace(" ","")
cardNumber = cardNumber.replace("-","")
print(cardNumber)
while not cardNumber.isnumeric() or len(cardNumber) !=16:
        print("Invalid number: You must enter 16 digits")

        cardNumber = input("Enter a 16-digit card number (without spaces):")
print("Valid Entry (16 digits)")