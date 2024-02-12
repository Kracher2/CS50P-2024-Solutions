import inflect

inf = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: ").strip())
    except EOFError:
        break

print(f"Adieu, adieu, to {inf.join(names)}")
