from collections import deque

def dfs(node, adj):
    if node == ref["out"]:
        return 1
    
    rtn = 0
    for v in adj[node]:
        rtn += dfs(v, adj)

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
    
    # BFS keeping up with num paths
    paths = [0] * (n + 1)
    q = deque()
    paths[ref["you"]] = 1
    q.append(ref["you"])

    print(dfs(ref["you"], adj))
