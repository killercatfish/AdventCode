'''
AoC 2019 7.1
'''

# get puzzle input
def get_input(file_name):
    input = []

    with open(f'../input/{file_name}.txt'.format(file_name, 'wb')) as f:
        # with open("input/day5_test_input.txt") as f:
        #     input = f.split(',')
        for line in f:
            l = line.strip()
            # print(l)
            input = [int(n) for n in l.split(',')]
    return input

from Intcode import Int_Code_Computer

input = get_input('day_7_input')

from itertools import permutations
codes = [5, 6, 7, 8, 9]
perms = list(permutations(codes,5))

signals = []
run = 1
for i in perms:
    result = (0, 0)
    comp_list = []
    for a in range(5):
        comp_list.append(Int_Code_Computer(input.copy(), 1))

    counter = 0

    while True:
        instructions = []
        if counter >= 0 and counter < 5:
            instructions = [i[counter], int(result[0])]
        else:
            instructions = [int(result[0])]

        result = comp_list[counter % 5].solve_puzzle(instructions)

        # print('result: ' + str(result) + '\nmachine: ' + str(counter % 5))

        counter += 1

        if(result[1] == 99):
            # print(comp_list[4].get_last_output())
            signals.append(comp_list[4].get_last_output())
            break

print(signals)
print(max(signals))

'''Tests
Solution: new copy of input each amp, not sharing among iteration
always give result of previous to next as 2nd input
'''


result = (0, 0)

comp_list = []
'''
Test 1
'''
# codes = [9,8,7,6,5]
# for a in range(5):
#     comp_list.append(Int_Code_Computer([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], 1))

'''
Test 2
'''
# codes = [9,7,8,5,6]
# for a in range(5):
#     comp_list.append(Int_Code_Computer([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], 1))
#
# counter = 0
#
# while True:
#     instructions = []
#     if counter >= 0 and counter < 5:
#         instructions = [codes[counter], int(result[0])]
#     else:
#         instructions = [int(result[0])]
#
#     result = comp_list[counter % 5].solve_puzzle(instructions)
#
#     print('result: ' + str(result) + '\nmachine: ' + str(counter % 5))
#
#     counter += 1
#
#     if(result[1] == 99):
#         print(comp_list[4].get_last_output())
#         break

# print("Sum: " + result[0])
