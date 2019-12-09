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

# input = get_input('day_7_input')
#
# from itertools import permutations
# codes = [5, 6, 7, 8, 9]
# perms = list(permutations(codes,5))

# signals = []
# run = 1
# for i in perms:
#     # print("**RUN #" + str(run) + "**")
#     # print("Perm: " + str(i))
#     result = 0
#     for j in range(len(i)):
#         int_comp = Int_Code_Computer(input.copy(), 0)
#         instructions = [i[j], int(result)]
#
#         result = int_comp.solve_puzzle(instructions)[0]
#     signals.append(int(result))
#     run += 1
#
# print(signals)
# print(max(signals))

'''Tests
Solution: new copy of input each amp, not sharing among iteration
always give result of previous to next as 2nd input
'''

codes = [9,8,7,6,5]
result = (0, 0)

comp_list = []

for a in range(5):
    comp_list.append(Int_Code_Computer([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], 1))

counter = 0

while True:
    instructions = []
    if counter >= 0 and counter < 5:
        instructions = [codes[counter], int(result[0])]
    else:
        instructions = [int(result[0])]

    result = comp_list[counter % 5].solve_puzzle(instructions)

    counter += 1

    print('result: ' + str(result))

    if(result[1] == 99):
        break

print("Sum: " + result[0])
