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

#This did nicely for getting dates and id's.  But I am going to use a while loop for real processing
    
# for i in range(len(input_list)):
#     ID = input_list[i][1].split(" ")[1][1:]
#     DATE = input_list[i][0][:5]
#     TIME = input_list[i][0][6:8]
#     if RepresentsInt(ID):
#         #print("ID is an int: ", ID)
#         #new_entry = "%-*s%-*s" % (8, i[0][:6], 8, ID)
#         if int(TIME) != 0:
#             print(TIME)
#             DATE = input_list[i+1][0][:5]
#
#         schedule.append([DATE,ID,""])


'''
Going to make it so that each entry is separate item in list
'''
# for i in input_list:
#     print(i[1].split(" "))
#     ID = i[1].split(" ")[1][1:]
#     if RepresentsInt(ID):
#         #print("ID is an int: ", ID)
#         new_entry = "%-*s%-*s" % (8, i[0][:6], 8, ID)
#         schedule.append(new_entry)
#     # else:
#     #     print("ID is not an int: ", ID)
#     #
#     # if i[0][:6] != schedule[len(schedule)-1][:6]:
#     #
#     #     new_entry = "%-*s%-*s" %(8,i[0][:6],8,i[0][6:])
#     #     schedule.append(new_entry)

for i in schedule:
    print(i)

i = 0
while i < len(input_list):
    print(i)
    i += 15