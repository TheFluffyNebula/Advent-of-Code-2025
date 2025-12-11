# wow that's fun
import turtle
lines = open("input2.txt").readlines()
lines = [tuple(map(int, lines[i].strip().split(","))) for i in range(len(lines))]
n = len(lines)
# print(lines)

SCALE = 10 ** (-2.5)

turtle.up()
turtle.goto(SCALE * lines[0][0], SCALE *  lines[0][1])
turtle.down()
for i in range(n):
    turtle.goto(SCALE * lines[i][0], SCALE * lines[i][1])
turtle.done()
