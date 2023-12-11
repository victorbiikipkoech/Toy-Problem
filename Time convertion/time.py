def convert_to_24_hour_format(hour, minute, period):
    if period.lower() == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    # Format the result as HHMM
    return "{:02d}{:02d}".format(hour, minute)

# Example usage:
hour = 8
minute = 30
period = "am"
result = convert_to_24_hour_format(hour, minute, period)
print(result)  # Output: 0830

hour = 8
minute = 30
period = "pm"
result = convert_to_24_hour_format(hour, minute, period)
print(result)  # Output: 2030
