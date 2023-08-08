import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

# 1. left, right 설정
left, right = min(levels), k + max(levels)
# 2.
while left <= right :
    # 2-1. mid 값 구하기
    mid = (left + right) // 2
    # 2-2. 소요되는 레벨 구하기
    need = 0
    for l in levels :
        if mid - l > 0 : need += mid - l
    # 2-3. 소요되는 레벨이 k보다 작거나 같을 경우
    if need <= k : left = mid + 1
    # 2-4. 소요되는 레벨이 k보다 클 경우
    else : right = mid - 1
# 3. 결과 출력
print(right)