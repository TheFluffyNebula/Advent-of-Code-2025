with open("01/day1.in", "r") as f:
    pos = 50
    rtn = 0
    for line in f.readlines():
        line = line.strip()
        c = line[0]
        num = int(line[1:])

        temp = pos

        rtn += num // 100
        num %= 100

        if c == 'L':
            temp -= num
        else:
            temp += num

        if pos != 0 and temp < 0 or temp > 100:
            rtn += 1

        pos = (temp + 100) % 100

        if pos == 0:
            rtn += 1

    print(rtn)


