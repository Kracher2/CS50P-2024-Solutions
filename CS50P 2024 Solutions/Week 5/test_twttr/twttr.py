def main():
    inp = input("Input: ").strip()
    outp = shorten(inp)
    print(outp)


def shorten(word):
    outp = ""
    for c in word:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            outp += c
    return outp


if __name__ == "__main__":
    main()
