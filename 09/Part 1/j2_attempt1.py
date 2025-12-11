lines = open("input.txt").readlines()
lines = [tuple(map(int, lines[i].strip().split(","))) for i in range(len(lines))]
n = len(lines)
print(lines)

orient = [0] * n
for i in range(n):
    curCol, curRow = lines[i]
    newCol, newRow = lines[(i + 1) % n]
    if curRow == newRow:
        # left or right
        if newCol > curCol:
            # moving right
            orient[i] = 3
        else:
            orient[i] = 1
    else:
        # up or down
        if newRow < curRow:
            # moving down
            orient[i] = 0
        else:
            orient[i] = 2

def segmentInPolygon(seg1, seg2):
    x1, y1 = seg1
    x2, y2 = seg2
    if x1 == x2:
        for i in range(min(y1, y2) + 1, max(y1, y2)):
            if not pointInPolygon((x1, i)):
                # if x1 == 2 and y1 == 3 and x2 == 9 and y2 == 3:
                #     print(x1, i)
                return False
    else:
        assert y1 == y2
        for i in range(min(x1, x2) + 1, max(x1, x2)):
            if not pointInPolygon((i, y1)):
                # if x1 == 2 and y1 == 3 and x2 == 9 and y2 == 3:
                #     print(i, y1)
                return False
    return True

def pointInPolygon(cow):
    hits = 0
    # does a ray from (cx, cy) intersect (f1, f2)?
    cx, cy = cow
    cx += 0.5
    cy += 0.5
    # print(cx, cy)
    for i in range(n):
        p1, p2 = lines[i], lines[(i + 1) % len(lines)]
        f1x, f1y = p1
        f2x, f2y = p2

        # based on where the points are, update the points
        # down, left, up, right
        if orient[i] == 0:
            # left
            pass
        elif orient[i] == 1:
            # top
            f1y += 1
            f2y += 1
        elif orient[i] == 2:
            # use the right edge
            f1x += 1
            f2x += 1
        else:
            # use bot edge
            pass

        if ((f1y > cy) ^ (f2y > cy)):
            hits += (f1y - f2y < 0) ^ (f2x * (f1y - cy) + f1x * (cy - f2y) > cx * (f1y - f2y))
        else:
            continue
    # print("hits:", hits)
    return hits % 2 == 1

# print(pointInPolygon((3, -3)))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = (lines[i][0], lines[i][1])
        b = (lines[j][0], lines[j][1])
        c = (a[0], b[1])
        d = (b[0], a[1])
        # print(b, d, a, segmentInPolygon(b, d), segmentInPolygon(d, a))
        if segmentInPolygon(a, c) and segmentInPolygon(c, b) and segmentInPolygon(b, d) and segmentInPolygon(d, a):
            cur = (abs(lines[i][0] - lines[j][0]) + 1) * (abs(lines[i][1] - lines[j][1]) + 1)
            # print(cur, a, b)
            ans = max(ans, cur)
print(ans)

'''
ray tracing attempt
'''
