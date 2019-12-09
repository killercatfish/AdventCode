class Int_Code_Computer():
    def __init__(self, input, mode):
        self.instructions = []
        self.input = input.copy()
        self.instructions_index = 0
        self.output = ""
        self.command_index = 0
        self.mode = mode # 0 not loop, 1 for loop

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
    def get_p1_val(self, p1, input):
        if p1 == 0:
            return input[input[self.command_index + 1]]
        else:
            return input[self.command_index + 1]

    # return the value of second parameter based on mode
    def get_p2_val(self, p2, input):
        if p2 == 0:
            return input[input[self.command_index + 2]]
        else:
            return input[self.command_index + 2]

    # return the value of third parameter based on mode
    def get_p3_val(self, p3, input):
        if p3 == 0:
            return input[self.command_index + 3]
        else:
            return self.command_index + 3

    def get_op_3_4_val(self, p1, input):
        if p1 == 0:
            return input[self.command_index + 1]
        else:
            return self.command_index + 1

    # get values from input with op codes 1-2, params 1-3
    def get_all_values(self, command, input):
        return self.get_p1_val(command[1], input), self.get_p2_val(command[2], input), self.get_p3_val(command[3], input)

    # update list if 1
    def run_op_1(self, command, input):
        vals =  self.get_all_values(command, input)
        input[vals[2]] = vals[0] + vals[1]

    # update list if 2
    def run_op_2(self, command, input):
        vals = self.get_all_values(command, input)
        input[vals[2]] = vals[0] * vals[1]

    # input instruction
    def run_op_3(self, command, input):
        val = self.get_op_3_4_val(command[1], input)
        input[val] = self.instructions[self.instructions_index]
        self.instructions_index += 1

    def run_op_4(self, command, input):
        val = self.get_op_3_4_val(command[1], input)
        # print(input[val])
        self.output += str(input[val])

    def run_op_5(self, command, input):
        vals = self.get_all_values(command, input)
        if vals[0] != 0:
            return vals[1]
        else:
            return self.command_index + 3

    def run_op_6(self, command, input):
        vals = self.get_all_values(command, input)
        if vals[0] == 0:
            return vals[1]
        else:
            return self.command_index + 3

    def run_op_7(self, command, input):
        vals = self.get_all_values(command, input)
        if vals[0] < vals[1]:
            input[vals[2]] = 1
        else:
            input[vals[2]] = 0

    def run_op_8(self, command, input):
        vals = self.get_all_values(command, input)
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

        input = self.input
        # print(input)

        op_codes = self.get_codes(input[self.command_index])

        print(op_codes)
        print(input)

        previous_command = 99

        while op_codes[0] != 99:
            # print(op_codes)
            # print(input)
            if op_codes[0] == 1:
                self.run_op_1(op_codes, input)
                self.command_index += 4

            elif op_codes[0] == 2:
                self.run_op_2(op_codes, input)
                self.command_index += 4

            elif op_codes[0] == 3:
                # print("**OP CODE 3**")
                self.run_op_3(op_codes, input)
                # print(input)
                self.command_index += 2

            elif op_codes[0] == 4:
                self.run_op_4(op_codes, input)
                self.command_index += 2
                if self.mode == 1:
                    break

            elif op_codes[0] == 5:
                self.command_index = self.run_op_5(op_codes, input)

            elif op_codes[0] == 6:
                self.command_index = self.run_op_6(op_codes, input)

            elif op_codes[0] == 7:
                self.run_op_7(op_codes, input)
                self.command_index += 4

            elif op_codes[0] == 8:
                self.run_op_8(op_codes, input)
                self.command_index += 4

            previous_command = op_codes[0]
            print("previous: " + str(previous_command))

            op_codes = self.get_codes(input[self.command_index])

        # print(self.output)
        self.input = input

        return (self.output, previous_command)