import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
# 1. 가장 높은 나무의 높이 구하기
# 2. start = 0, end = 가장 높은 나무의 높이
start, end = 0, max(array)
# 3. while문
while start <= end :
    # 3-1. mid 값 설정
    mid = (start + end) // 2
    total_m = 0
    # 자른 나무의 총 길이 구하기
    for i in array :
        if mid < i :
            total_m += i - mid
    # 3-2. mid값으로 구한 총 나무 길이가 m보다 같거나 클 경우
    if total_m >= m : start = mid+1
    # 3-3 mid값으로 구한 총 나무 길이가 m보다 작을 경우 end = mid
    else : end = mid-1
print(end)