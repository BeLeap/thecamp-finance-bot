import finance
import generator
import thecamp


def main():
    result = ""
    index = 0

    for res in generator.stockFinanceDataGenerator():
        result += f" / {res}"
        if (len(result) > 1000):
            content, result = result[0:1000], result[1000:len(result)]
            print(f"Sending message {index}")
            thecamp.sendMessage(content)
            index += 1

    for res in generator.upBitFinanceDataGenerator():
        result += f" / {res}"
        if (len(result) > 1000):
            content, result = result[0:1000], result[1000:len(result)]
            print(f"Sending message {index}")
            thecamp.sendMessage(content)
            index += 1

    if len(result) > 0:
        print(f"Sending message {index}")
        thecamp.sendMessage(result)


if __name__ == "__main__":
    main()
