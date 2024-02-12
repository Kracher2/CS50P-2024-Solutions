import sys
from PIL import Image, ImageOps

try:
    file = open(sys.argv[1])
    file.close()
except IndexError:
    sys.exit("Please specify filename")
except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} not found")

if sys.argv[1].lower()[-4:] not in [".jpg", ".jpeg", ".png"]:
    sys.exit(f"{sys.argv[1]} does not have the right file format")
if len(sys.argv) != 3:
    sys.exit("Usage: shirt.py input_image output_image")
if not sys.argv[1].lower()[-4:] == sys.argv[2].lower()[-4:]:
    sys.exit("File formats do not match")

with Image.open(sys.argv[1]) as image:
    with Image.open("shirt.png") as shirt:
        edited = ImageOps.fit(image, shirt.size)
        edited.paste(shirt, shirt)
    edited.save(sys.argv[2])
