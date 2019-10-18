import time
'''
**********************************************************************
Course Module Selector

This example is to demonstrate the use of loops, flags and decisions

--------------------------------------------------------------------------
Please note that this is by no means the best or only way of doing things!
This is also not a 'true' program and would not really be all that useful 
in a real situation!  Demo purposes only!!!
**********************************************************************
'''

# Setup the initial lists
moduleCode = [
  "COMP116",
  "COMP101",
  "COMP124",
  "COMP108",
  "COMP107",
  "COMP109",
  "COMP111",
  "COMP122",
  "COMP105",
  "COMP123",
  ]
moduleList = [
  "Analytic Techniques for Computer Science",
  "Introduction to Programming",
  "Computer Systems",
  "Data Structures and Algorithms",
  "Designing Systems for the Digital Society",
  "Foundations of Computer Science",
  "Introduction to Artificial Intelligence",
  "Object-oriented Programming",
  "Programming Language Paradigms",
  "Intoduction Database Development"
  ]

# Declare other variables
moduleChoices = []
selectionComplete = "N"

while selectionComplete == "N":                             #Set up the "main loop"
    print("""
    ************************************************
    Welcome to the University module selector
    
    ------------------------------------------------
    You are required to make your module selection 
    for semester one. 

    Press ENTER to begin
    """)
    input()
  
    print("Please select 4 modules from the list")
    print("  -  Please only enter the module code  - ")
    print()

    # Print information to user 
    for i in range(0, len(moduleCode)):
        print(moduleCode[i], " - ", moduleList[i])
    print()

    #Collect input from user
    for i in range(4):
        print("Please select module",i+1)
        validSelection = False                      #Flag for loop to allow user to re-enter if incorrect
        while validSelection == False:
            choice = input(">> ").upper()
            if choice not in moduleCode:
                print("Invalid selection. Please choose again.")
            elif choice == "":
                print("No module selected. Please choose again.")
            elif choice in moduleChoices:
                print("You have already selected this module. Please choose again.")
            else:
                validSelection = True
                moduleChoices.append(choice)

    #Output users input for user verification
    print()
    print("Your module choices are: ")
    print(moduleChoices)
    print()
    
    print("Is this correct? [Y/N]")
    selectionComplete = input(">> ").upper()
    
    if selectionComplete == "N":
        moduleChoices = []
        print("Plese reselect your modules.")
        time.sleep(3)                               #Just to make this text script a bit prettier/more 'realistic'
    elif selectionComplete == "Y":
        print("""Thank you. Your module chocie have been submitted. 
        You will recieve confirmation of your timetable in 1 - 3 days via email.""")
        input("Please press ENTER to reset for the next student")
        selectionComplete = "N"                         
        moduleChoices = []                          #REset ready for next user
        time.sleep(3)

        