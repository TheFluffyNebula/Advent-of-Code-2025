lines = open("input.txt").readlines()
lines = [list(lines[i].strip().split()[:-1]) for i in range(len(lines))]
n = len(lines)
# print(lines)

from functools import cache

def solve(a):
    global ans
    best = float('inf')
    goalS = a[0][1:-1]
    goal = [int(goalS[i] == "#") for i in range(len(goalS))]
    goalL = len(goal)
    # print(goal)
    toggles = []
    for i in range(1, len(a)):
        toggle = list(map(int, a[i][1:-1].split(",")))
        toggles.append(toggle)
    # print(toggles)

    # observation: never makes sense to hit a switch more than once
    numToggles = len(toggles)
    for i in range(2 ** numToggles):
        lights = [0] * goalL
        x = i
        for j in range(numToggles):
            if x % 2 == 1:
                # apply the changes in toggles[j]
                for idx in toggles[j]:
                    lights[idx] = 1 - lights[idx]
            x >>= 1
        if lights == goal:
            best = min(best, i.bit_count())
    # print(best)
    ans += best
        
ans = 0
for i in range(n):
    solve(lines[i])
print(ans)
