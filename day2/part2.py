from collections import Counter
from functools import reduce

tot = 0

with open('data.txt') as con:
    for line in con:
        game_id, draws = line.strip('\n').split(': ')
        game_id = int(game_id.split(' ')[1])
        draws = draws.split('; ')
        draws = [Counter({color.split(' ')[1]:int(color.split(' ')[0]) for color in draw.strip().split(', ')}) for draw in draws]
        draws_reduced = reduce(lambda x,y: x|y, draws)
        tot += reduce(lambda x,y: x*y, draws_reduced.values())
print(tot)
