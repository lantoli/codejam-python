# https://code.google.com/codejam/contest/2845486/dashboard#s=p3

FILENAME = "D-small-practice-2"

import sys
sys.stdin = open(FILENAME + ".in", 'r')
#sys.stdout = open(FILENAME + ".out", 'w')

def get_line(): return input()
def get_int(): return int(get_line())
def get_ints(): return [int(x) for x in get_line().split()]


import numpy as np
from itertools import product

incs = [ (-1,0), (1,0), (0,1), (0,-1) ]

def neigbours(y, x, maxy, maxx):
    ret = []
    for y,x in [(y+inc[0],x+inc[1]) for inc in incs]:
        if y>=0 and x>=0 and y<maxy and x<maxx:
            ret.append((y,x))
    return ret


def clean_players(matrix):
    M, N = matrix.shape[0] , matrix.shape[1]
    delete = []
    oldovers = 0
    newovers = 0
    has_players = False
    for y, x in product(range(M),range(N)):
        if matrix[y,x] == 0:
            oldovers += 1
        elif matrix[y,x] < 12 or sum(map(lambda pos: matrix[pos[0],pos[1]], neigbours(y, x, M, N))) == 0:
            newovers += 1
            delete.append((y,x))
        else:
            has_players = True
    for y,x in delete: matrix[y,x] = 0
    return matrix if has_players else None


def solve():
    M, N = get_int(), get_int()
    matrix = np.matrix([get_ints() for x in range(M)])
    turns = -1
    while not clean_players(matrix) == None:
        newmatrix = np.copy(matrix)
        for y, x in product(range(M),range(N)):
            if matrix[y,x]:
                good = list(filter(lambda pos: matrix[pos[0],pos[1]] > 0, neigbours(y, x, M, N)))
                count = len(good)
                for yy,xx in good: newmatrix[yy,xx] += 12/count
                newmatrix[y,x] -= 12
        if (matrix==newmatrix).all():
            return "%d children will play forever" % np.count_nonzero(matrix)
        matrix = newmatrix
        print(matrix)
        turns += 1
    return "%d turns" % max(0,turns)


for case in range(get_int()):
    print('Case #%d: %s' % (case+1, solve()))

