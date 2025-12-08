with open("06/Part 1/in.txt", "r") as f:
    grid = []
    ops = []
    
    for line in f.readlines():
        tokens = line.strip().split()
        if tokens[0].isdigit():
            grid.append(line)
        else:
            ops = tokens
    
    n = len(grid)
    m = len(grid[0])
    int_grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j].isdigit():
                int_grid[i][j] = int(grid[i][j])

    nums = []
    for i in range(m):
        total = 0
        for j in range(n):
            total += int_grid[j][i] * 10 ** (n - j - 1)

        # Weird debug
        while total > 0 and total % 10 == 0:
            total /= 10
        nums.append(int(total))

    groups = []
    group = []
    for num in nums:
        if num == 0:
            groups.append(group)
            group = []
        else:
            group.append(num)
    groups.append(group)  # Might be empty but adding anyways

    rtn = 0
    for i in range(len(ops)):
        if ops[i] == '+':
            val = 0
            for x in groups[i]:
                val += x
        else:
            val = 1
            for x in groups[i]:
                val *= x
        
        rtn += val

    print(rtn)