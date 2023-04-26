import sys
input = sys.stdin.readline

n = int(input())
# 1. 용액 리스트에 입력받고 정렬
array = sorted(list(map(int, input().split())))
# 2. left, right 설정
left, right = 0, n-1
# 3. 최솟값 변수 설정
min_summation = 2*1000000000 + 1
# 5. 방식 3~5에 따라 최솟값 재설정 및 left, right 값 재설정
while left < right :
    summation = array[left] + array[right]
    if min_summation > abs(summation) :
        min_summation = abs(summation)
        ans = [array[left], array[right]]
    if summation < 0 : left += 1
    elif summation > 0 : right -= 1
    else : break
# 6. 최솟값 출력
print(*ans)