# get user input
answer = input ("Greeting: ")

new_answer = answer.lower().strip()

# check if the answer has 'hello' , print $0
if 'hello' in new_answer:
    print("$0")
# check if anwer starts with 'h' , print $20
elif 'h' == new_answer[0]:
    print("$20")

# otherwise 
