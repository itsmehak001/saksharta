# get user input 
answer = input("what is the answer to the greate question of life , the universe and everything? ")

# print yes if the user inputs 42 or (case-insensitivety) fourty-two or fourty two
if answer == "42":
    print("yes")
elif answer.lower() == "fourty-two":
    print("yes")
elif answer.lower() == "fourty two":
    print("yes")
# otherwise output no
