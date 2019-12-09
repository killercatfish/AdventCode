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

def path_to_com(key):
    path = []
    next = input[key]
    while next != 'COM':
        path.append(next)
        next = input[next]
    path.append(next)

    return path


input = get_input('day_6_input')

# print(input)
# total = 0
# for key in input:
#     total += len(path_to_com(key))
# print(total)
you = path_to_com('YOU')
san = path_to_com('SAN')
print(you)
print(san)

inter = set(you).intersection(san)

print(inter)

you_len = len(you)
san_len = len(san)
inter_len = len(inter)

difference = set(you) - set(san)
difference2 = set(san) - set(you)

print(difference)
print((difference2))
print(len(difference) + len(difference2))