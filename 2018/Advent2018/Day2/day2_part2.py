'''
Advent of code 2018

'''

import numpy as np

list_of_ascii = []
list_of_original = []

def parse_entry(cur):
    letter_count = []
    for i in cur:
        letter_count.append(ord(i))

    return letter_count

with open("../input/inputday2.txt") as f:
    for line in f:
        l = line.strip()
        list_of_original.append(l)
        cur = parse_entry(l)
        list_of_ascii.append(cur)

# for i in range(len(list_of_ascii)):
#     print(list_of_original[i])
#     print(list_of_ascii[i])



#print([j-i for i, j in zip(list_of_ascii[0], list_of_ascii[1])])
def check_difference(a, b):
    c = [j - i for i, j in zip(a, b)]
    #print(c)
    return check_contents(c)

def check_contents(c):
    num_not_0 = 0
    for i in c:
        if i != 0:
            num_not_0 += 1

    if num_not_0 == 1:
        print(c)
        print(np.argmax(c))
        return np.argmax(c)
    return -1

def back_to_char(a):
    str = ""
    for i in a:
        str += chr(i)
    print(str)

for i in range(len(list_of_ascii)-1):
    for j in range(i+1,len(list_of_ascii)):
        index = check_difference(list_of_ascii[i], list_of_ascii[j])
        if index >= 0:
            print(list_of_ascii[i], "\n",list_of_ascii[j])
            winner = list_of_ascii[i]
            del winner[index]
            print(winner)
            back_to_char(winner)




