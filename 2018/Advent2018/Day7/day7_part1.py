input_list = []
# with open("test.txt") as f:#Test File
with open("../input/inputday7.txt") as f:#Input File
    for line in f:

        l = line.strip().split(" ")
        print(l)
        j = [l[1],l[7]]
        input_list.append(j)
print(input_list)
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

finished_list = []

def remove_from_values(val):
    # print("val in remove from values:",val)
    for i in order:
        if val in order[i]:
            order[i].remove(val)
    # print("order after remove:",order)

def remove_keys(key_list):
    for i in key_list:
        order.pop(i)
        # print(order)

# print("order len: ", len(order))
while len(order) > 0:
    next_list = []
    for i in order:
        if order[i] == []:
            next_list.append(i)
            # finished_list.append(i)
            # remove_from_values(i)
    next_list = sorted(next_list)
    print("next_list:",next_list)
    # for j in next_list:
    cur_val = next_list.pop(0)
    finished_list.append(cur_val)
    remove_from_values(cur_val)
    # remove_keys(cur_val)
    order.pop(cur_val)
    # print("order len: ",len(order))

print("\n*****done*****")
print(finished_list)
answer = ''.join(finished_list)

print(answer)
