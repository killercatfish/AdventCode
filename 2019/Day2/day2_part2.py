master_input = []
with open("input/day2_input.txt") as f:
    for line in f:
        l = line.strip()
        # print(l)
        master_input = [int(n) for n in l.split(',')]

def find_output(input):
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
        if save_to >= len(master_input):
            break

        if command == 1:
            input[save_to] = val_one + val_two
        elif command == 2:
            input[save_to] = val_one * val_two

        # print(input)
        # print('\n')

        command_index += 4

    # print('command_index: ' + str(command_index) + '\n')
    # print('command: ' + str(input[command_index]) + '\n')
    # print("HELLO")
    return(input[0])

print("****START****")
nv = -1

for i in range(100):
    for j in range(100):
        # print("i: " + str(i) + " j: " + str(j))
        # This was the key, and it was hinted in the instructions.
        # Need to make fresh copies, otherise the lists of copied by reference.
        inp = master_input.copy()
        inp[1] = i
        inp[2] = j
        # print(inp)
        output = find_output(inp)
        # print(output)
        if output == 19690720:
            nv = 100 * i + j
            print(nv)
            break
        inp = master_input.copy()
        inp[1] = j
        inp[2] = i
        # print(inp)
        output = find_output(inp)
        # print(output)
        if output == 19690720:
            nv = 100 * j + i
            print(nv)
            break
    if nv != -1:
        break