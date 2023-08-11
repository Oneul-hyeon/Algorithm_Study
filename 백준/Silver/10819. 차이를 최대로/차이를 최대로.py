import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1. 주어진 배열의 순열 구하기
permutation = permutations(array, n)
# 2. 최댓값 비교
ans = -sys.maxsize
for perm in permutation :
    ans = max(ans, sum([abs(perm[i-1] - perm[i]) for i in range(1, n)]))
# 3. 결과 출력
print(ans)