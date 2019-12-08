low = 307237
high = 769058

num_list = []

# i = low
# a = i // 100000
# b = i // 10000 % 10
# c = i // 1000 % 10
# d = i // 100 % 10
# e = i // 10 % 10
# f = i % 10
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

#Part 1
for i in range(low, high+1):
    a = i // 100000
    b = i // 10000 % 10
    c = i // 1000 % 10
    d = i // 100 % 10
    e = i // 10 % 10
    f = i % 10

    if a <= b and b <= c and c <= d and d <= e and e <= f:
        if a == b or b == c or c == d or d == e or e == f:
            num_list.append(i)

print(num_list)
print(len(num_list))


#Part 2
num_list = []
for i in range(low, high+1):
    a = i // 100000
    b = i // 10000 % 10
    c = i // 1000 % 10
    d = i // 100 % 10
    e = i // 10 % 10
    f = i % 10

    if a <= b and b <= c and c <= d and d <= e and e <= f:
        if a == b or b == c or c == d or d == e or e == f:
            if (a == b and b != c):
                num_list.append(i)
            elif (a != b and b == c and c != d):
                num_list.append(i)
            elif (b != c and c == d and d != e):
                num_list.append(i)
            elif (c != d and d == e and  e != f):
                num_list.append(i)
            elif  (e == f and e != d):
                num_list.append(i)

print(num_list)
print(len(num_list))
