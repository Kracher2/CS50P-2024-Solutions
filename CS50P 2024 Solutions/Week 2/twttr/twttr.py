inp = input("Input: ").strip()
outp = ""

for c in inp:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        outp += c

print(outp)
