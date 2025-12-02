import sys
sys.stdin = open("input.txt")

s = list(input().strip().split(","))
print(s)

allNums = set()

def f(x, y):
    for i in range(1, 10 ** 6):
        z = int(str(i) * 2)
        if z >= x and z <= y:
            allNums.add(z)
    
    for digitCount in range(3, 11):
        for i in range(1, 10 ** 5):
            z = int(str(i) * digitCount)
            if z >= x and z <= y:
                allNums.add(z)

for fragment in s:
    a, b = map(int, fragment.split("-"))
    # print(a, b)    
    f(a, b)
print(sum(allNums))
