input_list = []
# with open("test.txt") as f:#Test File
with open("../input/inputday7.txt") as f:#Input File
    for line in f:
        l = line.strip().split(" ")
        print(l)
        j = [l[1],l[7]]
        input_list.append(j)

print(input_list)

# one pair for testing and one for actual
# total_workers = 2
# step_time = {chr(64+i):i for i in range(1,27)}
total_workers = 5
step_time = {chr(64+i):60+i for i in range(1,27)}
# print(step_time)

avail_workers = total_workers



# Dictionary containing the letter key, and a list of what letter needs to come first.
order = {}

for i in input_list:
    if i[0] not in order.keys():
        order[i[0]] = []
    if i[1] not in order.keys():
        order[i[1]] = []

for i in input_list:
    order[i[1]].append(i[0])

for i in order:
    print(i,":",order[i])

# printable = "%-*s%-*s%-*s%-*s" % (12,'Second',12,'Worker 1', 12,'Worker 2', 12,'Done')
printable = "%-*s%-*s%-*s%-*s%-*s%-*s%-*s" % (12,'Second',12,'Worker 1', 12,'Worker 2',12,'Worker 3', 12,'Worker 4',12,'Worker 5',12, 'Done')



# List containing the completed
finished_list = []

# remove a completed project from list
def remove_from_values(val):
    # print("val in remove from values:",val)
    for i in order:
        if val in order[i]:
            order[i].remove(val)
    # print("order after remove:",order)

# # remove completed key from order dict
# def remove_keys(key_list):
#     for i in key_list:
#         order.pop(i)
#         # print(order)

# print("order len: ", len(order))

cur_list = [] #list of current parts
next_list = [] #list of parts that can now we started
clock = -1 #counter for time

def fill_lists():
    global next_list,avail_workers,order,cur_list
    for i in order: #find any parts ready to be built
        if order[i] == []:
            next_list.append(i)

    for i in next_list:#remove anything ready to be made from our list of items
        if i in order:
            order.pop(i)

    next_list = sorted(next_list)

    # print("next_list:",next_list)
    counter = avail_workers
    for i in range(counter):
        if len(next_list) > 0:
            avail_workers-=1
            cur_list.append(next_list.pop(0))

while len(cur_list) > 0 or clock == -1 or len(order) > 0: #keep going until all parts are done
    clock += 1
    # print("\n**CLOCK TICK",clock,"**")

    fill_lists()
    #
    # cur_list = sorted(cur_list)
    # print("cur_list:", cur_list)
    # print("next_list:", next_list)
    # print("order",order)

    temp_list = cur_list
    for i in temp_list:
        # print("i:", i)
        step_time[i] -= 1
        # print(i,"step time:", step_time[i])
        if step_time[i] == 0:
            # print("curval:",i)
            avail_workers+=1
            finished_list.append(i)
            remove_from_values(i)
            cur_list.remove(i)
            # print("finished list:", finished_list)
            # print("order:", order)
            # print("cur_list:",cur_list)
            fill_lists()


    print_worker_status = []
    for t in range(total_workers):
        if t < len(cur_list):
            print_worker_status.append(cur_list[t])
        else:
            print_worker_status.append('.')

    done = ''
    if len(finished_list) > 0:
        done = ''.join(finished_list)
    # printable = printable + '\n' + "%-*s%-*s%-*s%-*s" % (12, clock, 12, print_worker_status[0], 12, print_worker_status[1], 12, done)
    printable = printable + '\n' + "%-*s%-*s%-*s%-*s%-*s%-*s%-*s" % (12, clock, 12, print_worker_status[0], 12, print_worker_status[1],  12, print_worker_status[2], 12, print_worker_status[3], 12, print_worker_status[4],12, done)


print(printable)


#
#     next_list = []
#     for i in order:
#         if order[i] == []:
#             next_list.append(i)
#             # finished_list.append(i)
#             # remove_from_values(i)
#     next_list = sorted(next_list)
#     print("next_list:",next_list)
#     # for j in next_list:
#     cur_val = next_list.pop(0)
#     finished_list.append(cur_val)
#     remove_from_values(cur_val)
#     order.pop(cur_val)
#     # print("order len: ",len(order))
#
print("\n*****done*****")
print(finished_list)
answer = ''.join(finished_list)

print(answer)
print("clock:",clock)