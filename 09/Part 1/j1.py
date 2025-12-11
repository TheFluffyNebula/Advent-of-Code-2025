lines = open("input.txt").readlines()
lines = [tuple(map(int, lines[i].strip().split(","))) for i in range(len(lines))]
# print(lines)

n = len(lines)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        c = (abs(lines[i][0] - lines[j][0]) + 1) * (abs(lines[i][1] - lines[j][1]) + 1)
        ans = max(ans, c)
print(ans)
