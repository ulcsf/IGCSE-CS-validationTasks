score = 12345
high_score = 999999
lives = 2

#Based on the example on BBC Bitesize

print("Your score: " + str(score))
time.sleep(1)
print("High score: " + str(high_score))
time.sleep(1)
print("Lives remaining: " + str(lives))
time.sleep(1)


'''
Suppose you wanted to print out the player information at these different points in the game:

* at the end of a level
* when the player loses a life
* when the player beats the high score
* when the game is over
* You would need to repeat those six lines of code on each occasion, giving a total of 24 lines of code simply to display the player information:
'''


# End of level
print("Your score: " + str(score))
time.sleep(1)
print("High score: " + str(high_score))
time.sleep(1)
print("Lives remaining: " + str(lives))
time.sleep(1)

# Lose a life
print("Your score: " + str(score))
time.sleep(1)
print("High score: " + str(high_score))
time.sleep(1)
print("Lives remaining: " + str(lives))
time.sleep(1)

# New high score
print("Your score: " + str(score))
time.sleep(1)
print("High score: " + str(high_score))
time.sleep(1)
print("Lives remaining: " + str(lives))
time.sleep(1)

# Game over
print("Your score: " + str(score))
time.sleep(1)
print("High score: " + str(high_score))
time.sleep(1)
print("Lives remaining: " + str(lives))
time.sleep(1)


#This is repetitive and a waste of time. It would be better to write a procedure and simply run that procedure whenever it is needed.

