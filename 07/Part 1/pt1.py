from collections import deque

with open("07/Part 1/in.txt", "r") as f:
    grid = []
    for line in f.readlines():
        grid.append(line.strip())

    n = len(grid)  # Height
    m = len(grid[0])  # Width
    start = (0, grid[0].index('S'))

    q = deque()
    q.append(start)
    explored = set()
    explored.add(start)
    rtn = 0

    while q:
        beam = q.popleft()
        
        temp = (beam[0] + 1, beam[1])
        if temp[0] < m:
            if grid[temp[0]][temp[1]] == '.':
                if temp not in explored:
                    q.append(temp)
                    explored.add(temp)
            else:
                split = False
                if 0 < temp[1]:
                    # Splitting left
                    left_temp = (temp[0], temp[1] - 1)
                    if left_temp not in explored:
                        q.append(left_temp)
                        explored.add(left_temp)
                    split = True
                
                if temp[1] < m - 1:
                    # Splitting right
                    right_temp = (temp[0], temp[1] + 1)
                    if right_temp not in explored:
                        q.append(right_temp)
                        explored.add(right_temp)
                    spilt = True

                if split:
                    rtn += 1

        
    print(rtn)