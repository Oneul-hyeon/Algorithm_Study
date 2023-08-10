import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

# 1. left, right 설정
left, right = 0, m * max(array)
# 2.
while left <= right :
    # 2-1. mid 값 설정
    mid = (left + right) // 2
    # 2-2. 해당 시간 동안 만들 수 있는 풍선 계산
    count = 0
    for x in array : count += mid // x
    # 2-3. 만들어진 풍선 수가 m보다 작을 경우
    if count < m : left = mid + 1
    # 2-4. 만들어진 풍선 수가 m보다 크거나 같을 경우
    else : right = mid - 1
# 3. 결과 출력
print(left)