import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. 팀원들의 능력치 정렬
array = sorted(list(map(int, input().split())))
# 2. left, right 설정
left, right = 0, n-1
ans = 0
# 3.
while left < right :
    # 4. 견학이 불가능한 경우
    if array[left] + array[right] < m : left += 1
    else :
        left += 1
        right -= 1
        ans += 1
# 6. 결과 출력
print(ans)