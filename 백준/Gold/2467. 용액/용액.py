import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

# 1. left, right 값 설정
left, right = 0, N-1
# 2. 초기 정답 용약 설정
ans = (array[left], array[right])
# 3. 초기 최솟값 설정
min_summation = float("inf")
# 4.
while left < right:
    # 4-1. 두 수의 합의 절댓값이 최솟값보다 작을 경우
    if abs((summation:=array[left]+array[right])) < min_summation:
        # 정답 용액 업데이트
        ans = (array[left], array[right])
        # 최솟값 업데이트
        min_summation = abs(summation)
    # 4-2. 합이 음수인 경우 left 이동
    if summation < 0 : left += 1
    # 4-3. 합이 양수인 경우 right 이동
    else : right -= 1
# 5. 결과 출력
print(*ans)