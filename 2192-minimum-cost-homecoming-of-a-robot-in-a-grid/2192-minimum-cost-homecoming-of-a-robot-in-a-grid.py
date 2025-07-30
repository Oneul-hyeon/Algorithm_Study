class Solution:
    # 1. 정답 함수 정의
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        x, y = startPos
        fx, fy = homePos

        # 1-1. 비용 변수 정의
        cost = 0
        # 1-2. 행 간 이동 시 비용 업데이트
        cost += sum(rowCosts[x+1:fx+1]) if x < fx else sum(rowCosts[fx:x])
        # 1-3. 열 간 이동 시 비용 업데이트
        cost += sum(colCosts[y+1:fy+1]) if y < fy else sum(colCosts[fy:y])
        # 1-4. 총 비용 반환
        return cost