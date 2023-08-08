import sys, math
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())

# 1. left, right 설정
left, right = m // n, max(array)
# 2.
while left <= right :
    # 2-1. mid 값 구하기
    mid = (left+right) // 2
    # 2-2. 배정되는 예산 구하기
    cost = 0
    for c in array :
        cost += mid if mid <= c else c
    # 2-3. 배정되는 예산이 총 예산보다 작을 경우
    if cost <= m: left = mid + 1
    # 2-3. 배정되는 예산이 총 예산보다 클 경우
    elif cost > m: right = mid - 1
# 3. 결과 출력
print(right)