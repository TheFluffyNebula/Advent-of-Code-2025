def dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2


def dfs(node, adj, explored, temp):
    temp.add(node)
    explored.add(node)
    for v in adj[node]:
        if v not in explored:
            temp = dfs(v, adj, explored, temp)
    
    return temp


with open("08/Part 2/in.txt", "r") as f:
    # Create graph
    # Size of three largest connected components
    NUM_EDGES = 1000  # 10 for sample, 1000 for real

    pts = [[float(x) for x in line.strip().split(',')] for line in f.readlines()]

    n = len(pts)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append([dist(pts[i], pts[j]), i, j])
    
    edges.sort()
    edges = edges[:NUM_EDGES]

    # Construct adjacency
    adj = [[] for _ in range(n)]

    for e in edges:
        adj[e[2]].append(e[1])
        adj[e[1]].append(e[2])
    
    # Compute connected components
    explored = set()
    ccs = []
    for i in range(n):
        if i not in explored:
            ccs.append(dfs(i, adj, explored, set()))
    
    ccs.sort(key=lambda x: len(x), reverse=True)
    
    rtn = 1
    for i in range(3):
        rtn *= len(ccs[i])
    
    print(rtn)

