import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleeping = list(map(int, input().split()))
get_code = list(map(int, input().split()))
array = [1] * (n+3)
for who in get_code :
    if who in sleeping : continue
    for i in range(who, n+3, who) :
        if i in sleeping : continue
        if array[i] == 1: array[i] = 0

result = [0] * (n+3)
for i in range(3, n+3) :
    result[i] = result[i-1] + array[i]
for _ in range(m) :
    s, e = map(int, input().split())
    print(result[e] - result[s-1])