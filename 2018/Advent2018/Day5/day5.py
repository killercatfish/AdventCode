input_list = []
#with open("test.txt") as f:#Test File
with open("../input/inputday4.txt") as f:#Input File
    for line in f:
        l = line.strip()
        input_list.append(l)

print(input_list)