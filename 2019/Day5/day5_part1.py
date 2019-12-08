input = []
with open("input/day5_input.txt") as f:
# with open("input/day5_test_input.txt") as f:
#     input = f.split(',')
    for line in f:
        l = line.strip()
        # print(l)
        input = [int(n) for n in l.split(',')]
print(input)

command_index = 0


output = ""

while True:
    command = f"{input[command_index]:05}" #Get 5 character, 0's

    # Assign values
    op_code = int(command[3:])
    param_mode_1 = int(command[2])
    param_mode_2 = int(command[1])
    param_mode_3 = int(command[0])

    # print("command index: " + str(command_index) + "\ncommand: " + command + "\nop_code: " + str(op_code) + "\nparam_mode_1: " + str(param_mode_1) + "\nparam_mode_2: " + str(
    #     param_mode_2) + "\nparam_mode_3: " + str(param_mode_3))

    if op_code == 99:
        break
    elif op_code == 1 or op_code == 2:
        save_to = 0
        val_one = 0
        val_two = 0
        if param_mode_1 == 0:
            val_one = input[input[command_index + 1]]
        else:
            val_one = input[command_index + 1]
        if param_mode_2 == 0:
            val_two = input[input[command_index + 2]]
        else:
            val_two = input[command_index + 2]
        if param_mode_3 == 0:
            save_to = input[command_index + 3]
        else:
            save_to = command_index + 3
        if op_code == 1:
            # print(str(save_to) + " " + str(val_one) + " " + str(val_two))
            input[save_to] = val_one + val_two
        else:
            input[save_to] = val_one * val_two
        command_index += 4

    elif op_code == 3:
        if param_mode_1 == 0:
            print(command_index + 1)
            print(input[command_index + 1])
            print(input[input[command_index + 1]])

            input[input[command_index + 1]] = 1
            print(input)
        else:
            input[command_index + 1] = 1
        command_index += 2
    elif op_code == 4:
        if param_mode_1 == 0:
            print(input[input[command_index + 1]])
        else:
            print(input[command_index + 1])
        command_index += 2

    #
    # print("command: " + command + "\nop_code: " + str(op_code) + "\nparam_mode_1: " + str(param_mode_1) + "\nparam_mode_2: " + str(
    #     param_mode_2) + "\nparam_mode_3: " + str(param_mode_3))

    '''
    Next is to determine if it is a 3 or 4 and command index goes up by just 2
    use old code otherwise
    '''