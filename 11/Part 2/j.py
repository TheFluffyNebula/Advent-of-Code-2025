lines = open("input.txt").readlines()
lines = [list(lines[i].strip().split()) for i in range(len(lines))]
n = len(lines)
# print(lines)

from collections import defaultdict, deque
adj = defaultdict(list)
incoming = defaultdict(lambda: 1)
for i in range(n):
    line = lines[i]
    m = len(line)
    u = line[0][:-1]
    for j in range(1, m):
        adj[u].append(line[j])
        # incoming from u
        incoming[line[j]] += 1
# print(adj)

# nothing, dac, fft, dac & fft
visits = defaultdict(lambda: [0, 0, 0, 0])
q = deque([("svr")])
visits["svr"] = [1, 0, 0, 0]
while q:
    u = q.popleft()
    for v in adj[u]:
        incoming[v] -= 1
        # aggregate
        if v == "dac":
            # 0 -> 1, 1 -> 1, 2 -> 3, 3 -> 3
            visits[v][1] += visits[u][0]
            visits[v][1] += visits[u][1]
            visits[v][3] += visits[u][2]
            visits[v][3] += visits[u][3]
        elif v == "fft":
            # 0 -> 2, 1 -> 3, 2 -> 2, 3 -> 3
            visits[v][2] += visits[u][0]
            visits[v][3] += visits[u][1]
            visits[v][2] += visits[u][2]
            visits[v][3] += visits[u][3]
        else:
            # no status change (even for out)
            for i in range(4):
                visits[v][i] += visits[u][i]

        # everything is aggregated here, add it to the queue
        if incoming[v] == 1:
            q.append(v)

ans = visits["out"][3]
print(ans)

'''
once all things have caught up then proceed (aggregate)
'''
