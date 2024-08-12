import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1. 투 포인터 인덱스 설정
left, right = 0, n-1
# 2. 초기값 설정
ans = array[left] + array[right]
# 3.
while left < right :
    # 3-1. 두 수의 합이 0보다 큰 경우
    if (summation := array[left] + array[right]) > 0 :
        right -= 1
    # 3-2. 두 수의 합이 0보다 작은 경우
    else :
        left += 1
    # 3-3. 결과값 업데이트
    if abs(ans) > abs(summation) : ans = summation
# 4. 결과 출력
print(ans)