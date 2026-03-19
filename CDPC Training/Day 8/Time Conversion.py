def timeConversion(s):
    hour = int(s[:2])
    period = s[-2:]
    rest = s[2:-2]

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}{rest}"


# 🔽 Main program 
s = input("Enter time (e.g., 07:05:45PM): ")

result = timeConversion(s)

print(result) 