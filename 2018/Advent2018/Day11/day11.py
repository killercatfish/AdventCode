# def find_largest_total_power(grid_serial):
#     return 0 , 0
#
#
# print(find_largest_total_power(10))

def get_fuel_cell_level(x,y,serial):
    rack_id = x + 10

    power_level = rack_id * y

    power_level += serial

    power_level *= rack_id

    if power_level > 100:
        hun = int(str(power_level)[-3])

        power_level = hun

    else:
        power_level = 0

    power_level-=5
    return power_level


def find_max_part2(pcs):
    square_list = {}
    max_val = [(0, 0), -10000, 1]

    for a in range(300):
        for x in range(300-a):
            for y in range(300-a):

                sub_list = [item[x:x + a] for item in pcs[y:y + a]]
                total = sum(map(sum, sub_list))
                # print('(',x,',',y,')',total)
                if total > max_val[1]:
                    max_val[0] = [x + 1, y + 1]  # add one to x and y since real list is 1-300
                    max_val[1] = total
                    # map the sum
                    # add to square list key is x,y
    print(max_val)

def find_max(pcs):
    square_list = {}
    max_val = [(0,0), -10000]


    for x in range(297):
        for y in range(297):

            sub_list = [item[x:x+3] for item in pcs[y:y+3]]
            total = sum(map(sum, sub_list))
            # print('(',x,',',y,')',total)
            if total > max_val[1]:
                max_val[0] = [x+1,y+1]#add one to x and y since real list is 1-300
                max_val[1] = total
            #map the sum
            #add to square list key is x,y
    print(max_val)
    #return max value and key


def find_max_any_size(pcs):
    max_val = [(0, 0), -10000,0]
    for size in range(1,301):
        for x in range(301-size):
            for y in range(301-size):

                sub_list = [item[x:x + size] for item in pcs[y:y + size]]
                total = sum(map(sum, sub_list))
                # print('(',x,',',y,')',total)
                if total > max_val[1]:
                    max_val[0] = [x + 1, y + 1]  # add one to x and y since real list is 1-300
                    max_val[1] = total
                    max_val[2] = size
                    # map the sum
                    # add to square list key is x,y
    print(max_val)

serial = 1309
power_cells = [[get_fuel_cell_level(i,j,serial) for i in range(1,301)] for j in range(1,301)]

# for x in range(300):
#     for y in range(300):
#         print(power_cells[x][y],end=' ')
#     print('')

# find_max(power_cells)
find_max_part2(power_cells)

'''
power level tests
'''
#Test 1
# serial = 8
# print(get_fuel_cell_level(3,5))

#Test 2
# serial = 57
# print(get_fuel_cell_level(122,79))

#Test 3
# serial = 39
# print(get_fuel_cell_level(217,196))

#Test 4
# serial = 71
# print(get_fuel_cell_level(101,153))

# test = [[x+y for x in range(5)] for y in range(5) ]
# for i in range(5):
#     for j in range(5):
#         print(test[i][j],end=' ')
#     print('')
#
# new_list = [item[1:4] for item in test[1:4]]
# print(new_list)