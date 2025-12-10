"""
Docstring for 10.Part 1.pt1

BFS over possible subspaces of combinations
"""

MAX_VAL = 100000

def lightsToBinary(token):
    token = token.strip('[').strip(']')
    rtn = 0
    for i in range(len(token)):
        if token[i] == '#':
            rtn += 2 ** i
    return rtn


def buttonToBinary(token):
    nums = [int(x) for x in token.strip('(').strip(')').split(',')]
    rtn = 0
    for num in nums:
        rtn += 2 ** num
    return rtn


with open("10/Part 1/in.txt", "r") as f:
    ends = []
    edges = []
    lengths = []

    for line in f.readlines():
        tokens = line.strip().split()
        lights = tokens[0]
        buttons = tokens[1:-1]
        joltage = tokens[-1]

        # Converting lights
        ends.append(lightsToBinary(lights))
        edges.append([buttonToBinary(x) for x in buttons])
        lengths.append(len(lights) - 2)

    rtn = 0
    for i in range(len(ends)):
        # BFS starting at 0 and ending at end
        # Using the edges to xor along the way

        fin = ends[i]
        edg = edges[i]
        dist = [MAX_VAL for _ in range(2 ** lengths[i])]
        dist[0] = 0

        while dist[fin] == MAX_VAL:
            for e in edg:
                for node in range(len(dist)):
                    if dist[node] != MAX_VAL:
                        # If this is a node that's explored
                        new_val = e ^ node
                        dist[new_val] = min(dist[new_val], dist[node] + 1)
                    
        rtn += dist[fin]
    
    print(rtn)