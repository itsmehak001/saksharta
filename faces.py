def main():
    # Get user input
    msg = input()
    #call convert function
    result = convert(msg)
    # print the result
    print(result)

def convert(msg):
    # Replace :) for happy emoji
    msg1 = msg.replace(":)", '🙂')
    # Replace :( for sad emoji
    msg2 = msg1.replace(":(",'🙁')
    # Return string
    return msg2

main()