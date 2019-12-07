'''
AoC 2019 5.2
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


# get command values
def get_codes(command):
    command = f"{command:05}"  # Get 5 character, 0's

    # Assign values
    op_code = int(command[3:])
    param_mode_1 = int(command[2])
    param_mode_2 = int(command[1])
    param_mode_3 = int(command[0])

    return op_code, param_mode_1, param_mode_2, param_mode_3

# return the value of first parameter based on mode
def get_p1_val(p1, input, command_index):
    if p1 == 0:
        return input[input[command_index + 1]]
    else:
        return input[command_index + 1]

# return the value of second parameter based on mode
def get_p2_val(p2, input, command_index):
    if p2 == 0:
        return input[input[command_index + 2]]
    else:
        return input[command_index + 2]

# return the value of third parameter based on mode
def get_p3_val(p3, input, command_index):
    if p3 == 0:
        return input[command_index + 3]
    else:
        return command_index + 3

def get_op_3_4_val(p1, input, command_index):
    if p1 == 0:
        return input[command_index + 1]
    else:
        return command_index + 1

# get values from input with op codes 1-2, params 1-3
def get_all_values(command, input, command_index):
    return get_p1_val(command[1], input, command_index), get_p2_val(command[2], input, command_index), get_p3_val(command[3], input, command_index)

# update list if 1
def run_op_1(command, input, command_index):
    vals =  get_all_values(command, input, command_index)
    input[vals[2]] = vals[0] + vals[1]

# update list if 2
def run_op_2(command, input, command_index):
    vals = get_all_values(command, input, command_index)
    input[vals[2]] = vals[0] * vals[1]

# input instruction
def run_op_3(command, input, command_index, instruction):
    val = get_op_3_4_val(command[1], input, command_index)
    input[val] = instruction

def run_op_4(command, input, command_index):
    val = get_op_3_4_val(command[1], input, command_index)
    print(input[val])

def run_op_5(command, input, command_index):
    vals = get_all_values(command, input, command_index)
    if vals[0] != 0:
        return vals[1]
    else:
        return command_index + 3

def run_op_6(command, input, command_index):
    vals = get_all_values(command, input, command_index)
    if vals[0] == 0:
        return vals[1]
    else:
        return command_index + 3

def run_op_7(command, input, command_index):
    vals = get_all_values(command, input, command_index)
    if vals[0] < vals[1]:
        input[vals[2]] = 1
    else:
        input[vals[2]] = 0

def run_op_8(command, input, command_index):
    vals = get_all_values(command, input, command_index)
    if vals[0] == vals[1]:
        input[vals[2]] = 1
    else:
        input[vals[2]] = 0

# run command, return new index
# def run_command(input, )

# Solve the Puzzle
def solve_puzzle(file_name, instruction):
    command_index = 0
    input = get_input(file_name)
    op_codes = get_codes(input[0])
    # print(str(op) + "\n" + str(p1) + "\n" + str(p2) + "\n" + str(p3))

    # print(op_codes)
    print(input)
    # run_op_3(op_codes, input, command_index, instruction)
    # print(input)


    while op_codes[0] != 99:
        print(op_codes)
        print(input)
        if op_codes[0] == 1:
            run_op_1(op_codes, input, command_index)
            command_index += 4

        elif op_codes[0] == 2:
            run_op_2(op_codes, input, command_index)
            command_index += 4

        elif op_codes[0] == 3:
            run_op_3(op_codes, input, command_index, instruction)
            # print(input)
            command_index += 2

        elif op_codes[0] == 4:
            run_op_4(op_codes, input, command_index)
            command_index += 2

        elif op_codes[0] == 5:
            command_index = run_op_5(op_codes, input, command_index)

        elif op_codes[0] == 6:
            command_index = run_op_6(op_codes, input, command_index)

        elif op_codes[0] == 7:
            run_op_7(op_codes, input, command_index)
            command_index += 4

        elif op_codes[0] == 8:
            run_op_8(op_codes, input, command_index)
            command_index += 4

        op_codes = get_codes(input[command_index])

solve_puzzle('day5_input', 5)