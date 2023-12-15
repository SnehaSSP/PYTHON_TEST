print("Welcome! Tip Calculator")
bill = float(input("enter the total bill in dollar? $"))
percentage_tip = int(input("how much percentage you will like to give"))
after_tip = bill + (percentage_tip * bill) / 100
print(after_tip)

bill_split = int(input("how many people to split the bill"))
each_person_pay = after_tip/bill_split
print(round(each_person_pay, 2))
print("{:.2f}".format(each_person_pay))

