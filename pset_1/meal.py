def main():
    # get time from user
    answer = input("what time is it? ")
    # call the convert function 
    time = convert(answer)
    # breakfast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("breakfast")
    # lunch between 12:00 and 13:00
    if time >= 12 and time <= 12:
        print("lunch time")
    # dinner between 18:00 and 19:00
    if time >= 18 and time <= 19:
        print("dinner time")
def convert(time):
    # gett hour and minute
    hours, minutes = time.split(":")
    # convert time into a float number
    new_minute = float(minutes) / 60
    # return the result to main function 
    return float (hours) + new_minute

if __name__ == "__main__":
    main()