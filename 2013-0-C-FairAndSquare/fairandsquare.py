# https://code.google.com/codejam/contest/2270488/dashboard#s=p2

FILENAME = "C-large-practice-1"

import sys
sys.stdin = open(FILENAME + ".in", 'r')
sys.stdout = open(FILENAME + ".out", 'w')

def get_line(): return input()
def get_int(): return int(get_line())
def get_ints(): return [int(x) for x in get_line().split()]


def as_str(number, digits):
    ret = str(number)
    while len(ret) < digits: ret = "0" + ret
    return ret

def good(number):
    n = str(number)
    l = len(n)//2
    part1 = n[l-1::-1]
    part2 = n[l+1:]
    return part1 == part2

numbers = [1, 4, 9]
for digits in range(1,5):
    for part in range(10 ** (digits-1), 10 ** digits):
        number = int(as_str(part, digits) + as_str(part, digits)[::-1])
        nnumber = number*number
        if len(str(nnumber)) % 2 == 1 and good(nnumber):
            numbers.append(nnumber)
    for part in range(10 ** (digits-1), 10 ** digits):
        for middle in range(0,10):
            number = int(as_str(part, digits) + str(middle) +  as_str(part, digits)[::-1])
            nnumber = number*number
            if len(str(nnumber)) % 2 == 1 and good(nnumber):
                numbers.append(nnumber)

import bisect
def solve():
    a,b = get_ints()


    return bisect.bisect_right(numbers, b) - bisect.bisect_left(numbers, a)


for case in range(get_int()):
    print('Case #%d: %s' % (case+1, solve()))


