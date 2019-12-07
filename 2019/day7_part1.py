'''
AoC 2019 7.1
'''

# get puzzle input
def get_input(file_name):
    input = []

    with open(f'input/{file_name}.txt'.format(file_name, 'wb')) as f:
        # with open("input/day5_test_input.txt") as f:
        #     input = f.split(',')
        for line in f:
            l = line.strip()
            # print(l)
            input = [int(n) for n in l.split(',')]
    return input

class Int_Code_Computer():
    def __init__(self, input):
        self.instructions = []
        self.input = input.copy()
        self.instructions_index = 0
        self.output = ""

    # get command values
    def get_codes(self, command):
        command = f"{command:05}"  # Get 5 character, 0's

        # Assign values
        op_code = int(command[3:])
        param_mode_1 = int(command[2])
        param_mode_2 = int(command[1])
        param_mode_3 = int(command[0])

        return op_code, param_mode_1, param_mode_2, param_mode_3

    # return the value of first parameter based on mode
    def get_p1_val(self, p1, input, command_index):
        if p1 == 0:
            return input[input[command_index + 1]]
        else:
            return input[command_index + 1]

    # return the value of second parameter based on mode
    def get_p2_val(self, p2, input, command_index):
        if p2 == 0:
            return input[input[command_index + 2]]
        else:
            return input[command_index + 2]

    # return the value of third parameter based on mode
    def get_p3_val(self, p3, input, command_index):
        if p3 == 0:
            return input[command_index + 3]
        else:
            return command_index + 3

    def get_op_3_4_val(self, p1, input, command_index):
        if p1 == 0:
            return input[command_index + 1]
        else:
            return command_index + 1

    # get values from input with op codes 1-2, params 1-3
    def get_all_values(self, command, input, command_index):
        return self.get_p1_val(command[1], input, command_index), self.get_p2_val(command[2], input, command_index), self.get_p3_val(command[3], input, command_index)

    # update list if 1
    def run_op_1(self, command, input, command_index):
        vals =  self.get_all_values(command, input, command_index)
        input[vals[2]] = vals[0] + vals[1]

    # update list if 2
    def run_op_2(self, command, input, command_index):
        vals = self.get_all_values(command, input, command_index)
        input[vals[2]] = vals[0] * vals[1]

    # input instruction
    def run_op_3(self, command, input, command_index):
        val = self.get_op_3_4_val(command[1], input, command_index)
        input[val] = self.instructions[self.instructions_index]
        self.instructions_index += 1

    def run_op_4(self, command, input, command_index):
        val = self.get_op_3_4_val(command[1], input, command_index)
        # print(input[val])
        self.output += str(input[val])

    def run_op_5(self, command, input, command_index):
        vals = self.get_all_values(command, input, command_index)
        if vals[0] != 0:
            return vals[1]
        else:
            return command_index + 3

    def run_op_6(self, command, input, command_index):
        vals = self.get_all_values(command, input, command_index)
        if vals[0] == 0:
            return vals[1]
        else:
            return command_index + 3

    def run_op_7(self, command, input, command_index):
        vals = self.get_all_values(command, input, command_index)
        if vals[0] < vals[1]:
            input[vals[2]] = 1
        else:
            input[vals[2]] = 0

    def run_op_8(self, command, input, command_index):
        vals = self.get_all_values(command, input, command_index)
        if vals[0] == vals[1]:
            input[vals[2]] = 1
        else:
            input[vals[2]] = 0

    # run command, return new index
    # def run_command(input, )

    # Solve the Puzzle
    def solve_puzzle(self, instructions):
        self.instructions = instructions
        self.instructions_index = 0
        command_index = 0
        input = self.input
        # print(input)
        op_codes = self.get_codes(input[0])
        # print(str(op) + "\n" + str(p1) + "\n" + str(p2) + "\n" + str(p3))

        # print(op_codes)
        # print(input)
        # run_op_3(op_codes, input, command_index, instruction)
        # print(input)


        while op_codes[0] != 99:
            # print(op_codes)
            # print(input)
            if op_codes[0] == 1:
                self.run_op_1(op_codes, input, command_index)
                command_index += 4

            elif op_codes[0] == 2:
                self.run_op_2(op_codes, input, command_index)
                command_index += 4

            elif op_codes[0] == 3:
                # print("**OP CODE 3**")
                self.run_op_3(op_codes, input, command_index)
                # print(input)
                command_index += 2

            elif op_codes[0] == 4:
                self.run_op_4(op_codes, input, command_index)
                command_index += 2

            elif op_codes[0] == 5:
                command_index = self.run_op_5(op_codes, input, command_index)

            elif op_codes[0] == 6:
                command_index = self.run_op_6(op_codes, input, command_index)

            elif op_codes[0] == 7:
                self.run_op_7(op_codes, input, command_index)
                command_index += 4

            elif op_codes[0] == 8:
                self.run_op_8(op_codes, input, command_index)
                command_index += 4

            op_codes = self.get_codes(input[command_index])
        # print(self.output)
        self.input = input
        return self.output

input = get_input('day_7_input')

from itertools import permutations
codes = [0, 1, 2, 3, 4]
perms = list(permutations(codes,5))

# signals = []
# run = 1
# for i in perms:
#     # print("**RUN #" + str(run) + "**")
#     # print("Perm: " + str(i))
#     signal = 0
#     result = 0
#     for j in range(len(i)):
#         int_comp = Int_Code_Computer(input.copy())
#         instructions = [i[j], int(result)]
#
#         result = int_comp.solve_puzzle(instructions)
#         signal += int(result)
#     signals.append(signal)
#     run += 1
#
# print(signals)
# print(max(signals))


'''Tests
Solution: new copy of input each amp, not sharing among iteration
always give result of previous to next as 2nd input
'''
# inp = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
codes = [4,3,2,1,0]
sum = 0
result = 0
for j in range(len(codes)):
    int_comp = Int_Code_Computer([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    instructions = [codes[j], int(result)]
    result = int_comp.solve_puzzle(instructions)
    sum += int(result)
print("Sum: " + str(sum))
