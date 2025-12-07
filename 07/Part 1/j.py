import sys
sys.stdin = open("input.txt")

lines = [list(x.strip()) for x in sys.stdin.readlines()]
# print(*lines, sep='\n')
from collections import deque

n = len(lines)
m = len(lines[0])
sLoc = lines[0].index("S")
# print(sLoc)

startRow = 0
startCol = sLoc

beams = [sLoc]
ans = 0
for i in range(2, n):
    newBeam = set()
    for j in range(m):
        if j in beams:
            if lines[i][j] == "^":
                ans += 1
                newBeam.add(j - 1)
                newBeam.add(j + 1)
            else:
                newBeam.add(j)
    beams = newBeam
print(ans)
