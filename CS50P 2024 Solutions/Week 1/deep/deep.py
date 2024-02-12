input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

if input.strip().lower() in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")
