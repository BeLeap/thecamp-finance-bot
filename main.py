import datetime
import os

import thecampy
import yfinance as yf
from dotenv import load_dotenv

load_dotenv(verbose=True)


class FinanceData:
    def __init__(self, name, price, currency):
        self.name = name
        self.price = price
        self.currency = currency

    def toSummary(self):
        return f'{self.name}: {self.currency} {self.price}'


def getFinanceData(code: str):
    print(f"INFO: Processing {code}...")
    data = yf.Ticker(code).info

    if 'longName' in data.keys():
        return FinanceData(data['longName'], data['regularMarketPrice'], data['currency'])
    else:
        print(f"ERR: Failed to get data: {code}")
        return FinanceData("", 0, "")


def parseCode(filename: str):
    file = open(f'./resources/{filename}')
    data = file.read()
    return list(map(lambda elem: f"{elem.strip()}", data.split("\n")))


soldier = thecampy.Soldier(
    "김종연",
    "20010212",
    "20210426",
    "육군훈련소",
)

tc = thecampy.client()
tc.login(os.getenv('ID'), os.getenv('PASSWORD'))
tc.get_soldier(soldier)


def sendMessage(content: str):
    msg = thecampy.Message(
        f'{datetime.datetime.now().isoformat()} 주가정보', content)
    tc.send_message(soldier, msg)


def processFinanceData(code: str):
    return getFinanceData(code).toSummary()


resultArray = []
resultArray += list(map(processFinanceData,
                        parseCode("KOSPI.txt")))
resultArray += list(map(processFinanceData,
                        parseCode("NASDAQ.txt")))

result = " / ".join(resultArray)

chunks, chunk_size = len(result), 1000
map(sendMessage, [result[i:i+chunk_size] for i in range(0, chunks, chunk_size)])
