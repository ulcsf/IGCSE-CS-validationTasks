'''
****************************************************************************************
Based on the challenge set at https://www.101computing.net/my-e-mail-validation-script/
****************************************************************************************

Some of the validation checks that your program should complete are as follows:

* The email should contain one and only one “@” sign
* The email should contain at least one “.” sign located after the “@” sign. 
      - However it may contains more than one “.” sign for emails ending in .co.uk for instance
* The email cannot contain any space or “#” signs
* The “@” sign cannot be in the first position and there should be at least 1 character between the “@” and the “.” sign.
* The email cannot end with a “.” sign

'''

myEmail="@john@google.com"
#We could use an input to retrive an email from the end user
#However we are going to input the email into the code as it will make testing easier.
atSignPosition=-1
atSignCount = 0
invalidChars = 0

for i in range(0,len(myEmail)):
    if myEmail[i]=="@":
        atSignPosition=i
        atSignCount += 1
    if myEmail[i]=="#" or myEmail[i]==" ":
        invalidChars += 1

if atSignPosition>0:
  if myEmail[atSignPosition+1] == "@" or myEmail[atSignPosition+1] == ".":
  	print("This is NOT a valid e-mail address (does not contain letter/number after @)")
  elif invalidChars > 0:
    print("This is NOT a valid e-mail address - contains invalid characters/spaces")
  elif myEmail[-1] == ".":
    print("This is NOT a valid e-mail address - ends with .") 
  elif atSignCount > 1:
    print("This is NOT a valid e-mail address - cannot have more than 1 @")
  else:
  	print("This seems to be a valid e-mail address")
else:
	print("This is NOT a valid e-mail address - cannot start with @")
	