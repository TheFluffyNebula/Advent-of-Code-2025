import sys
sys.stdin = open("input.txt")
input = sys.stdin.readlines

lines = input()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
# print(lines)

ans = 0
for line in lines:
    n = len(line)
    mx = 0
    for i in range(n):
        for j in range(i + 1, n):
            mx = max(mx, int(line[i] + line[j]))
    ans += mx
print(ans)
