import sys
import csv

try:
    file = open(sys.argv[1])
    file.close()
except IndexError:
    sys.exit("Please specify filename")
except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} not found")

if len(sys.argv) != 3:
    sys.exit("Usage: scourgify.py input_file.csv output_file.csv")

people = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)

with open(sys.argv[2], "w") as file:
    header = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for person in people:
        last, first = person["name"].split(", ")
        writer.writerow({"first": first, "last": last, "house": person["house"]})
