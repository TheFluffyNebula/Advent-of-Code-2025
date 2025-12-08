with open("05/Part 1/in.txt", "r") as f:
    intervals = []
    nums = []

    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            if len(line.split("-")) > 1:
                intervals.append([int(x) for x in line.split("-")])
            else:
                nums.append(int(line))

    rtn = 0
    for num in nums:
        for i in intervals:
            if i[0] <= num <= i[1]:
                rtn += 1
                break

    print(rtn)