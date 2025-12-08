with open("07/Part 1/in.txt", "r") as f:
    grid = []
    for line in f.readlines():
        grid.append(line.strip())

    n = len(grid)  # Height
    m = len(grid[0])  # Width
    start = grid[0].index('S')

    rtn = 0
    beams = {}  # X positions / ways to get there
    beams[start] = 1

    # Going down the grid, beams are x positions updated for each height
    for h in range(1, n):
        for i in range(m):
            if grid[h][i] == '^' and i in beams:
                if i > 0:
                    # Splitting left
                    if i - 1 in beams:
                        beams[i - 1] += beams[i]
                    else:
                        beams[i - 1] = beams[i]
                
                if i < m - 1:
                    # Splitting right
                    if i + 1 in beams:
                        beams[i + 1] += beams[i]
                    else:
                        beams[i + 1] = beams[i]
                
                beams.pop(i)

    for val in beams.values():
        rtn += val
        
    print(rtn)