def colorList():
    list = []
    f = open('colors.txt', 'r')
    file = f.read()
    for line in file.split('\n'):
        for color in line.split(','):
            if len(color) > 3:
                list.append(color)
    f.close()
    return list