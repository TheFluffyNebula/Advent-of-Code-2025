from collections import deque

# Trying memoization
memo = {}
memo_fft = {}
memo_dac = {}
memo_both = {}

# FSAs for DFS to control state
def dfs(node, adj):
    if node == ref["out"]:
        return 0
    
    rtn = 0
    for v in adj[node]:
        if v not in memo:
            if ref["fft"] == v:
                memo[v] = dfs_fft(v, adj)
            elif ref["dac"] == v:
                memo[v] = dfs_dac(v, adj)
            else:
                memo[v] = dfs(v, adj)
        rtn += memo[v]

    return rtn


def dfs_fft(node, adj):
    if node == ref["out"]:
        return 0
    
    rtn = 0
    for v in adj[node]:
        if v not in memo_fft:
            if ref["dac"] == v:
                memo_fft[v] = dfs_both(v, adj)
            else:
                memo_fft[v] = dfs_fft(v, adj)
        rtn += memo_fft[v]

    return rtn


def dfs_dac(node, adj):
    if node == ref["out"]:
        return 0
    
    rtn = 0
    for v in adj[node]:
        if v not in memo_dac:
            if ref["fft"] == v:
                memo_dac[v] = dfs_both(v, adj)
            else:
                memo_dac[v] = dfs_dac(v, adj)
        rtn += memo_dac[v]

    return rtn


def dfs_both(node, adj):
    if node == ref["out"]:
        return 1
    
    rtn = 0
    for v in adj[node]:
        if v not in memo_both:
            memo_both[v] = dfs_both(v, adj)
        rtn += memo_both[v]

    return rtn


with open("11/Part 1/in.txt", "r") as f:

    vertices = []
    edges = []
    for line in f.readlines():
        tokens = line.split(':')
        vertices.append(tokens[0])
        edges.append([x.strip() for x in tokens[1].split()])

    # Encoding everything into numbers
    ref = {}
    count = 0
    n = len(vertices)
    for i in range(n):
        ref[vertices[i]] = i
    ref["out"] = n

    # Constructing adjacency list with numbers
    adj = [[] for _ in range(n + 1)]
    for i in range(n):
        adj[ref[vertices[i]]] = [ref[x] for x in edges[i]]

    print(dfs(ref["svr"], adj))
