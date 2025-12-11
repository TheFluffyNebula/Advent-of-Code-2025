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

    best = float('inf')
    memo = {}
    # backtracking attempt
    def backtrack(state, c):
        nonlocal best
        # if state violates constraints: return
        for i in range(goalL):
            if state[i] > goal[i]:
                return
        # if state can't beat current best: prune (return)
        if c >= best:
            return
        # if complete solution: update best, return
        if state == goal:
            best = c
            return
        # memo check
        stateHash = tuple(state)
        if stateHash in memo and memo[stateHash] <= c:
            return
        memo[stateHash] = c        
        # for each valid choice c: apply c, backtrack(new_state), undo c
        for i in range(len(toggles)):
            for idx in toggles[i]:                
                state[idx] += 1
            backtrack(state, c + 1)
            for idx in toggles[i]:
                state[idx] -= 1

    backtrack([0] * goalL, 0)
    return best
        
ans = 0
for i in range(n):
    ans += solve(lines[i])
print(ans)

'''
backtracking might work... or not
'''
