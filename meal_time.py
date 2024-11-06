def meal_time(time):
    """Determines the meal time based on the input time."""

    if "07:00" <= time < "10:00":
        return "Breakfast time"
    elif "12:00" <= time < "14:00":
        return "Lunch time"
    elif "19:00" <= time < "21:00":
        return "Dinner time"
    else:
        return "Not a meal time"

while True:
    time = input("Enter the time (HH:MM): ")
    if not time:  # Exit if the user enters an empty input
        break

    print(meal_time(time))