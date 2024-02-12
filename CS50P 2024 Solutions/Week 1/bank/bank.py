input = input("Greeting: ").strip().lower()

if input.startswith("hello"):
    print("$0")
elif input[0] == "h":
    print("$20")
else:
    print("$100")
