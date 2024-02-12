import random


def main():
    score = 0
    lvl = get_level()
    for _ in range(10):
        x = gen_int(lvl)
        y = gen_int(lvl)
        for i in range(3):
            try:
                inp = int(input(f"{x} + {y} = "))
                if inp == x + y:
                    score += 1
                    break
                print("EEE")
                if i == 2:
                    print(f"{x} + {y} = {x + y}")
            except ValueError:
                print("EEE")
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            lvl = int(input("Level: ").strip())
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass


def gen_int(lvl):
    min = 0 if lvl == 1 else 10 ** (lvl - 1)
    max = 10**lvl - 1
    return random.randint(min, max)


if __name__ == "__main__":
    main()
