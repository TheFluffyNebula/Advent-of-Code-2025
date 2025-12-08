lines = open("input.txt").readlines()
lines = [tuple(map(int, lines[i].strip().split(","))) for i in range(len(lines))]
# print(lines)

class DisjointSets:
    def __init__(self, size: int) -> None:
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]

    def find(self, x: int) -> int:
        """:return: the "representative" node in x's component"""
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x: int, y: int) -> bool:
        """:return: whether the merge changed connectivity"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False

        if self.sizes[x_root] < self.sizes[y_root]:
            x_root, y_root = y_root, x_root

        self.parents[y_root] = x_root
        self.sizes[x_root] += self.sizes[y_root]
        return True

    def connected(self, x: int, y: int) -> bool:
        """:return: whether x and y are in the same connected component"""
        return self.find(x) == self.find(y)

n = len(lines)
dsj_set = DisjointSets(n)

edges = []
for i in range(n):
    for j in range(i + 1, n):
        w = ((lines[i][0] - lines[j][0]) ** 2 + (lines[i][1] - lines[j][1]) ** 2 + (lines[i][2] - lines[j][2]) ** 2)
        e = (i, j, w)
        edges.append(e)
edges.sort(key = lambda x: x[2])

ans = -1
for (i, e) in enumerate(edges):
    if dsj_set.find(e[0]) != dsj_set.find(e[1]):
        ans = lines[e[0]][0] * lines[e[1]][0]
        dsj_set.unite(e[0], e[1])
print(ans)     
