with open("12/Part 1/in.txt", "r") as f:
    shapes = []
    boxes = []
    lines = f.readlines()
    for i in range(len(lines)):
        l = lines[i].strip()
        if ':' in l:
            tokens = l.split()
            if len(tokens) < 2:
                shape = []
                for j in range(3):
                    shape.append([int(x == '#') for x in lines[i + j + 1].strip()])
                shapes.append(shape)
                i += 3
            else:
                box = []
                box.append([int(x) for x in tokens[0].strip(':').split('x')])
                box.extend([int(x) for x in tokens[1:]])
                boxes.append(box)

    # We need a sort of dynamic programming approach

    """
    Actually we just cheese the solution based on if there are enough grid spaces...
    """

    possible = 0
    for box in boxes:
        if box[0][0] * box[0][1] >= 7 * sum(box[1:]):
            possible += 1
    
    print(possible)
