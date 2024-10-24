def get_day_of_week(number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    return days_of_week.get(number, "Invalid input")

number = int(input("Enter a number (1 to 7) to get the corresponding day of the week: "))

day = get_day_of_week(number)
print(day)