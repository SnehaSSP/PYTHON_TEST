print("Welcome to the disney world")
height = int(input("enter your height in cm? "))

bill = 0
if height >= 120:
    print("can ride")
    age = int(input("enter your age "))
    if age < 12:
        print("child tickets are $ 5")
        bill = 5
    elif age <= 18:
        print("child tickets are $7")
        bill = 7
    else:
        print("child tickets are $12")
        bill = 12

    photos = input("want photos enter Y or N").lower()
    if photos == "y":
        bill += 3
    print("the total bill is ", bill)

else:
    print("can't ride")
