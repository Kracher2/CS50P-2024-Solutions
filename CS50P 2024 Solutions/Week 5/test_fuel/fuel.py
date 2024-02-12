def main():
    inp = input("Fraction: ")
    perc = convert(inp)
    tank = gauge(perc)
    print(tank)


def convert(fraction):
    try:
        x, y = fraction.strip().split("/")
        if int(x) > int(y) or int(x) < 0 or int(y) < 0:
            raise ValueError
        return int(x) / int(y) * 100
    except (ValueError, ZeroDivisionError, TypeError) as Error:
        if Error == TypeError:
            raise ValueError
        raise Error


def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{round(percent)}%"


if __name__ == "__main__":
    main()
