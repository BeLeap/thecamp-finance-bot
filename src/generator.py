import finance
import parse


def stockFinanceDataGenerator():
    codes = []
    codes += parse.parseCode("KOSPI.txt")
    codes += parse.parseCode("NASDAQ.txt")

    for code in codes:
        yield str(finance.getStockData(code))


def upBitFinanceDataGenerator():
    codes = []
    codes += parse.parseCode("UPBIT.txt")

    for code in codes:
        yield str(finance.getUpBitData(code))
