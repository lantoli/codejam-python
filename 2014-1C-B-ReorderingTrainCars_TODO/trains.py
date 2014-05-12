# https://code.google.com/codejam/contest/3004486/dashboard#s=p1

FILENAME = "sample"

import operator
import sys
sys.stdin = open(FILENAME + ".in", 'r')
#sys.stdout = open(FILENAME + ".out", 'w')

from itertools import groupby
from functools import reduce
from math import factorial

def get_line(): return input()
def get_int(): return int(get_line())
def get_ints(): return [int(x) for x in get_line().split()]
def get_strs(): return [x for x in get_line().split()]


def prod(iterable): return reduce(operator.mul, iterable, 1)

MOD = 1000000007


def recur(str, cars):
    total = 0
    return 1

def solve():
    get_line()
    cars = [x for x in get_line().split()]
    letters = set([ch for car in cars for ch in car])

    for idx, car in enumerate(cars):
        while len(car) > 2 and car[0] == car[1]:
            car = car[1:]
        while len(car) > 2 and car[-1] == car[-2]:
            car = car[:-1]
        for i in range(1, len(car)-1):
            if car[i] in letters:
                return 0    # middle letter can't match another car
        cars[idx] = str(car[0]) + str(car[-1])
    cars = sorted(cars)
    mult = prod([factorial(len(list(group))) % MOD for key, group in groupby(sorted(cars))]) % MOD

    return (mult * recur("A", frozenset(cars))) % MOD

for case in range(get_int()):
    print('Case #%d: %s' % (case+1, solve()))


