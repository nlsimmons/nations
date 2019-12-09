from pprint import pprint


def incrange(start, end):
    return range(start, end + 1)

def adjacent(x_start, y_start, x_limit=None, y_limit=None):
    square = []
    for x in incrange(x_start - 1, x_start + 1):
        for y in incrange(y_start - 1, y_start + 1):
            if((x == x_start and y == y_start) or
              (x_limit != None and (x < 0 or x >= x_limit)) or
              (y_limit != None and (y < 0 or y >= y_limit))):
                continue
            square.append((x, y))
    return square