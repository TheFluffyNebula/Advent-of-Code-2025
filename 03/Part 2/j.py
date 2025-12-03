import sys
sys.stdin = open("input.txt")
input = sys.stdin.readlines

lines = input()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
# print(lines)

ans = 0
for line in lines:
    n = len(line)

    skip = 0
    stack = [line[0]]
    for i in range(1, n):
        while stack and line[i] > stack[-1]:
            if skip < n - 12:
                stack.pop()
                skip += 1
            else:
                break
        stack.append(line[i])
    stack = stack[:12]
    # print(stack)
    ans += int("".join(stack))
print(ans)
