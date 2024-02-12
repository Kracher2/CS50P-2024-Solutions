def main():
    percent = get_input()
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{round(percent)}%")


def get_input():
    while True:
        try:
            x, y = input("Fraction: ").strip().split("/")
            if int(x) > int(y):
                raise ValueError
            return int(x) / int(y) * 100
        except (ValueError, ZeroDivisionError):
            pass


main()
