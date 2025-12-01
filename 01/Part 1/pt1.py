with open("01/day1.in", "r") as f:
    pos = 50
    rtn = 0
    for line in f.readlines():
        line = line.strip()
        c = line[0]
        num = int(line[1:])

        if c == 'L':
            pos -= num
        else:
            pos += num

        if pos % 100 == 0:
            rtn += 1

    print(rtn)
    
