class Solution:
    def __init__(self) -> None:
        self.INF = float("inf")

    # 1. 정답 함수 정의    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1-1. DP 리스트 생성
        dp = [self.INF] * (amount+1)
        # 1-2. 초기값 설정
        dp[0] = 0
        # 1-3.
        for coin in sorted(coins, reverse=True):
            for i in range(coin, amount+1):
                # 1-3-1. 점화식을 활용해 최솟값 업데이트
                dp[i] = min(dp[i], dp[i-coin]+1)
        # 1-4. 결과 리턴
        return dp[amount] if dp[amount] != self.INF else -1