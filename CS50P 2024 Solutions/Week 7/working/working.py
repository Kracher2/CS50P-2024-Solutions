import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start, end = s.split(" to ")
    return format(start) + " to " + format(end)


def format(s):
    time, zone = s.split()
    if not ":" in time:
        time = time + ":00"
    hour, minute = time.split(":")
    if int(hour) > 12 or int(hour) < 0 or int(minute) > 59 or int(minute) < 0:
        raise ValueError
    if int(hour) == 12:
        if zone == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if zone == "PM":
            hour = int(hour) + 12
    hour = f"{int(hour):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
