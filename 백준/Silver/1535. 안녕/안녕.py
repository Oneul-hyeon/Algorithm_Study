import sys
input = sys.stdin.readline

def solution(n, stamina_consumed, happiness) :
    # 1. dp 생성
    dp = [0 for _ in range(100)]
    # 2.
    for i in range(1, n+1) :
        hp, h = stamina_consumed[i], happiness[i]
        for j in range(99, -1, -1) :
            # 2-1. 현재 체력이 잃는 체력보다 클 경우
            if j >= hp :
                dp[j] = max(dp[j], dp[j-hp] + h)
    # 3. 결과 출력
    print(dp[-1])

if __name__ == '__main__' :
    n = int(input())
    stamina_consumed = [[]] +list(map(int, input().split()))
    happiness = [[]] + list(map(int, input().split()))
    solution(n, stamina_consumed, happiness)