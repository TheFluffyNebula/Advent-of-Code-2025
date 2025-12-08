with open("06/Part 1/in.txt", "r") as f:
    nums = []
    ops = []
    
    for line in f.readlines():
        tokens = line.strip().split()
        if tokens[0].isdigit():
            nums.append([int(x) for x in tokens])
        else:
            ops = tokens
    
    rtn = 0
    n = len(ops)
    for i in range(n):
        if ops[i] == '+':
            val = 0
            for j in range(len(nums)):
                val += nums[j][i]
        else:
            val = 1
            for j in range(len(nums)):
                val *= nums[j][i]
        rtn += val

    print(rtn)