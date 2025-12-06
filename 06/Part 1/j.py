import sys
sys.stdin = open("input.txt")
input = sys.stdin.readlines

lines = input()
# print(lines)
n = len(lines)
for i in range(n):
    lines[i] = lines[i].strip().split()
# print(lines)
m = len(lines[0])

ans = 0
for i in range(m):
    if lines[-1][i] == "*":
        add = False
    else:
        add = True
    if add:
        cur = 0
    else:
        cur = 1
    for j in range(n - 1):
        if add:
            cur += int(lines[j][i])
        else:
            cur *= int(lines[j][i])
    # print(cur)
    ans += cur
print(ans)
