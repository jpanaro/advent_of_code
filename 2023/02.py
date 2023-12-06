from aocd import get_data
from parse import parse, findall, search

data = get_data(day=2, year=2023)


def p1():
    id_total = 0
    for game in data.split('\n'):
        game_id = list(search("Game {}:", game))[0]
        green = list(r[0] for r in findall("{:d} green", game))
        blue = list(r[0] for r in findall("{:d} blue", game))
        red = list(r[0] for r in findall("{:d} red", game))
        
        if any(x > 13 for x in green):
            continue
        if any(x > 14 for x in blue):
            continue
        if any(x > 12 for x in red):
            continue

        id_total += int(game_id)
    
    return id_total




print(p1())
        
