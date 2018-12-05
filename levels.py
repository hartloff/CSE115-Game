level1 = {
    'map': [
        [1, 1, 1, 1, 1],
        [1, 7, 0, 0, 1],
        [1, 1, 1, 2, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ],
    'start': [1, 3]
};

level2 = {
    'map': [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 6, 1, 1, 1, 1, 1, 1],
        [1, 3, 1, 2, 0, 5, 7, 1],
        [1, 0, 2, 4, 2, 1, 1, 1],
        [1, 3, 1, 2, 0, 0, 0, 1],
        [1, 2, 1, 0, 5, 5, 0, 1],
        [1, 2, 1, 0, 5, 5, 6, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ],
    'start': [3, 6]
};

level3 = {
    'map': [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 2, 2, 2, 1, 7, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 3, 1, 1, 0, 1, 0, 5, 5, 2, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 1, 0, 5, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 1, 1],
        [1, 1, 1, 1, 0, 4, 0, 3, 0, 5, 0, 0, 1, 1],
        [1, 1, 5, 1, 0, 0, 0, 5, 5, 5, 5, 0, 1, 1],
        [1, 1, 5, 1, 1, 0, 0, 5, 2, 5, 0, 0, 1, 1],
        [1, 1, 6, 3, 3, 0, 0, 3, 4, 5, 0, 5, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 5, 2, 5, 6, 5, 1, 1],
        [1, 1, 4, 2, 3, 0, 0, 5, 5, 5, 5, 5, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    'start': [4, 6]
};

level4 = {
    'map': [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5, 1],
        [1, 5, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1],
        [1, 5, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1],
        [1, 5, 1, 1, 5, 5, 1, 1, 5, 1, 1, 5, 5, 1],
        [1, 5, 1, 1, 1, 5, 1, 1, 5, 1, 1, 1, 5, 1],
        [1, 5, 1, 1, 1, 5, 1, 1, 5, 1, 1, 1, 5, 1],
        [1, 1, 5, 5, 5, 1, 1, 1, 1, 5, 5, 5, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    'start': [6, 10]
};


levels = [level1, level2, level3, level4]

def getLevel(number):
    if number > len(levels):
        return levels[-1]
    if number - 1 not in range(len(levels)):
        return levels[0]
    return levels[number - 1]

    
    