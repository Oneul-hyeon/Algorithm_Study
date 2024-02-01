import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1. 계산 함수 정의
def calculate(c) :
    # 1-1. 변수 생성
    value = 0
    # 1-2.
    for comb in combinations(array, c) :
        # 1-2-1. 공집합에 해당하는 수 생성
        num = 1
        for x in comb : num *= x
        # 1-2-2. n보다 클 경우 continue
        if num > n : continue
        # 1-2-3. 공집합의 수 더하기
        value += n // num
    # 1-3. 값 리턴
    return value

n = int(input())
# 2. 고려 범위 구하기
array = [int('1' * i) for i in [2, 3, 5, 7, 11, 13, 17] if int('1' * i) <= n]
# 3. flag 선언
flag = 1
# 4. 출력 변수 생성
ans = 0
# 5.
for c in range(1, len(array) + 1) :
    # 5-1. 출력 변수 업데이트
    ans += flag * calculate(c)
    # 5-2. flag 업데이트
    flag *= -1
# 6. 결과 출력
print(ans)