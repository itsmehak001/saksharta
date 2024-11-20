# variable to keep track 
amount_due = 50

# loop until amount_due is greater than 0
while amount_due > 0:
    # print the amount due 
     print("amount due: ", amount_due)
    # ask user to insert coin 
     coin = int(input("insert coin: "))
    # check if coin is 25,10 or 5 cents
     if coin in [25, 10, 5]:
        #subtract value from amount_due
        amount_due -= coin

# calculate change_owed
change_owed = abs(amount_due)
# print the result
print("change owed: ", change_owed)