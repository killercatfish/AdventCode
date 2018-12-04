#https://stackoverflow.com/questions/2173797/how-to-sort-2d-array-by-row-in-python
from operator import itemgetter

input_list = []
with open("test.txt") as f:#Test File
#with open("../input/inputday4.txt") as f:#Input File
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


# for i in input_list:
#     print(i)

schedule = []



tens = ""
for i in range(6):
    tens += str(i) * 10

ones = "0123456789" * 6

#https://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
# heading = "%-*s%-*s%s" % (8,"Date",8,"ID","Minute")
# tens_heading = "%-*s%-*s%s" % (8,"",8,"",tens)
# ones_heading = "%-*s%-*s%s" % (8,"",8,"",ones)
schedule.append(["Date","ID","Minute"])
schedule.append(["","",tens])
schedule.append(["","",ones])

awake_list = '.' * 60

# print(schedule[0])
# print(schedule[1])
# print(schedule[2])

# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

id_list = []

#This did nicely for getting dates and id's.  But I am going to use a while loop for real processing

for i in range(len(input_list)):
    ID = input_list[i][1].split(" ")[1][1:]
    DATE = input_list[i][0][:5]
    TIME = input_list[i][0][6:8]
    if RepresentsInt(ID):
        id_list.append(ID)
        #print("ID is an int: ", ID)
        #new_entry = "%-*s%-*s" % (8, i[0][:6], 8, ID)
        if int(TIME) != 0:
            DATE = input_list[i+1][0][:5]

        schedule.append([DATE,ID,awake_list])

def determine(x):
    #print(x[1].split(" ")[1][1:])
    return RepresentsInt(x[1].split(" ")[1][1:])

# https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
input_list[:] = [x for x in input_list if not determine(x)]


print(id_list)
print("****")

actions_dict = {}
AWAKE = True

for i in input_list:
    DATE = i[0][:5]

    if DATE in actions_dict.keys():
        sleep_pattern = actions_dict[DATE]
        if AWAKE:
            sleep_pattern[1].append(int(i[0][-2:]))
        else:
            sleep_pattern[0].append(int(i[0][-2:]))
        AWAKE = not AWAKE
    else:
        actions_dict[DATE] = [[],[],id_list[0]] #[awakes,asleeps] times
        id_list = id_list[1:]

print(actions_dict)

def print_actions():
    heading = "%-*s%-*s%s" % (8,"Date",8,"ID","Minute")
    tens_heading = "%-*s%-*s%s" % (8,"",8,"",tens)
    ones_heading = "%-*s%-*s%s" % (8,"",8,"",ones)
    print(heading)
    print(tens_heading)
    print(ones_heading)
    for i in actions_dict:
       print("%-*s%-*s%s" % (8,i,8,actions_dict[i][2],actions_dict[i][1]))

print_actions()

# for i in schedule:
#     print("%-*s%-*s%s" % (8,i[0],8,i[1],i[2]))
