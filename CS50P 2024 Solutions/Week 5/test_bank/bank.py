def main():
    inp = input("Greeting: ")
    outp = value(inp)
    print(f"${outp}")


def value(inp):
    inp = inp.strip().lower()
    if inp.startswith("hello"):
        return 0
    elif inp[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
