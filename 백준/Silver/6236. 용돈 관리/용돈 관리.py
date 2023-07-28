import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
# 1. 이분탐색을 위한 left, right 변수 설정
left, right = max(array), sum(array)
# 2.
while left <= right :
    # 2-1. mid 값 설정
    mid = (left + right) // 2
    # 2-2. 인출 횟수 구하기
    now = 0
    count = 0
    for money in array :
        if now - money >= 0 : now -= money
        else :
            count += 1
            now = mid - money
    # 2-3. 인출 횟수가 M보다 크거나 같은 경우
    if count > m : left = mid + 1
    else : right = mid - 1
# 3. 결과 출력
print(left)