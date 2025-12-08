# All 8 directions
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (1, 0),
    (1, -1),
    (1, 1),
    (0, 1),
    (0, -1)
]

with open("04/Part 1/in.txt", "r") as f:
    grid = []
    for line in f.readlines():
        grid.append([x for x in line.strip()])
    
    n = len(grid)
    m = len(grid[0])

    rtn = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                count = 0
                for d in directions:
                    new_i = d[0] + i
                    new_j = d[1] + j
                    if 0 <= new_i < n and 0 <= new_j < m:
                        if grid[new_i][new_j] == '@':
                            count += 1
                
                if count < 4:
                    rtn += 1
    
    print(rtn)