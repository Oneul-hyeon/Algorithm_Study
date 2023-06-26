import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

ans = 0
minus = sorted([num for num in array if num < 0])
plus = sorted([num for num in array if num > 0], reverse = True)

try :not_return = minus[0] if abs(minus[0]) > plus[0] else plus[0]
except : not_return = minus[0] if not plus else plus[0]

# 음수 처리
for i in range(0, len(minus), m) :
    # 돌아가지 않는 경우 체크
    if minus[i] == not_return : continue
    # 이외의 경우 체크
    ans += 2 * abs(minus[i])

# 양수 처리
for i in range(0, len(plus), m) :
    # 돌아가지 않는 경우 체크
    if plus[i] == not_return : continue
    # 이외의 경우 체크
    ans += 2  * plus[i]

# 돌아가지 않는 경우 처리
ans += abs(not_return)

# 결과 출력
print(ans)
