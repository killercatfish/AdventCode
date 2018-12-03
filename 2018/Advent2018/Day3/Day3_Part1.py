
'''
a list with lists of the integer values of the inputs
[claim ID, left edge, top edge, width, height]
'''
input_list = []

with open("../input/inputday3.txt") as f:
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

for i in fabric_array:
    print(i)

print(fabric_array[0][0])