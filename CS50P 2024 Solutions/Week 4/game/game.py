import random

while True:
    try:
        lvl = int(input("Level: ").strip())
        if lvl >= 0:
            break
    except ValueError:
        pass

num = random.randint(0, lvl)

while True:
    try:
        guess = int(input("Guess: ").strip())
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
