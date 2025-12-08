with open("03/Part 1/in.txt", "r") as f:
    lines = f.readlines()
    js = []
    for line in lines:
        js.append([int(x) for x in line.strip()])

    n = len(js)

    rtn = 0
    for i in range(n):
        top = 0

        m = len(js[i])
        # 12 numbers now
        prior = 0
        for j in reversed(range(12)):
            ## Greddy Algorithm
            max_val = max(js[i][prior:(m - j)])
            # Grabbing index of max value
            max_index = js[i][prior:(m - j)].index(max_val) + prior
            top += max_val * 10 ** j  # adding digit
            prior = max_index + 1

        rtn += top
    
    print(rtn)
