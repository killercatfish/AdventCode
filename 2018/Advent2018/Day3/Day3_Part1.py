
'''
a list with lists of the integer values of the inputs
[claim ID, left edge, top edge, width, height]
'''
input_list = []

with open("../input/inputday3.txt") as f:#../input/inputday3.txt
    for line in f:
        l = line.strip()
        j = l[1:]
        j = j.replace(' @ ',',')
        j = j.replace(': ', ',')
        j = j.replace('x', ',')
        new_entry = [int(x) for x in j.split(',')]

        input_list.append(new_entry)

locations = {(0,0):1}
max_width = 0
max_height = 0

for i in input_list:
    cur_width = i[1]+i[3]
    cur_height = i[2] + i[4]
    if cur_width > max_width:
        max_width = cur_width
    if cur_height > max_height:
        max_height = cur_height
    print('le + w: ', i[1], ' + ', i[3], ' = ', (i[1]+i[3]))
    print('te + h: ', i[2], ' + ', i[4], ' = ', (i[2] + i[4]))

print(input_list)
print('max height: ', max_height)
print('max width: ', max_width)

fabric_array = [['.' for x in range(max_height)] for y in range(max_width)]

for i in input_list:
    for x in range(i[1],i[1]+i[3]):
        for y in range(i[2], i[2] + i[4]):
            if fabric_array[x][y]  == '.':
                fabric_array[x][y] = i[0]
            else:
                fabric_array[x][y] = 'x'

for i in fabric_array:
    print(i)

square_inches = sum(x.count('x') for x in fabric_array)

found_id = -1

for i in input_list:
    other_count = 0
    for x in range(i[1],i[1]+i[3]):
        for y in range(i[2], i[2] + i[4]):
            if fabric_array[x][y] != i[0]:
                other_count += 1
    if other_count == 0:
        found_id = i[0]

print(square_inches)
print(found_id)