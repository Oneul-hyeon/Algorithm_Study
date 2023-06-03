import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
#1. 변화량 리스트 생성
change = [0] * (n+1)
dp = [0] * (n+1)
#2. 리스트에 변화하는 지점 추가
for _ in range(m) :
    a, b, k = map(int, input().split())
    change[a-1] += k
    change[b] -= k
#3. dp에 인덱스 별 총 변화량 계산
dp[0] = change[0]
for i in range(1, n+1) :
    dp[i] = dp[i-1] + change[i]
#4. 결과 출력
print(*[array[i] + dp[i] for i in range(n)])