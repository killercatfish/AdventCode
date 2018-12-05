#https://stackoverflow.com/questions/2173797/how-to-sort-2d-array-by-row-in-python
from operator import itemgetter
import operator

input_list = []
#with open("test.txt") as f:#Test File
with open("../input/inputday4.txt") as f:#Input File
    for line in f:
        l = line.strip()
        j = l.split(']')
        # print(j[1:])
        k = j[0][6:]
        m = j[1][1:]

        input_list.append([k,m])
        #print(l)

#input_list.sort()

input_list = sorted(input_list, key=itemgetter(0))

print(input_list)

#Check if number
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#generate dict of quard id's and list of their nap start/end
guar_stats = {}
cur_guard = ""
for i in range(len(input_list)):

    if RepresentsInt(input_list[i][1].split(" ")[1][1:]):
        cur_guard = input_list[i][1].split(" ")[1][1:]
        if cur_guard not in guar_stats:
            guar_stats[cur_guard] = [] #[0] * 60
    else:
        cur_list = guar_stats[cur_guard]
        cur_list.append(int(input_list[i][0][9:]))
        # print(input_list[i][0][9:])
        guar_stats[cur_guard] = cur_list

print(guar_stats)
most_sleep = [] #[guard, minute most often asleep,total sleep]
#calculate frequency and biggest time

#Had an issue and got some help: https://www.reddit.com/r/adventofcode/comments/a385sh/day_4_part_1_python_stuck/

for i in guar_stats:
    freq = [0] * 60
    l = guar_stats[i]
    for j in range(0,len(l),2):
        # print(l[j])
        for k in range(l[j],l[j+1]):
            freq[k] += 1
    total = sum(freq)
    biggest = max(freq)
    #print(biggest)
    biggest_index = freq.index((biggest))
    #print(biggest_index)
    most_sleep.append([i,biggest_index,total])
    guar_stats[i] = [biggest,biggest_index, total,freq]

# How can I return the key instead of the actual value?
largest = max(guar_stats[data][2] for data in guar_stats.keys())
print(largest)

max_guard = 0

for i in guar_stats:
    if guar_stats[i][2] == largest:
        max_guard = i

print(guar_stats)
print(most_sleep)
print(max_guard)
answer = int(max_guard) * guar_stats[max_guard][1]

print("Solution 1:", answer)

#Must be able to python this into a simpler method?

max_minute = [] #[Guard ID, max Minute, max Minute Value]
guard_max = [0,0,0] #[ID, mm, mmv]
for i in guar_stats:
    m = max(guar_stats[i][3])
    print(m)
    ind = guar_stats[i][3].index(m)
    print(ind)
    max_minute.append([i, ind, m])
    if m > guard_max[2]:
        guard_max = [i, ind, m]

print(max_minute)
print(guard_max)
answer2 = int(guard_max[0]) * guard_max[1]
print("solution2:",answer2)





# # Old visualization method
#
# # for i in input_list[]:
#
#
# # for i in input_list:
# #     print(i)
#
# schedule = []
#
#
#
# tens = ""
# for i in range(6):
#     tens += str(i) * 10
#
# ones = "0123456789" * 6
#
# #https://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
#
# schedule.append(["Date","ID","Minute"])
# schedule.append(["","",tens])
# schedule.append(["","",ones])
#
# awake_list = '.' * 60
#
#
#
# # https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
# def RepresentsInt(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
#
# id_list = []
# '''
# This did nicely for getting dates and id's.
# '''
#
#
# for i in range(len(input_list)):
#     ID = input_list[i][1].split(" ")[1][1:]
#     DATE = input_list[i][0][:5]
#     TIME = input_list[i][0][6:8]
#     if RepresentsInt(ID):
#         id_list.append(ID)
#         #print("ID is an int: ", ID)
#         #new_entry = "%-*s%-*s" % (8, i[0][:6], 8, ID)
#         if int(TIME) != 0:
#             DATE = input_list[i+1][0][:5]
#
#         schedule.append([DATE,ID,awake_list])
#
# '''
# Remove guard shift start
# '''
# def determine(x):
#     #print(x[1].split(" ")[1][1:])
#     return RepresentsInt(x[1].split(" ")[1][1:])
#
# # https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
# input_list[:] = [x for x in input_list if not determine(x)]
#
#
# # print(id_list)
# # print("****")
#
# '''
# Make dictionary with date as key & [[times],[id],[hash tag]]
# '''
#
# actions_dict = {}
#
# for i in input_list:
#     DATE = i[0][:5]
#
#     if DATE in actions_dict.keys():
#         sleep_pattern = actions_dict[DATE]
#         sleep_pattern[0].append(int(i[0][-2:]))
#     else:
#         actions_dict[DATE] = [[int(i[0][-2:])],id_list[0]] #[awakes,asleeps] times
#         id_list = id_list[1:]
#
# #print(actions_dict)
#
# '''
# Print the schedule
# '''
#
# def print_actions():
#     heading = "%-*s%-*s%s" % (8,"Date",8,"ID","Minute")
#     tens_heading = "%-*s%-*s%s" % (8,"",8,"",tens)
#     ones_heading = "%-*s%-*s%s" % (8,"",8,"",ones)
#     print(heading)
#     print(tens_heading)
#     print(ones_heading)
#     for i in actions_dict:
#        print("%-*s%-*s%s" % (8,i,8,actions_dict[i][1],actions_dict[i][0]))
#
#
# '''
# Build hashtag string
# '''
#
# for i in actions_dict:
#     sleep_list = actions_dict[i][0]
#     num_sleep = len(sleep_list)
#     a_list = list(awake_list)
#
#     for j in range(0,num_sleep,2):
#         # print("h")
#         # L[2:4] = ["foo"] * (4 - 2)
#         start = sleep_list[j]
#         end = sleep_list[j+1]
#         a_list[start:end] = '#' * (end - start)
#
#     actions_dict[i][0] = "".join(a_list)
#
# print_actions()
#
# # for i in schedule:
# #     print("%-*s%-*s%s" % (8,i[0],8,i[1],i[2]))
#
# guard_sleep_time = {}
# for i in actions_dict:
#     id = actions_dict[i][1]
#     time_sleeping = list(actions_dict[i][0]).count('#')
#     #print(time_sleeping)
#     if id in guard_sleep_time.keys():
#         time_sleeping = time_sleeping + guard_sleep_time[id]
#     guard_sleep_time[id] = time_sleeping
#
# print(guard_sleep_time)
#
# largest = max(guard_sleep_time, key = guard_sleep_time.get)
#
# when_largest_asleep = [0] * 60
#
# for i in actions_dict:
#
#     if actions_dict[i][1] == largest:
#         print(actions_dict[i][1])
#         for c in range(len(actions_dict[i][0])):
#             if actions_dict[i][0][c] == '#':
#                 when_largest_asleep[c] += 1
#
# print("guard", largest, "with", guard_sleep_time[largest], "minutes asleep")
#
# max_min = [0,0] #minute, value
# for i in range(len(when_largest_asleep)):
#     if when_largest_asleep[i] >= max_min[1]:
#         max_min[0] = i
#         max_min[1] = when_largest_asleep[i]
# print(when_largest_asleep)
# print(max_min)
#
# print(int(largest) * max_min[0])