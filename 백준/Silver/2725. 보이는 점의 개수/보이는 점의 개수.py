import sys, math
input = sys.stdin.readline

# 1. dp 생성
dp = [0] * 1001
# 2. 초기값 설정
dp[1] = 3
# 3.
for x in range(2, 1001) :
    # 3-1. 카운트 생성
    count = 0
    # 3-2.
    for y in range(1, x) :
        # 해당 인덱스의 최대 공약수가 1일 경우 카운트
        if math.gcd(x, y) == 1 : count += 1
    # 3-3. 점화식에 따라 처리
    dp[x] = dp[x-1] + 2 * count
# 4. 결과 출력
t = int(input())
for _ in range(t) :
    print(dp[int(input())])