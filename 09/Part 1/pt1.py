with open("09/Part 2/in.txt", "r") as f:
    pts = []
    for line in f.readlines():
        pts.append(tuple([int(x) for x in line.strip().split(',')]))

    n = len(pts)

    # Naive (n^2) solution
    rtn = 0
    for i in range(n):
        for j in range(i + 1, n):
            rtn = max(rtn, (abs(pts[i][0] - pts[j][0]) + 1) * (abs(pts[i][1] - pts[j][1]) + 1))
    
    print(rtn)