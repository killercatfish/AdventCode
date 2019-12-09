def get_input(file_name):
    input = []

    with open(f'../input/{file_name}.txt'.format(file_name, 'wb')) as f:
        # with open("input/day5_test_input.txt") as f:
        #     input = f.split(',')
        for line in f:
            l = line.strip()
            # print(l)
            layer = []
            counter = 1
            for d in l:
                layer.append(int(d))
                if counter % 150 == 0:
                    input.append(layer)
                    layer = []
                counter += 1

    return input

input = get_input('day_8_input')

print(input[0])

WIDTH = 25
HEIGHT = 6

LAYERS = int(len(input))

print(LAYERS)
print(input)

num_zeros = []
num_ones = []
num_twos = []
for i in input:
    num_zeros.append(i.count(0))
    num_ones.append(i.count(1))
    num_twos.append(i.count(2))
min_num = num_zeros.index(min(num_zeros))
print(min_num)
ones = num_ones[min_num]
twos = num_twos[min_num]
print(ones * twos)
