'''
Advent of code 2018 Part 2
1) Read careful.  Describe what it is asking below:




'''

input_list = []
sum_dict = {0:1}

with open("../input/input.txt") as f:
    for line in f:
        l = line.strip()
        if l[0] == '-':
            input_list.append(int(l))
        else:
            input_list.append(int(l[1:]))
        #input_list.append([l[:1],int(l[1:])])


print(input_list)
cur_sum = 0

found_repeat = False

while not found_repeat:
    for i in input_list:
        cur_sum += i
        if cur_sum in sum_dict:
            print("repeat: ",cur_sum)
            found_repeat = True
            break
        else:
            sum_dict[cur_sum] = 1


#print(sum_dict)

