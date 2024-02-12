import sys

try:
    file = open(sys.argv[1])
    file.close()
except IndexError:
    sys.exit("Please specify filename")
except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} not found")

if not sys.argv[1].endswith(".py"):
    sys.exit(f"{sys.argv[1]} does not end with .py")
if len(sys.argv) != 2:
    sys.exit("Too many arguments")

rows = 0
with open(sys.argv[1]) as file:
    for row in file:
        if not (row.strip().startswith("#") or row.strip() == ""):
            rows += 1

print(rows)
