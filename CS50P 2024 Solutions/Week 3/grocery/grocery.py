list = {}

while True:
    try:
        thing = input().strip().upper()
        list[thing] += 1
    except EOFError:
        list = dict(sorted(list.items()))
        print()
        for item in list:
            print(f"{list[item]} {item}")
        break
    except KeyError:
        list[thing] = 1
