import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, q = map(int, input().split())
array = sorted([list(map(int, input().split())) for _ in range(n)])
array_col = list(zip(*array))
spicy = list(array_col[0])
sweet = list(array_col[1])
for _ in range(q) :
    u, v, x, y = map(int, input().split())
    sweet_lst = sorted(sweet[bisect_left(spicy, u): bisect_right(spicy, v)])
    print(bisect_right(sweet_lst, y) - bisect_left(sweet_lst, x))
