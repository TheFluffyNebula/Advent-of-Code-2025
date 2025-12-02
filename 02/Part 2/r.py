
data = []
with open("in.txt") as file:
    data = file.read().splitlines()

ranges = data[0].split(",")
ranges = [tuple(map(int, r.split("-"))) for r in ranges]

ret = 0
ret2 = 0
for r in ranges:
    left = r[0]
    right = r[1]
    for num in range(left, right + 1):
        # print(num)
        snum = str(num)
        if len(snum) % 2 == 0 and snum[:len(snum)//2] == snum[len(snum)//2:]:
            ret += num
            # print(num)
        
        for size in range(1, len(snum)):
            if len(snum) % size == 0:
                parts = []
                for i in range(len(snum)//size):
                    parts.append(snum[i*size:(i+1)*size])
                
                flag = True
                for i in range(1, len(parts)):
                    if parts[i] != parts[0]:
                        flag = False
                        break
                if flag:
                    ret2 += num
                    # print(num, parts)
                    break

print(ret, ret2)
