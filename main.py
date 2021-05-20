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


def resultGenerator():
    codes = []
    codes += parseCode("KOSPI.txt")
    codes += parseCode("NASDAQ.txt")

    for code in codes:
        yield processFinanceData(code)


result = ""
index = 0

for res in resultGenerator():
    result += f" / {res}"
    if (len(result) > 1000):
        content = result[0:1000]
        result = result[1000:len(result)]
        print(f"Sending message {index}")
        sendMessage(content)
        index += 1

if not result:
    print(f"Sending message {index}")
    sendMessage(result)
