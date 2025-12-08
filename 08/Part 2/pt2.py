def dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2

parent = []

# Basic DSU, no optimizations
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(i, j):
    pi = find(i)
    pj = find(j)

    parent[pi] = pj


with open("08/Part 2/in.txt", "r") as f:
    # Create graph
    # Literally just run kruskal's algorithm

    pts = [[float(x) for x in line.strip().split(',')] for line in f.readlines()]

    n = len(pts)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append([dist(pts[i], pts[j]), i, j])
    
    edges.sort()

    # Creating the DSU
    parent = [i for i in range(n)]

    ans = -1
    for e in edges:
        if find(e[1]) != find(e[2]):
            ans = int(pts[e[1]][0] * pts[e[2]][0])
            union(e[1], e[2])
    
    print(ans)

