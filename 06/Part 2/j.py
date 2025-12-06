import sys
sys.stdin = open("input.txt")
input = sys.stdin.readlines

lines = input()
# print(lines)
n = len(lines)
# no strip yet, -1 for \n
m = len(lines[0]) - 1
# print(m)
digitPresent = [False] * m
for i in range(n):
    lines[i] = list(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            digitPresent[j] = True
# print(*lines, sep='\n')
# print(digitPresent)

# strategy: pad w/ zeros & convert to int 😎
for i in range(n - 1):
    for j in range(m):
        if lines[i][j] == ' ':
            if digitPresent[j]:
                lines[i][j] = '0'

for i in range(n):
    lines[i] = lines[i][:-1]
    lines[i] = list("".join(lines[i]).split())
# print(*lines, sep='\n', end="\n\n")

n = len(lines)
m = len(lines[0])

def f(x):
    nums = [lines[i][x] for i in range(n - 1)]
    operator = lines[-1][x]
    # print(nums, sep='\n')
    numLength = len(nums[0])
    if operator == "+":
        ret = 0
    else:
        ret = 1
    for j in range(numLength):
        curNum = ""
        for i in range(len(nums)):
            if nums[i][j] != "0":
                curNum += nums[i][j]
        if operator == "+":
            ret += int(curNum)
        else:
            ret *= int(curNum)
        # print(curNum)
    return ret

ans = 0
# process each column now
for i in range(m):
    # f(i)
    ans += f(i)
print(ans)
