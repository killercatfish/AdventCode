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
codes = [0, 1, 2, 3, 4]
perms = list(permutations(codes,5))

signals = []
run = 1
for i in perms:
    # print("**RUN #" + str(run) + "**")
    # print("Perm: " + str(i))
    result = 0
    for j in range(len(i)):
        int_comp = Int_Code_Computer(input.copy(), 0)
        instructions = [i[j], int(result)]

        result = int_comp.solve_puzzle(instructions)[0]
    signals.append(int(result))
    run += 1

print(signals)
print(max(signals))


'''Tests
Solution: new copy of input each amp, not sharing among iteration
always give result of previous to next as 2nd input
'''
# inp = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# codes = [4,3,2,1,0]
# sum = 0
# result = 0
# for j in range(len(codes)):
#     int_comp = Int_Code_Computer([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
#     instructions = [codes[j], int(result)]
#     result = int_comp.solve_puzzle(instructions)
#     sum += int(result)
# print("Sum: " + result)
