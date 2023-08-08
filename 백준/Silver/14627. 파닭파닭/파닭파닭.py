import sys
input = sys.stdin.readline

s, c = map(int, input().split())
array = [int(input()) for _ in range(s)]

# 1. left, right 설정
left, right = 1, max(array)
# 2.
while left <= right :
    # 2-1. mid 값 설정
    mid = (left + right) // 2
    # 2-2. 파의 개수 구하기
    count = 0
    for l in array :
        count += l // mid
    # 2-3. 파의 개수가 파닭의 수보다 많거나 같을 경우
    if count >= c : left = mid + 1
    # 2-4. 파의 개수가 파닭의 수보다 적은 경우
    else : right = mid - 1
# 3. 결과 출력
print( sum(array) - right * c)