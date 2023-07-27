import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
permutation = permutations(range(1, n+1))
for perm in permutation :
    for i in range(len(line)) :
        idx = perm.index(i+1)
        count = 0
        for j in range(idx-1, -1, -1) :
            if i + 1 < perm[j] : count += 1
        if count != line[i] : break
    else :
        print(*perm)
        exit()