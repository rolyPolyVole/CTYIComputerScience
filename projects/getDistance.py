import math


def get_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    c_squared = dx * dx + dy * dy
    return math.sqrt(c_squared)

print(get_distance(1, 1, 4, 5))
# 5.0