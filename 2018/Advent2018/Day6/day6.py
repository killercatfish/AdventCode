import operator
from collections import Counter
input_list = []
# with open("test.txt") as f:#Test File
with open("../input/inputday6.txt") as f:#Input File
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

letter_point = {input_list[i]:letter_representations[i] for i in range(len(input_list))}# (x,y):Letter
# print(letter_point)

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
            # check_min_num_occurances(min_dist[1],distances)
            # locations_grid[i][j] = letter_point[min_dist[0]].lower()

for i in locations_grid:
    print(i)

infinite_list = []
#top
for i in locations_grid[0]:
    # print(i)
    if i not in infinite_list and i != '.':
        infinite_list.append(i)
#bottom
for i in locations_grid[len(locations_grid)-1]:
    # print(i)
    if i not in infinite_list and i != '.':
        infinite_list.append(i)
#right
for i in locations_grid:
    # print(i)
    if i[len(i)-1] not in infinite_list and i[len(i)-1] != '.':
        infinite_list.append(i[len(i)-1])
#left
for i in locations_grid:
    if i[0] not in infinite_list and i[0] != '.':
        infinite_list.append(i[0])

print(infinite_list)

areas = {}
for i in range(len(locations_grid)):
    for j in range(len(locations_grid[i])):
        # print(i,j)
        cur_val = locations_grid[i][j]
        if cur_val not in infinite_list and cur_val != '.':
            # print(locations_grid[i][j],"is Naughty!")
            # print(cur_val)
            if cur_val not in areas.keys():
                areas[cur_val] = 1
            else:
                areas[cur_val] += 1
# for i in areas:
#     print(areas,":",areas[i])
max_area = max(areas.items(), key = operator.itemgetter(1))
print("max area:",max_area)
