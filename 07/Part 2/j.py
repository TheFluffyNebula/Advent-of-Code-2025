import sys
sys.stdin = open("input.txt")

lines = [list(x.strip()) for x in sys.stdin.readlines()]
# print(*lines, sep='\n')
from functools import cache

n = len(lines)
m = len(lines[0])
sLoc = lines[0].index("S")
# print(sLoc)

@cache
def search(i, j):
    if i == n - 1:
        return 1
    ret = 0
    if lines[i + 1][j] == ".":
        ret += search(i + 1, j)
    else:
        if j > 0:
            ret += search(i + 1, j - 1)
        if j < m:
            ret += search(i + 1, j + 1)
    return ret

ans = search(0, sLoc)
print(ans)
