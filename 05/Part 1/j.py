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
# print(ranges)

n = len(elements)
for i in range(n):
    elements[i] = int(elements[i])
# print(elements)

ans = 0
for i in range(n):
    fresh = False
    for j in range(m):
        if elements[i] >= ranges[j][0] and elements[i] <= ranges[j][1]:
            fresh = True
            break
    if fresh:
        ans += 1
print(ans)
