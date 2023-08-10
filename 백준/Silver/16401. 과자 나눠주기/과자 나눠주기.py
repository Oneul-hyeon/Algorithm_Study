import sys
input = sys.stdin.readline

m, n = map(int, input().split())
cookies = list(map(int, input().split()))

# 1. left, right 설정
left, right = 1, max(cookies)
# 2.
while left <= right :
    # 2-1. mid 값 구하기
    mid = (left + right) // 2
    # 2-2. 해당 길이로 나눌 수 있는 과자 개수 구하기
    count = 0
    for cookie in cookies : count += cookie // mid
    # 2-3. 구한 과자 개수가 조카 수보다 많거나 같은 경우
    if count >= m : left = mid + 1
    # 2-4. 구한 과자 개수가 조카 수보다 적은 경우
    else : right = mid - 1
# 3. 결과 출력
print(right)