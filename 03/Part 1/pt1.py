with open("03/Part 1/in.txt", "r") as f:
    lines = f.readlines()
    js = []
    for line in lines:
        js.append([int(x) for x in line.strip()])

    n = len(js)

    rtn = 0
    for i in range(n):
        top = 0
        for j in range(len(js[i]) - 1):
            top = max(top, 10 * js[i][j] + max(js[i][j+1:]))
    
        rtn += top
    
    print(rtn)
