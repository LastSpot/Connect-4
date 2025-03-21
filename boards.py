boards = {}  # dictionary with label, test board key-value pairs

boards['test_1'] = [  
    [  0,  0 ],                       
    [  1, -1 ],
    [  1, -1 ] 
]

boards['test_2'] = [  
    [ -1,   0,  0, -1, -1 ],  
    [ -1,   1, -1,  1,  1 ],
    [  1,  -1,  1, -1,  1 ],
    [  1,   1, -1,  1, -1 ] 
]

boards['writeup_1'] = [
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0, -1,  0,  0,  0 ],
    [  0,  0,  0,  1,  0,  0,  0 ],
    [  0,  1,  0, -1,  0,  1,  0 ]
]

boards['writeup_2'] = [  
    [ -1,  1, -1, -1 ],                       
    [  1, -1,  1, -1 ],
    [  1, -2, -1,  1 ],
    [  1, -2,  1, -1 ] 
]

boards['tournament'] = [
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0, -2,  0,  0,  0 ],
    [  0,  0,  0, -2 , 0,  0,  0 ],
    [  0, -2,  0, -2,  0,  0,  0 ]
]

boards['your_test'] = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]  # put something here!

boards['your_tester'] = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, -2, 0],
    [0, -2, -2, 0]
]  # put something here!

boards['your_testest'] = [
    [0, 0, 0, 0],
    [0, 0, 0, -1],
    [0, 0, 1, 1],
    [0, 1, -1, -1]
]  # put something here!


def get_board(tag):
    if tag in boards:
        return list(reversed(boards[tag]))  # reversed so the y-coordinates read upward
    else:
        try:
            rowstr, colstr = tag.lower().split('x')
            rows = int(rowstr)
            cols = int(colstr)
            return [ [0]*cols ] * rows

        except ValueError:
            pass
        raise ValueError("bad board tag: '{}'".format(tag))       
