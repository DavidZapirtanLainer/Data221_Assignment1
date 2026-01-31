def number_of_seconds_to_time_in_day(number_seconds):
    # Using a conditional to only allow positive integers be used to find the time of day
    if not isinstance(number_seconds, int) or number_seconds < 0:
        return "INVALID INPUT. POSITIVE INTEGER NEEDED."

    #Taking out n factor of 86400 from the seconds as 86400 seconds is a day, and time of the resets
    if number_seconds >= 86400:
        number_seconds = number_seconds - int(number_seconds/86400)*86400

    #Taking out n factor of 43200 from the seconds as 43200 seconds is 12 hours, and the time on the clock resets at noon.
    #Furthermore, we also need to determine if it's AM or PM.
    if number_seconds >= 43200:
        meridiem = "PM"
        number_seconds -= 43200
    else:
        meridiem = "AM"

    #Using int to get the floor of the factor of hours into seconds so we know how many hours passed after midnight.
    #Then from the number_seconds we subtract the factored number of hours multiplied by 3600 (number of seconds in an hour)
    #This gives us the remaining seconds
    number_of_hours = int(number_seconds/3600)
    if number_of_hours > 0:
        number_seconds = number_seconds - (3600 * (number_of_hours))
        hour_on_the_clock = str(number_of_hours)
    else:
        hour_on_the_clock = 12

    # Using int to get the floor of the factor of minutes into seconds so we know how many minutes passed after the clock hour.
    # Then from the number_seconds we subtract the factored number of minutes multiplied by 60 (number of seconds in a minute)
    # This gives us the remaining seconds
    number_of_minutes = int(number_seconds/60)
    if number_of_minutes > 0:
        minutes_on_the_clock = str(number_of_minutes)
        number_seconds = number_seconds - (60 * (number_of_minutes))

    #Making number_of_minutes a string to add a 0 in front incase it is just one digit
    if number_of_minutes < 10:
        minutes_on_the_clock = "0" + str(number_of_minutes)
    else:
        minutes_on_the_clock = str(number_of_minutes) #Setting it to 00 to follow the format of a clock

    seconds_on_the_clock = str(number_seconds)
    if seconds_on_the_clock == "0":
        seconds_on_the_clock += "0"


    # Returning an f-string with all the string variables to put it in the proper format
    display = f"{hour_on_the_clock}:{minutes_on_the_clock}:{seconds_on_the_clock} {meridiem}"
    return display

#Example of the function
example_number_of_seconds = 6000
print(number_of_seconds_to_time_in_day(example_number_of_seconds))





