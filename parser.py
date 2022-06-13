def parse_file(path):
    file = open(path, "r", encoding='UTF-8')
    lines = file.readlines()
    file.close()
    return list(map(lambda line: line.strip(), lines))
