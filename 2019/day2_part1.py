input = []
with open("input/day2_input.txt") as f:
# with open("input/day2_test_input_2.txt") as f:
    # input = f.split(',')
    for line in f:
        l = line.strip()
        # print(l)
        input = [int(n) for n in l.split(',')]
# print(input)

command_index = 0

while input[command_index] != 99:


    command = input[command_index]
    val_one = input[input[command_index + 1]]
    val_two = input[input[command_index + 2]]
    save_to = input[command_index + 3]

    # print('command_index: ' + str(command_index))
    # print('command: ' + str(input[command_index]))
    # print('val_one: ' + str(val_one))
    # print('val_two: ' + str(val_two))
    # print('save_to: ' + str(save_to))

    if command == 1:
        input[save_to] = val_one + val_two
    elif command == 2:
        input[save_to] = val_one * val_two

    # print(input)
    # print('\n')

    command_index += 4

# print('command_index: ' + str(command_index) + '\n')
# print('command: ' + str(input[command_index]) + '\n')
print(input[0])