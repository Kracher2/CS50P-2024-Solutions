from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

if len(argv) not in [1, 3]:
    exit("Usage: filename.py -f font")
if len(argv) == 3:
    if argv[-2] not in ["-f", "--font"]:
        exit("Please only use -f or --font")
    if argv[-1] not in figlet.getFonts():
        exit("Font not found")

inp = input("Input: ").strip()

if len(argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
else:
    figlet.setFont(font=argv[-1])

print(figlet.renderText(inp))
