import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution(n, m, k, information):
    # 1. 도수를 기준으로 오름차순 정렬
    information.sort(key = lambda x : x[1])
    # 2. 힙 리스트, 선호도 합 변수 생성
    heap, summation = [], 0
    # 3.
    for v, c in information :
        # 3-1. 힙 리스트의 길이가 n보다 작을 경우
        if len(heap) < n :
            # 힙 리스트에 정보 삽입
            heappush(heap, [v, c])
            # 선호도 합 업데이트
            summation += v
        # 3-2. 힙 리스트의 길이가 n과 같을 경우
        if len(heap) == n :
            # 선호도가 기준보다 낮을 경우
            if summation < m :
                summation -= heappop(heap)[0]
            # 선호도가 기준보다 같거나 높을 경우
            else :
                print(max(list(zip(*heap))[1]))
                exit()
    # 4. -1 출력
    print(-1)
if __name__ == "__main__" :
    n, m, k = map(int, input().split())
    information = [list(map(int, input().split())) for _ in range(k)]
    solution(n, m, k, information)