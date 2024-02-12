coke = 50

while coke > 0:
    insert = int(input("Insert Coin: "))
    if insert in [25, 10, 5]:
        coke -= insert
    if coke <= 0:
        print(f"Change Owed: {abs(coke)}")
    else:
        print(f"Amount Due: {coke}")
