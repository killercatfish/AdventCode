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

two = 0
three = 0

def parse_entry(cur):
    letter_count = {}
    for i in cur:
        if i in letter_count:
            letter_count[i] = letter_count[i] + 1
        else:
            letter_count[i] = 1

    return letter_count

with open("../input/inputday2.txt") as f:
    for line in f:
        l = line.strip()
        cur = parse_entry(l)
        if 2 in cur.values():
            two += 1
        if 3 in cur.values():
            three += 1

print(two * three)