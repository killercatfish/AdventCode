'''
Advent of code 2018
1) How do you import from a file
    a) Did you create a file for input?
2) What format would you like the input to be in?
    a) Ideally, what type of value would the input have been?
3) What data structure could you use to organize your input?
4) What is the question asking?
    a) How should you compute it?
5) Wrong answer?
'''

input_list = []

with open("input/input.txt") as f:
    for line in f:
        l = line.strip()

        if l[0] == '-':
            input_list.append(int(l))
        else:
            input_list.append(int(l[1:]))
        #input_list.append([l[:1],int(l[1:])])

sum = 0
for n in range(len(input_list)):
    sum += input_list[n]


print(sum)