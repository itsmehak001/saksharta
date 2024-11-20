# get user input
answer = input("input: ")
# print "output: "
print("output: ", end= "")
# loop through every letter
for letter in answer:
    # check if it is not vowels whether inputted in upper case or lowercase
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u',]:
            # print the letter 
            print(letter, end="")
            # print new line
            print()