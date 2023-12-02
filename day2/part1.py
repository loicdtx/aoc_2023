from collections import Counter
from functools import reduce

bag = Counter({'blue': 14, 'green': 13, 'red': 12})
tot = 0

with open('data.txt') as con:
    for line in con:
        game_id, draws = line.strip('\n').split(': ')
        game_id = int(game_id.split(' ')[1])
        draws = draws.split('; ')
        draws = [Counter({color.split(' ')[1]:int(color.split(' ')[0]) for color in draw.strip().split(', ')}) for draw in draws]
        draws_reduced = reduce(lambda x,y: x|y, draws)
        if bag >= draws_reduced:
            tot += game_id
print(tot)
