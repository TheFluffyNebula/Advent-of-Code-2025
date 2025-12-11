# pf max on leftptr, pf min on rightptr
# run on fragmented input
lines = open("input.txt").readlines()
lines = [tuple(map(int, lines[i].strip().split(","))) for i in range(len(lines))]

#######################
# RUN THIS IF INPUT 1 #
#######################
lines = lines[::-1]

n = len(lines)
# print(lines)

pf_max = [0] * (100000)
pf_min = [100000] * (100000)

# set the max going forward
for i in range(n):
    pf_max[lines[i][1]] = max(pf_max[lines[i][1]], lines[i][0])

# set the min going backward
for i in range(n - 1, -1, -1):
    pf_min[lines[i][1]] = min(pf_min[lines[i][1]], lines[i][0])

# accumulate
cur = 0
for i in range(100000):
    cur = max(cur, pf_max[i])
    pf_max[i] = max(pf_max[i], cur)
cur = 100000
for i in range(100000 - 1, -1, -1):
    cur = min(cur, pf_min[i])
    pf_min[i] = max(pf_min[i], cur)

# final calculation
ans = 0
# for elevation in range(100000):
#     if 

print(ans)
