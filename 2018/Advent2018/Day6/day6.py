input_list = []
with open("input.txt") as f:#Test File
#with open("../input/inputday5.txt") as f:#Input File
    for line in f:
        l = line.strip()
        input_list.append(l)

#print(input_list)