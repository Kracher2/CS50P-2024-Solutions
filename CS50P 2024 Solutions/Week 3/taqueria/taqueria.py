meal = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0
while True:
    try:
        inp = input("Item: ").strip().title()
        if inp not in meal:
            raise KeyError
    except EOFError:
        print()
        break
    except KeyError:
        pass
    else:
        total += meal[inp]
        print(f"Total: ${total:.2f}")
