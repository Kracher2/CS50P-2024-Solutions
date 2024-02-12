from tabulate import tabulate
import sys
import csv

try:
    file = open(sys.argv[1])
    file.close()
except IndexError:
    sys.exit("Please specify filename")
except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} not found")

if not sys.argv[1].endswith(".csv"):
    sys.exit(f"{sys.argv[1]} does not end with .csv")
if len(sys.argv) != 2:
    sys.exit("Too many arguments")

menu = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        menu.append(row)

print(tabulate(menu, tablefmt="grid", headers="keys"))
