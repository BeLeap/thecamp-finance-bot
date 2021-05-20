def parseCode(filename: str):
    file = open(f'./resources/{filename}')
    data = file.read()
    return list(map(lambda elem: f"{elem.strip()}", data.split("\n")))
