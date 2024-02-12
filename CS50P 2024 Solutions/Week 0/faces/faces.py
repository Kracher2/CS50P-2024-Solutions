def main():
    word = input("Input: ")
    word = convert(word)
    print(word)


def convert(word):
    return word.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()
