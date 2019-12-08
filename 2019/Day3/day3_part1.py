import math
input = []

with open("input/day3_test_input.txt") as f:
    for line in f:
        l = line.strip()
        input.append(l)

input[0] = input[0].split(',')
input[1] = input[1].split(',')

for i in range(len(input[0])):
    input[0][i] = (input[0][i][0], int(input[0][i][1:]))
for i in range(len(input[1])):
    input[1][i] = (input[1][i][0], int(input[1][i][1:]))



path_one = [[0,0]]
for i in input[0]:
    start = path_one[len(path_one)-1]
    if i[0] == 'R':
        for j in range(1,i[1]+1):
            path_one.append([start[0]+j,start[1]])
            # print(path_one)
    elif i[0] == 'L':
        for j in range(1, i[1] + 1):
            path_one.append([start[0] - j, start[1]])
            # print(path_one)
    elif i[0] == 'U':
        for j in range(1, i[1] + 1):
            path_one.append([start[0], start[1] + j])
            # print(path_one)
    elif i[0] == 'D':
        for j in range(1, i[1] + 1):
            path_one.append([start[0], start[1] - j])
            # print(path_one)



path_two = [[0,0]]
for i in input[1]:
    start = path_two[len(path_two)-1]
    if i[0] == 'R':
        for j in range(1,i[1]+1):
            path_two.append([start[0]+j,start[1]])
    elif i[0] == 'L':
        for j in range(1, i[1] + 1):
            path_two.append([start[0] - j, start[1]])
    elif i[0] == 'U':
        for j in range(1, i[1] + 1):
            path_two.append([start[0], start[1] + j])
    elif i[0] == 'D':
        for j in range(1, i[1] + 1):
            path_two.append([start[0], start[1] - j])
# print(path_two)

path_one.pop(0)
path_two.pop(0)




intersections = [value for value in path_one if value in path_two]
print("after")
# print(intersections)

distances = [abs(x)+abs(y) for x,y in intersections]

print(distances)

print(min(distances))