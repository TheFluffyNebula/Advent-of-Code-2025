lines = open("input.txt").readlines()
lines = [list(lines[i].strip().split()[1:]) for i in range(len(lines))]
n = len(lines)
# print(lines)

# from functools import cache

def solve(a):
    global ans
    goalS = a[-1][1:-1].split(",")
    goal = [int(goalS[i]) for i in range(len(goalS))]
    goalL = len(goal)
    # print(goal)
    toggles = []
    for i in range(len(a) - 1):
        toggle = list(map(int, a[i][1:-1].split(",")))
        toggles.append(toggle)
    # print(toggles)
    print(goal, toggles)
        
ans = 0
for i in range(n):
    solve(lines[i])
print(ans)

'''
giving knapsack a go!
'''
