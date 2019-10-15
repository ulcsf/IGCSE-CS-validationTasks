a = input("Hour: ")
if not a.isnumeric():
    print("error")

b = input("Mins: ")
c = input("AM or PM: ")
d = ":"

print(a+d+b+c)
