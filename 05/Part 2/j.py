import sys
sys.stdin = open("input.txt")
input = sys.stdin.readlines

lines = input()
# print(lines)
n = len(lines)
for i in range(n):
    lines[i] = lines[i].strip()
# print(lines)
spaceIdx = lines.index('')
# print(spaceIdx)
ranges = lines[:spaceIdx]
elements = lines[spaceIdx + 1:]
# print(ranges, elements)

m = len(ranges)
for i in range(m):
    a, b = map(int, ranges[i].split('-'))
    ranges[i] = (a, b)
ranges.sort()
# print(ranges)

mergedRanges = []
L = ranges[0][0]
R = ranges[0][1]
for i in range(1, m):
    if ranges[i][0] > R:
        mergedRanges.append((L, R))
        L = ranges[i][0]
        R = ranges[i][1]
    else:
        R = max(R, ranges[i][1])
        if i == m - 1:
            mergedRanges.append((L, R))
# print(mergedRanges)
ans = 0
for r in mergedRanges:
    ans += r[1] - r[0] + 1
print(ans)
