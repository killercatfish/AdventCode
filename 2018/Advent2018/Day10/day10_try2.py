import collections
import re

#with open('day10test.txt') as f:
with open('../input/inputday10.txt') as f:
  lines = [l.rstrip('\n') for l in f] #quickly split and strip the end line character and make list
  lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines] #regex to find all numbers in each line
  # print(lines)

min_list = {} #get a min list

for i in range(20000): #arbitrarily large number
    # i * vx gives ith movement
    # find the min and max for each iteration,
    minx = min(x + i * vx for (x, y, vx, vy) in lines)
    maxx = max(x + i * vx for (x, y, vx, vy) in lines)
    miny = min(y + i * vy for (x, y, vx, vy) in lines)
    maxy = max(y + i * vy for (x, y, vx, vy) in lines)

    #finding the smallest "window" where all the lights are
    val = maxx - minx + maxy - miny
    min_list[i] = val

    # print(i, maxx - minx + maxy - miny)

min_key = min(min_list, key=min_list.get)
min_val = min_list[min_key]

print(min_key,min_val)


map = [[' '] * 200 for j in range(400)]
i = min_key
for (x, y, vx, vy) in lines:
    map[y + i * vy][x + i * vx - 250] = '*'

for m in map:
    print(''.join(m))

#PANLPAPR