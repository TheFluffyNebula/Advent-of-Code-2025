import sys
sys.stdin = open("input.txt")

s = list(input().strip().split(","))
print(s)

def f(x, y):
    ret = 0
    for i in range(1, 10 ** 6):
        z = int(str(i) * 2)
        if z >= x and z <= y:
            ret += z
    return ret

ans = 0
for fragment in s:
    a, b = map(int, fragment.split("-"))
    # print(a, b)    
    ans += f(a, b)
print(ans)
