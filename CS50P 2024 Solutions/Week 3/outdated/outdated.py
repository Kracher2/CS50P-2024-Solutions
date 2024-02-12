months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    try:
        inp = input("Date: ").strip().title()
        if "/" in inp:
            month, day, year = inp.split("/")
        else:
            month, day, year = inp.split()
            day = day[: len(day) - 1]
            month = months.index(month) + 1
        day, month, year = int(day), int(month), int(year)
        if month > 12 or day > 31:
            raise KeyError
        print(f"{year:04}-{month:02}-{day:02}")
        break
    except (KeyError, ValueError):
        pass
