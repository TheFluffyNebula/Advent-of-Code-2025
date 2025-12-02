
data = []
with open("in.txt") as file:
    data = file.read().splitlines()

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

ret2 = 0
ret = 0
val = 50
for line in data:
    if line.startswith("L"):
        dir = -1
        dist = int(line[1:])
    elif line.startswith("R"):
        dir = 1
        dist = int(line[1:])
    
    for i in range(dist):
        val += dir
        if val == -1:
            val = 99
        if val == 100:
            val = 0
        if val == 0:
            ret2 += 1
    if val == 0:
        ret += 1

print(ret, ret2)
