'''Advent day 9'''
'''test 1'''
# marbles = 25
# players = 9
'''test 2'''
# marbles = 1618
# players = 10
'''test 3''' #Issue with this test.  Too Low
marbles = 7999
players = 13
'''test 4'''
# marbles = 1104
# players = 17
'''test 5'''
# marbles = 6111
# players = 21
'''test 6'''
# marbles = 5807
# players = 30
'''input''' #Test 1 got 419420 was too low
# marbles = 70953
# players = 405


player_turn = 0

current = 0
marble_list = [[0]]
print('%-*s%-*s' % (5,'[-]',5,'('+str(marble_list[0][0])+')'))

player_scores = {}
for i in range(1,players+1):
    player_scores[i] = 0
# print(player_scores)

def print_list(prev,i,player_turn):
    print('%-*s' %(5,'[' + str(player_turn) + '] '), end='')
    out = ''
    for n in range(len(prev)):
        if n == i:
            print('%-*s' %(5,'(' + str(prev[n]) + ')'),end='')
            # out += ' (' + str(n) + ')'
        else:
            print('%-*s' % (5,str(prev[n])),end='')
    print('')

prev_index = 0

for i in range(1,marbles+1):
    player_turn += 1
    if player_turn > players:
        player_turn = 1

    if i % 23 == 0:
        prev = marble_list[len(marble_list) - 1]
        player_scores[player_turn] += i
        next_index = prev_index - 7
        # print(next_index)
        prev_index = next_index
        player_scores[player_turn] += prev.pop(next_index)
        marble_list.append(prev)
        print(player_scores[player_turn])

    else:
        prev = marble_list[len(marble_list)-1]
        #prev_index = prev.index(i-1)

        next_index = (prev_index + 2)

        if next_index == len(prev):
            prev.append(i)
        elif next_index > len(prev):
            next_index -= len(prev)
            prev.insert(next_index,i)
        else:
            prev.insert(next_index, i)
        prev_index = next_index

        marble_list.append(prev)

    # print_list(prev,prev_index,player_turn)

for i in player_scores:
    print(i,':',player_scores[i])

print('max:',max(player_scores.values()))