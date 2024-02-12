def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    executed = False
    if not s[:2].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    for i in range(len(s)):
        if s[i].isdigit() and not executed:
            executed = True
            if not s[i : len(s) + 1].isdigit() or s[i] == "0":
                return False
        if s[i] in [".", " ", "?", "!"]:
            return False
    return True


if __name__ == "__main__":
    main()
