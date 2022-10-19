from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
fiat = 'USD'

API_KEY = '' # Set your api key

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

params = {
  'start':'1',
  'limit':'5000',
  'convert':fiat
}

session = Session()
session.headers.update(headers)

try:
  r = session.get(url, params=params)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

print(r.json())

import pandas as pd

df = pd.DataFrame(r.json()['data'])
df.head()

f_name = 'cmc_coinlist.csv'
df.to_csv(f_name)

for target_key in df.quote.iloc[0][fiat]:
    df[fiat+'_'+target_key] = df.quote.map(lambda d: d[fiat][target_key])