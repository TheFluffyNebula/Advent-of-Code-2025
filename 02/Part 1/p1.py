def solve1():
    with open("Part 1/in.txt", "r") as f:
        tokens = []
        for line in f.readlines():
            tokens.extend(line.strip().split(","))

        intervals = []
        for token in tokens:
            val = [x for x in token.split("-") if len(x) > 0]
            if len(val) > 0:
                intervals.append(val)

        rtn = 0
        count = 0
        for i in intervals:
            count += int(i[1]) - int(i[0])
            n = len(i[0])
            if n % 2 == 1:
                start = 10 ** (n // 2)
            else:
                start = int(i[0][:(n // 2)])
            
            while int(str(start) * 2) <= int(i[1]):
                if int(str(start) * 2) >= int(i[0]):
                    rtn += int(str(start) * 2)
                start += 1
            
        print(f"Complexity: {count}")
        print(f'Final Answer: {rtn}')


if __name__ == '__main__':
    solve1()