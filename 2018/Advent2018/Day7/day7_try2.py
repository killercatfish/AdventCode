'''
In order to copy an inner list not by reference:
https://stackoverflow.com/questions/8744113/python-list-by-value-not-by-reference
'''
from copy import deepcopy
input_list = []
'''
step_time: list of letter values
printable: heading for printing
second_list: [workers current job, seconds remaining], done list
'''
'''
Test input
'''
# with open("test.txt") as f:#Test File
#     for line in f:
#         l = line.strip().split(" ")
#         print(l)
#         j = [l[1],l[7]]
#         input_list.append(j)
# step_time = {chr(64+i):i for i in range(1,27)}
# printable = "%-*s%-*s%-*s%-*s" % (12,'Second',12,'Worker 1', 12,'Worker 2', 12,'Done')
# second_list = [[[],[],[]]]
'''
Real input
'''
with open("../input/inputday7.txt") as f:#Input File
    for line in f:
        l = line.strip().split(" ")
        print(l)
        j = [l[1],l[7]]
        input_list.append(j)
step_time = {chr(64+i):60+i for i in range(1,27)}
printable = "%-*s%-*s%-*s%-*s%-*s%-*s%-*s" % (12,'Second',12,'Worker 1', 12,'Worker 2',12,'Worker 3', 12,'Worker 4',12,'Worker 5', 12,'Done')
second_list = [[[],[],[],[],[],[]]]

# print(input_list)
# print(step_time)
# print(printable)

# Dictionary containing the letter key, and a list of what letter needs to come first.
order = {}
'''
order dictionary: list of what needs to come before a letter
'''
for i in input_list:
    if i[0] not in order.keys():
        order[i[0]] = []
    if i[1] not in order.keys():
        order[i[1]] = []

for i in input_list:
    order[i[1]].append(i[0])
#
# for i in order:
#     print(i,":",order[i])

final_size = len(order.keys())
# print(len(second_list[len(second_list)-1]))
#len(second_list[len(second_list)-1]) #get length of finished list

'''
find any parts that no longer have to wait
'''
def find_available_parts():
    found = []
    for i in order:
        if order[i] == []:
            found.append(i)
    return sorted(found)

# available = find_available_parts()
# print(available)

# remove a completed project from list
def remove_from_values(val):
    # print("val in remove from values:",val)
    for i in order:
        if val in order[i]:
            # print("removing:",val)
            order[i].remove(val)

#check if there are workers available and a part ready.
def update_second_workers(next):
    ready = find_available_parts()
    for i in range(0, len(next) - 1):
        if next[i] == []:
            # print(second_list[0][i])
            if len(ready) > 0:
                r = ready.pop(0)
                time = step_time[r]
                next[i] = [r, time]
                del order[r]
    return next


#Create next second list entry
def decrease_times(cur):
    #goes through and decreases any current work times by 1 second and returns list.
    #moves to finished list if at 0

    for i in range(len(cur)-1):
        next = cur
        # print("i:",i, "next[i]", next[i])
        if next[i] != []:
            next[i][1]-=1
            if next[i][1] == 0:
                next[len(next)-1].append(next[i][0])
                needs_removal = next[i][0]
                next[i] = []
                # print("i:",i)
                remove_from_values(needs_removal)
    next = update_second_workers(next)
    #add any available parts to any available worker.
    return next

#update another second
def update_second_list():
    current_index = len(second_list)-1
    # print(current_index)
    cur = deepcopy(second_list[current_index])
    second_list.append(decrease_times(cur))
    #method to update available, check if its in the done list too.
    #update what workers are doing

#Initialize seconds list
update_second_workers(second_list[0])
# print(second_list)

#while the done lists length is less than the total letters needing completion
while len(second_list[len(second_list)-1][len(second_list[len(second_list)-1])-1]) <final_size:
    update_second_list()


#print(len(second_list[len(second_list)-1][len(second_list[len(second_list)-1])-1]))

for i in range(len(second_list)):
    print(i,second_list[i])