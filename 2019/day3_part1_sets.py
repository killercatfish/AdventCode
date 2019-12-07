'''
mine was working, but with lists it was too slow for the large list.
refactored with sets similar to: https://github.com/Dementophobia/advent-of-code-2019/blob/master/2019_03_p1.py
'''
input = []

with open("input/day3_input.txt") as f:
    for line in f:
        l = line.strip()
        input.append(l)

input[0] = input[0].split(',')
input[1] = input[1].split(',')

for i in range(len(input[0])):
    input[0][i] = (input[0][i][0], int(input[0][i][1:]))
for i in range(len(input[1])):
    input[1][i] = (input[1][i][0], int(input[1][i][1:]))

def get_path(wire):
    x,y = 0, 0
    positions = set()

    for i in range(len(wire)):
        for _ in range(int(wire[i][1])):
            dir = wire[i][0]
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y -= 1
            elif dir == 'D':
                y += 1
            positions.add((x,y))
    return positions

def manhattan(pos):
    return abs(pos[0] + abs(pos[1]))


# print(input[0])
p1 = get_path(input[0])
p2 = get_path(input[1])

print(p1)
print(p2)

crossings = p1.intersection(p2)

solution = min(manhattan(pos) for pos in crossings)

print(solution)