x, y, z = input("Expression: ").strip().split()

x, z = float(x), float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)
