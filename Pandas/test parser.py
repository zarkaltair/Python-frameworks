# import pandas as pd


# tables = pd.read_html("https://ethgasstation.info/")
# print(tables[0])



# import pandas as pd


# pd.options.display.max_rows = 200
# pd.options.display.max_columns = 20
# pd.options.display.expand_frame_repr = False


# calls_df = pd.read_html("https://www.fnb.co.za/Controller?nav=rates.forex.list.ForexRatesList",) # header={'User-Agent': 'Mozilla/5.0'})
# print(calls_df)


import requests
import pandas as pd

from bs4 import BeautifulSoup


pd.options.display.max_rows = 200
pd.options.display.max_columns = 20
pd.options.display.expand_frame_repr = False


response = requests.get("https://free-proxy-list.net/")
html = response.text
soup = BeautifulSoup(html, 'lxml')
# print(soup)
table = soup.find('table', class_='table')
# print(table)
tr = table.find('tr', class_='odd')
print(tr)

# calls_df = pd.read_html(table)
# print(calls_df)



# import pandas as pd


# def get_forex_buy_quote(currency_code: str = 'EUR', source: str = 'FNB', order_type: str = 'buy'):
#     """Get latest forex from FNB website
#     """
#     if source == 'FNB':
#         tables = pd.read_html(
#             'https://www.fnb.co.za/Controller?nav=rates.forex.list.ForexRatesList',
#             index_col=1, header=0, match=currency_code)

#         df = tables[0]

#         types = {
#             'buy': 'Bank Selling Rate',
#             'sell': 'Bank Buying Rate',
#         }

#         exhange_rate = df.loc[currency_code, types[order_type]]
#         print(exhange_rate)
#         # print(Decimal("%.4f" % float(exhange_rate)))

# get_forex_buy_quote()