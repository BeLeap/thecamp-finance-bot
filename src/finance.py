import enum

import requests
import yfinance as yf


class FinanceType(enum.Enum):
    UNKNOWN = 0
    STOCK = 1
    UPBIT = 2


class FinanceData:
    def __init__(self, name: str = "", price: int = 0, currency: str = "", type: FinanceType = FinanceType.UNKNOWN):
        self.name, self.price, self.currency, self.type = name, price, currency, type

    def __str__(self):
        return f'{self.name}: {self.currency} {self.price}'


def getStockData(code: str):
    print(f"INFO: Processing {code}...")
    data = yf.Ticker(code).info

    if 'longName' in data.keys():
        return FinanceData(data['longName'], data['regularMarketPrice'], data['currency'], FinanceType.STOCK)
    else:
        print(f"ERR: Failed to get data: {code}")
        return FinanceData()


def getUpBitData(code: str):
    print(f"INFO: Processing {code}...")
    res = requests.get(f"https://api.upbit.com/v1/ticker?markets=KRW-{code}")
    res = res.json()[0]
    if 'market' in res.keys():
        return FinanceData(code, res['trade_price'], 'KRW', FinanceType.UPBIT)
    else:
        print(f"ERR: Failed to get data: {code}")
        return FinanceData()
