import math
sum = 0

with open("input/day1_input.txt") as f:
    for line in f:
        l = line.strip()
        l = int(l)
        module_sum = 0
        while l > 0:
            l = math.floor(l / 3) - 2
            if l > 0:
                module_sum += l
        sum += module_sum
print(sum)