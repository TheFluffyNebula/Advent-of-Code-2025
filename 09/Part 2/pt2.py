with open("09/Part 2/in.txt", "r") as f:
    pts = []
    for line in f.readlines():
        pts.append(tuple([int(x) for x in line.strip().split(',')]))

    n = len(pts)

    # r, d, l, u
    seg = [[] for _ in range(4)]

    for i in range(n):
        j = (i + 1) % n
        if pts[i][0] != pts[j][0]:
            if pts[i][0] < pts[j][0]:
                # Right
                seg[0].append([pts[i][0], pts[j][0], pts[i][1]])
            else:
                # Left
                seg[2].append([pts[j][0], pts[i][0], pts[i][1]])
        else:
            if pts[i][1] < pts[j][1]:
                # Down
                seg[1].append([pts[i][1], pts[j][1], pts[i][0]])
            else:
                # Up
                seg[3].append([pts[j][1], pts[i][1], pts[i][0]])
    
    # Naive (n^2) solution

    rtn = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check rectangle based on segments
            count = 0
            
            # Defining rectangle segments
            top = [min(pts[i][0], pts[j][0]), max(pts[i][0], pts[j][0]), min(pts[i][1], pts[j][1])]
            for s in seg[0]:
                # If overlapping
                if (not (top[1] <= s[0] or s[1] <= top[0])) and s[2] > top[2]:
                    # print("Top:", pts[i], pts[j])
                    count += 1
                    break
                    
            right = [min(pts[i][1], pts[j][1]), max(pts[i][1], pts[j][1]), max(pts[i][0], pts[j][0])]
            for s in seg[1]:
                # If overlapping
                if (not (right[1] <= s[0] or s[1] <= right[0])) and s[2] < right[2]:
                    # print("Right:", pts[i], pts[j])
                    count += 1
                    break
            
            bottom = [min(pts[i][0], pts[j][0]), max(pts[i][0], pts[j][0]), max(pts[i][1], pts[j][1])]
            for s in seg[2]:
                # If overlapping
                if (not (bottom[1] <= s[0] or s[1] <= bottom[0])) and s[2] < bottom[2]:
                    # print("Bottom:", pts[i], pts[j])
                    count += 1
                    break

            left = [min(pts[i][1], pts[j][1]), max(pts[i][1], pts[j][1]), min(pts[i][0], pts[j][0])]
            for s in seg[3]:
                # If overlapping
                if (not (left[1] <= s[0] or s[1] <= left[0])) and s[2] > left[2]:
                    # print("Left:", pts[i], pts[j])
                    count += 1
                    break
            
            if count < 2:
                # print(pts[i], pts[j])
                rtn = max(rtn, (abs(pts[i][0] - pts[j][0]) + 1) * (abs(pts[i][1] - pts[j][1]) + 1))

    print(rtn)