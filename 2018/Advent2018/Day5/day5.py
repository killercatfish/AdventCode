input_list = []
with open("input.txt") as f:#Test File
#with open("../input/inputday5.txt") as f:#Input File
    for line in f:
        l = line.strip()
        input_list.append(l)

#print(input_list)
# print(len(input_list[0]))

polymer = input_list[0]

def react(polymer):
    # print("polymer before:",polymer)

    i = 0
    length = len(polymer)-1

    while(i < length):
        if ((polymer[i].isupper() and not polymer[i + 1].isupper()) or (not polymer[i].isupper() and \
            (polymer[i + 1].isupper()))) and (polymer[i].upper() == polymer[i+1].upper()):
            #print(polymer[i], "", polymer[i+1])
            polymer = polymer[:i] + polymer[i+2:]
            #i = 0
            if i != 0:
                i-=1
            length -= 2
        else:
            i+=1
    # print("polymer after:", polymer)
    # print("polymer size:",len(polymer))
    return len(polymer)

# react(polymer)
# print(polymer)
# print(polymer.replace('a','*').replace('A','*'))
# print(polymer)
# print(chr(65+32))
# print(chr(90+32))

min_list = []

for v in range(65,91):
    # print(chr(v),"",chr(v+32))
    react(polymer.replace(chr(v),'').replace(chr(v+32),''))
    min_list.append(react(polymer.replace(chr(v),'').replace(chr(v+32),'')))
print(min(min_list))

#print(polymer[0].upper() == polymer[2].upper())

#
# for i in range(len(polymer)-1):
#     print(i)
#     if (polymer[i].isupper() and not polymer[i+1].isupper()) or (not polymer[i].isupper() and polymer[i + 1].isupper()):
#         print(polymer[i], "", polymer[i+1])
#         polymer = polymer[:i] + polymer[i+2:]
#     # print(input_list[0][i],"",input_list[0][i].isupper())
#     # print(input_list[0][i+1], "", input_list[0][i+1].isupper())
# print("polymer:",polymer)
#
# i = 0
# length = 10
# while(i < length-1):
#     print("i",i)
#     print("length",length)
#     length-=2
#     i=0