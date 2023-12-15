print("welcome if you python pizza!")
size = input("enter the pizza size")
pepperoni = input("do you want pepperoni")
extra_cheese = input("do you want extra cheese")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill = bill + 2

    else:
        bill = bill + 3


if extra_cheese == "Y":
    bill = bill + 1
print("your final bill is ", bill)