#https://www.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/
from collections import deque, defaultdict

def play_game(last_marble, max_players):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

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
#
# print(play_game(70953,405))

print(play_game(7095300,405))