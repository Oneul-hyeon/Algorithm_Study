import sys
from typing import List
input = sys.stdin.readline

# 1. 프로세스 클래스 정의
class Processor:
    # 1-1. initialize 함수 생성
    def __init__(self, n):
        self.n = n
        # 1-1-1. 최소 거리 변수 초기화
        self.ans = float("inf")

    # 1-2. 플로이드-워셜 함수 생성
    def _floyd_warshall(self) -> List[List[int]]:
        # 1-2-1. 그래프 생성
        graph = [[float("inf") for _ in range(self.n+1)] for _ in range(self.n+1)]
        # 1-2-2.
        for a in range(self.n+1):
            # 그래프 내 간선 정보 입력
            for b, c in enumerate(list(map(int, input().split()))):
                graph[a][b] = c
        # 1-2-3. 점화식에 따라 플로이드-워셜 알고리즘 수행
        for a in range(self.n+1):
            for x in range(self.n+1):
                for b in range(self.n+1):
                    graph[a][b] = min(graph[a][b], graph[a][x]+graph[x][b])
        # 1-2-4. 노드 별 최단거리 그래프 반환
        return graph

    # 1-3. 백트래킹 함수 생성
    def _backtracking(self, now:int, dist:int):
        # 1-3-1. 모든 노드를 방문한 경우
        if self.visited.count(False) == 0:
            # 피자 가게로 돌아가는 거리를 포함한 전체 이동 거리 값이 최소 거리 값보다 작을 경우 최소 거리 값 업데이트
            self.ans = min(dist+self.graph[now][0], self.ans)
            return
        # 1-3-2.
        for next in range(1, self.n+1):
            # 현재 위치를 방문하지 않은 경우
            if not self.visited[next]:
                # 현재 위치 방문 처리
                self.visited[next] = True
                # 백트래킹 함수 실행
                self._backtracking(next, dist+self.graph[now][next])
                # 현재 위치 방문 해제
                self.visited[next] = False

    # 1-4. 실행 함수 생성
    def execute(self) -> int:
        # 1-4-1. 플로이드-워셜을 통한 노드 별 최단 거리 그래프 생성
        self.graph = self._floyd_warshall()
        # 1-4-2. 방문 여부 리스트 생성 후 현재 위치 방문 처리
        self.visited = [False for _ in range(self.n+1)]
        self.visited[0] = True
        # 1-4-3. 백트래킹 함수 실행
        self._backtracking(now=0, dist=0)
        # 1-4-4. 최소 거리 변수 반환
        return self.ans
# 2.
while N:=int(input()):
    # 2-1. 프로세스 실행
    print(Processor(N).execute())