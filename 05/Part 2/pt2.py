with open("05/Part 1/in.txt", "r") as f:
    intervals = []

    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            if len(line.split("-")) > 1:
                intervals.append([int(x) for x in line.split("-")])

    # Just interval merging
    intervals.sort()

    n = len(intervals)
    new_int = []
    i = 0
    while i < n:
        start = intervals[i][0]
        end = intervals[i][1]
        j = i + 1
        while j < n and intervals[j][0] <= end:
            end = max(intervals[j][1], end)
            j += 1
        
        new_int.append([start, end])
        i = j

    rtn = 0
    for i in new_int:
        rtn += i[1] - i[0] + 1

    print(rtn)
