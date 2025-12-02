def solve2():
    with open("Part 1/in.txt", "r") as f:
        tokens = []
        for line in f.readlines():
            tokens.extend(line.strip().split(","))

        intervals = []
        for token in tokens:
            val = [int(x) for x in token.split("-") if len(x) > 0]
            if len(val) > 0:
                intervals.append(val)

        a = set()
        for i in intervals:
            for j in range(i[0], i[1] + 1):
                for k in range(1, len(str(j))):
                    if int(str(j)[0:k] * (len(str(j)) // k)) == j:
                        a.add(j)
            
        print(f'Final Answer: {sum(a)}')
    

if __name__ == '__main__':
    solve2()