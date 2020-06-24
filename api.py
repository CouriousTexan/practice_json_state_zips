import json
from urllib.request import urlopen

# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo
with urlopen("https://api.exchangeratesapi.io/latest?base=USD") as response:
    source = response.read()

data = json.loads(source)

with open('exchage_rates.json', 'w') as f:
    json.dump(data, f, indent=2)

