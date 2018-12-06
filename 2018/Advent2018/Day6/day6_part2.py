import operator
from collections import Counter
input_list = []
with open("test.txt") as f:#Test File
max_distance = 32
# max_distance = 10000
# with open("../input/inputday6.txt") as f:#Input File
    for line in f:
        l = line.strip().split(", ")
        # l[0],l[1] = int(l[0]), int(l[1])
        # using tupples since they should be immutable
        pt = (int(l[0]), int(l[1]))

        input_list.append(pt)
#
# print(input_list)
# print(len(input_list))

# find the largest x and y
max_x = max(input_list, key=lambda x: x[0])[0]
max_y = max(input_list, key=lambda x: x[1])[1]
# print(max_x, max_y)

locations_grid = [[]]
letter_representations = [chr(i) for i in range(65,91)]
letter_representations = letter_representations + [chr(i)+chr(i) for i in range(65,89)]
# print(letter_representations)

out = ''

# Make a list of letters mapped to coordinates
letter_point = {input_list[i]:letter_representations[i] for i in range(len(input_list))}# (x,y):Letter
# print(letter_point)

#Place letters where they go, ! place holder
for y in range(max_y+2):
    locations_grid.append([])
    for x in range(max_x+2):
        if((x,y) in letter_point.keys()):
            out+=letter_point[(x,y)]
            locations_grid[y].append(letter_point[(x,y)])
        else:
            out += '!'
            locations_grid[y].append('!')
    out += '\n'
locations_grid.pop(-1)

# for i in locations_grid:
#     print(i)

'''
will need to eliminate infinite
maybe by checking for any and all touching an edge
add to exempt list
'''

#could i place a dict of each locations distance to all the locations in each location grid?
#then find min and place key there?
#if multiple occurances of min, place a .
#if letter on edge, remove from possible winner
#find the most occurances of the little letter.

def manhattan_distance(pt1, pt2):
    #|a-c|+|b-d|
    # print(pt1[0])
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
#
# print(input_list[0],input_list[1])
# print(manhattan_distance(input_list[0],input_list[1]))


# finding occurances of min distance
def check_min_num_occurances(val,dist):
    counter = 0
    # print("searching for:",val)
    for i in dist:
        # print(dist[i])
        if dist[i] == val:
            # print(dist[i])
            counter+=1
            if counter > 1:
                return True
    return False

# calculate distances to each location from each cell
for i in range(len(locations_grid)):
    for j in range(len(locations_grid[i])):
        # print(i,j)
        if locations_grid[i][j] == '!':
            # print(i,j,locations_grid[i][j])
            distances = {}
            for z in letter_point:
                distances[z] = manhattan_distance((j,i), z)
            min_dist = min(distances.items(), key = operator.itemgetter(1))
            # print(min_dist)
            locations_grid[i][j] = distances
            if check_min_num_occurances(min_dist[1],distances):
                locations_grid[i][j] = '.'
            else:
                locations_grid[i][j] = letter_point[min_dist[0]]#.lower()
        