input = input("camelCase: ")

output = ""
for c in input:
    if c.isupper():
        output += "_" + c.lower()
        continue
    output += c

print(f"snake_case: {output} ")
