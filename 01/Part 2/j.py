with open("input.txt") as fin:
    lines = fin.readlines()
    cur = 50
    ans = 0

    def f(x, y):
        c = 0
        if x < y:
            for i in range(x + 1, y):
                if i % 100 == 0:
                    c += 1
        else:
            for i in range(y + 1, x):
                if i % 100 == 0:
                    c += 1
        return c


    for line in lines:
        line = line.strip()
        direction = line[0]
        num = int(line[1:])
        # print(direction, num)
        if direction == "L":
            newCur = cur - num
        else:
            newCur = cur + num
        # ended up at zero
        if newCur % 100 == 0:
            ans += 1
        ans += f(cur, newCur)
        cur = newCur
    print(ans)
