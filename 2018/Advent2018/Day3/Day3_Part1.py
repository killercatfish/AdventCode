
'''
a list with lists of the integer values of the inputs
[claim ID, left edge, right edge, width, height]
'''
input_list = []

with open("text.txt") as f:
    for line in f:
        l = line.strip()
        j = l[1:]
        j = j.replace(' @ ',',')
        j = j.replace(': ', ',')
        j = j.replace('x', ',')
        new_entry = [int(x) for x in j.split(',')]

        input_list.append(new_entry)


locations = {}

for i in input_list:
    

print(input_list)