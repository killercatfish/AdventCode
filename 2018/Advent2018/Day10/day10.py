'''
This is attempt was going to be to use open cv to detect text.
'''


import re
from PIL import Image
locations = []
velocities = []
# with open("test.txt") as f:#Test File
with open("../input/inputday10.txt") as f:#Input File
    for line in f:
        l = line.strip()
        '''
        Gross code following, need to use regex probably
        '''
        start = l.index("<")#l[  : l.index(">") ]
        end = l.index(">")
        # print(start,end)
        loc = l[start+1:end].replace(' ','').split(',')
        loc[0],loc[1] = int(loc[0]),int(loc[1])
        l = l[end+1:]
        start = l.index("<")  # l[  : l.index(">") ]
        end = l.index(">")
        # print(start, end)
        vel = l[start + 1:end].replace(' ', '').split(',')
        vel[0], vel[1] = int(vel[0]), int(vel[1])
        # print(vel)
        locations.append(loc)
        velocities.append((vel[0],vel[1]))

# for i in range(len(locations)):
#     print(locations[i])
#     print(velocities[i])
def adjust_locations():
    for l in range(len(locations)):
        locations[l][0] += velocities[l][0]
        locations[l][1] += velocities[l][1]

for i in range(5):
    min_x = min(locations,key=lambda x: x[0])[0]
    min_y = min(locations, key=lambda x: x[1])[1]
    max_x = max(locations,key=lambda x: x[0])[0]
    max_y = max(locations, key=lambda x: x[1])[1]

    print('min x',min_x)
    print('max x',max_x)
    print('min y',min_y)
    print('max y',max_y)

    x_adjust = 0
    y_adjust = 0
    if min_x < 0:
        x_adjust = abs(min_x)
    if min_y < 0:
        y_adjust = abs(min_y)

    print('x adjust:',x_adjust)
    print('y adjust:',y_adjust)

    width = max_x + x_adjust+1
    height = max_y + y_adjust+1

    cur_image = Image.new('1',(width, height))

    pixels = cur_image.load()

    print(cur_image.size[0],cur_image.size[1])

    for l in locations:
        # print(l)
        # print('l[0]',l[0])
        # print('l[1]',l[1])
        x = l[0] + x_adjust
        y = l[1] + y_adjust
        print('x',x)
        print('y',y)
        pixels[x,y] = 1

    # for i in range(height):
    #     for j in range(width):
    #         print(pixels[j,i],end='')
    #     print('')

    cur_image.show()
    adjust_locations()