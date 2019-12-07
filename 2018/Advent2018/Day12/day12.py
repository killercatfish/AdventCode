data = []
# with open("test.txt") as f:
with open("../input/inputday12.txt") as f:#Input File
    # data = [line.strip()[0:5] for line in f if line[-1].strip() == '#']#How to make this work?
    for line in f:
        l = line.strip()
        if l[-1] == '#':
            # print(l[0:5])
            data.append(l[0:5])

'''
added .. to beginning of initial -2, -1
'''
initial = '#.#.#...#..##..###.##.#...#.##.#....#..#.#....##.#.##...###.#...#######.....##.###.####.#....#.#..##'

'''
initial test
'''
# initial = '#..#.#..##......###...###'
# print(data)
#
# print(initial)
# print(len(initial))

left_shift = 0

for j in range(20):
    flag = False
    next_gen = ''
    for i in range(-5+left_shift,len(initial)+5):

        append = ''
        if i == -5+left_shift:
            test = '.....'
            if test in data:
                next_gen += '#'
                left_shift += i
            # print(test)
        if i == -4+left:
            test = '....'+initial[0]
            if test in data:
                next_gen += '#'
                left_shift += i
            # print(test)
        if i == -3:
            test = '...' + initial[0:2]
            if test in data:
                next_gen += '#'
                left_shift += i
            # print(test)
        if i == -2:
            test = '..' + initial[0:3]
            if test in data:
                next_gen += '#'
                left_shift += i
            else:
                next_gen += '.'
                left_shift += i
            # print(test)
        if i == -1:
            test = '.' + initial[0:4]
            if test in data:
                next_gen += '#'
                left_shift += i
            else:
                next_gen += '.'
            # print(test)
        if i == len(initial)-4:
            test = initial[i:] + '.'
            if test in data:
                next_gen += '#'

            else:
                next_gen += '.'
            # print(test)
        if i == len(initial)-3:
            test = initial[i:] + '..'
            if test in data:
                next_gen += '#'
            else:
                next_gen += '.'
            # print(test)
        if i == len(initial)-2:
            test = initial[i:] + '...'
            if test in data:
                next_gen += '#'
            # print(test)
        if i == len(initial)-1:
            test = initial[i:] + '....'
            if test in data:
                next_gen += '#'
            # print(test)
        if i == len(initial):
            test = '.....'
            if test in data:
                next_gen += '#'
            # print(test)
        if i > -1 and i < len(initial)-4:
            test = initial[i:i+5]
            if test in data:
                next_gen += '#'
                # print('test:',test,"\nindex:",data.index(test),'data:',data[data.index(test)])
            else:
                next_gen += '.'
            # print(test)
        # if append == '#':
        #     next_gen += '#'
        # else:
        #     next_gen += '.'

    print(next_gen)
    initial = next_gen

print('initial:\n',initial)
print(initial.count('#'))
print('left:',left_shift)
total = 0
for i in range(len(initial)):
    val = i + left_shift
    if initial[i] == '#':
        print(i+left_shift)
        total += val
print('total:',total)

#3072 too low