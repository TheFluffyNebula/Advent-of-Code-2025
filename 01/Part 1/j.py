with open("input.txt") as fin:
    lines = fin.readlines()
    cur = 50
    ans = 0
    for line in lines:
        line = line.strip()
        direction = line[0]
        num = int(line[1:])
        # print(direction, num)
        if direction == "L":
            cur -= num
        else:
            cur += num
        cur %= 100
        if cur == 0:
            ans += 1
    print(ans)
