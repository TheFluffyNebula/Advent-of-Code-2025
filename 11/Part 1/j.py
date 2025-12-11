lines = open("input.txt").readlines()
lines = [list(lines[i].strip().split()) for i in range(len(lines))]
n = len(lines)
# print(lines)

from collections import defaultdict
adj = defaultdict(list)
for i in range(n):
    line = lines[i]
    m = len(line)
    u = line[0][:-1]
    for j in range(1, m):
        adj[u].append(line[j])
# print(adj)

ans = 0
stack = [("you", "")]
while stack:
    u, prev = stack.pop()
    for v in adj[u]:
        if v != prev:
            stack.append((v, u))
            if v == "out":
                ans += 1
print(ans)
