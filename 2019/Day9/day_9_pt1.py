input = {}

def get_input(file_name):

    with open(f'../input/{file_name}.txt'.format(file_name, 'wb')) as f:
        # with open("input/day5_test_input.txt") as f:
        #     input = f.split(',')
        for line in f:
            l = line.strip()
            l = l.split(')')
            print(l)
            input[l[1]] = l[0]


    return input

input = get_input('day_9_input')
print(input)
total = 0
for key in input:
    current = 1
    next = input[key]
    while next != 'COM':
        current += 1
        next = input[next]
    total += current
print(total)