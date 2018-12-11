def play_game(marbles, players):
    scores = {i:0 for i in range(players)}
    circle = [0]
    prev_index = 0

    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            next_index = prev_index - 7
            if next_index < 0:
                next_index = len(circle) + next_index

            # print(circle[next_index])
            # print(marble)
            # print(marble % players)

            scores[marble % players] += circle.pop(next_index) + marble
            prev_index = next_index
        else:
            next_index = (prev_index + 2)

            if next_index == len(circle):
                circle.append(marble)
            elif next_index > len(circle):
                next_index -= len(circle)
                circle.insert(next_index, marble)
            else:
                circle.insert(next_index, marble)
            prev_index = next_index

    return max(scores.values())

# print(play_game(25,9))
#
# print(play_game(1618,10))
#
# print(play_game(7999,13))
#
# print(play_game(1104,17))
#
# print(play_game(6111,21))
#
# print(play_game(5807,30))

# print(play_game(70953,405))
#
print(play_game(7095300,405))