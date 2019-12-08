'''
mine was working, but with lists it was too slow for the large list.
refactored with sets similar to: https://github.com/Dementophobia/advent-of-code-2019/blob/master/2019_03_p1.py
'''
input = []

'''Long processes for parsing ¯\_(ツ)_/¯'''
with open("input/day3_input.txt") as f:
    for line in f:
        l = line.strip()
        input.append(l)

input[0] = input[0].split(',')
input[1] = input[1].split(',')

#split the direction and the distance
for i in range(len(input[0])):
    input[0][i] = (input[0][i][0], int(input[0][i][1:]))
for i in range(len(input[1])):
    input[1][i] = (input[1][i][0], int(input[1][i][1:]))


#Make a list of all points the wire will hit.
def get_path(wire):
    x,y = 0, 0
    positions = set() #Sets enabled us to do things faster!

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

#Quick way to calculate distance to 0,0
def manhattan(pos):
    return abs(pos[0] + abs(pos[1]))

#Pretty much re-use get_path but keep track of number of moves and save that value when at a crossing
def get_distance_to_crossing(wire, crossings):
    distances = {}
    distance = 0
    x, y = 0, 0

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

            distance += 1

            if (x, y) in crossings:
                distances[(x, y)] = distance

    return distances

# print(input[0])
p1 = get_path(input[0])
p2 = get_path(input[1])



# print(p1)
# print(p2)

#This was the key to part 1, quciker way to find intersections instead of list comprehension
crossings = p1.intersection(p2)

p1_distances = get_distance_to_crossing(input[0], crossings)
p2_distances = get_distance_to_crossing(input[1], crossings)

#Min of the distances to a crossing.
closest = min(p1_distances[crossing] + p2_distances[crossing] for crossing in crossings)

print(closest)
#
# solution = min(manhattan(pos) for pos in crossings)
#
# print(solution)