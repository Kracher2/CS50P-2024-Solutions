import requests
import sys

try:
    n = float(sys.argv[-1])
except ValueError:
    sys.exit("Usage: python bitcoin.py n")

json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
json = dict(json.json())
rate = json["bpi"]["USD"]["rate_float"]

print(f"${(n * rate):,.4f}")
