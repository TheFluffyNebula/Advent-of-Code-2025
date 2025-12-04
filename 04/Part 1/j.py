import sys
sys.stdin = open("input.txt")
input = sys.stdin.readlines

board = input()
n = len(board)
for i in range(n):
    board[i] = board[i].strip()
# print(board)

DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

ans = 0
for i in range(n):
    for j in range(len(board[0])):
        cur = 0
        for dx, dy in DIRECTIONS:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= len(board[0]):
                continue
            # print(nx, ny)
            if board[nx][ny] == "@":
                cur += 1
        if cur < 4 and board[i][j] == "@":
            ans += 1

print(ans)
