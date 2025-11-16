import sys
from typing import List, Any, Tuple
from collections import deque
input = sys.stdin.readline

# 1. 프로세스 클래스 정의
class Processor:
    # 1-1. initialize 함수 저으이
    def __init__(self, graph):
        # 1-1-1. 지도 딕셔너리 초기화
        self.graph:List[int, List[List[str]]] = {0: graph[:][:]}

    # 1-2. 위치 추출 함수 정의
    def _extract_index(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        # 1-2-1. 고슴도치, 비버 위치 초기화
        start, end = None, None
        # 1-2-2.
        for i in range(R):
            for j in range(C):
                # 해당 위치에 고슴도치가 있는 경우 위치 변수 업데이트
                if self.graph[0][i][j] == "S":
                    start = (i, j)
                # 해당 위치에 비버가 있는 경우 위치 변수 업데이트
                elif self.graph[0][i][j] == "D":
                    end = (i, j)
        # 1-2-3. 고슴도치, 비버 위치 반환
        return (start, end)

    # 1-3. 특정 시간 대 지도 생성 함수 정의
    def _generate_graph(self, time:int) -> List[List[str]]:
        # 1-3-1. 이전 시간의 지도 추출
        graph = [row[:] for row in self.graph[time-1]]
        # 1-3-2. 서브 지도 생성
        sub_graph = [row[:] for row in graph]
        # 1-3-3.
        for x in range(R):
            for y in range(C):
                # 해당 위치가 이전 시간에 물로 차 있던 경우
                if graph[x][y] == "*":
                    for dir_x, dir_y in dirs:
                        # 다음 위치 생성
                        nx, ny = x+dir_x, y+dir_y
                        # 예외 처리
                        if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
                        # 다음 위치가 빈 공간인 경우 서브 지도 업데이트
                        if sub_graph[nx][ny] == ".":
                            sub_graph[nx][ny] = "*"
        # 1-3-4. 서브 지도 반환
        return sub_graph[:][:]

    # 1-4. bfs 함수 정의
    def _bfs(self, start:Tuple[int, int], end:Tuple[int, int]) -> Any:
        # 1-4-1. 큐 생성 후 현재 위치 및 시간 정보 삽입
        queue = deque([(*start, 0)])
        # 1-4-2. 방문 여부 리스트 생성 후 현재 위치 방문 처리
        visited = [[False for _ in range(C)] for _ in range(R)]
        visited[start[0]][start[1]] = True
        # 1-4-3.
        while queue:
            # 큐에서 위치 및 시간 정보 반환
            x, y, t = queue.popleft()
            for dir_x, dir_y in dirs:
                # 다음 위치 생성
                nx, ny = x+dir_x, y+dir_y
                # 다음 시간에 해당하는 지도가 없는 경우 지도 생성
                if (next_time:=t+1) not in self.graph:
                    self.graph[next_time] = self._generate_graph(next_time)
                # 다음 시간에 해당하는 지도 추출
                next_graph = self.graph[next_time]
                # 예외 처리
                if ((nx < 0 or nx >= R or ny < 0 or ny >= C)
                    or next_graph[nx][ny] == "X") : continue
                # 다음 위치가 도착점인 경우
                if (nx, ny) == end:
                    # print(self.graph)
                    # 최소 시간 반환
                    return next_time
                # 방문하지 않았으면서 이동이 가능한 경우
                if not visited[nx][ny] and next_graph[nx][ny] == ".":
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 다음 위치 및 시간 정보 삽입
                    queue.append((nx, ny, next_time))

        # 1-4-4. 비버의 굴로 이동할 수 없으므로, KAKTUS 반환
        return "KAKTUS"

    # 1-5. 실행 함수 정의
    def execute(self) -> Any:
        # 1-5-1. 고슴도치, 비버 위치 추출
        start, end = self._extract_index()
        # 1-5-2. 최소 시간 반환
        return self._bfs(start, end)


R, C = map(int, input().split())
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 2. 지도 입력
graph = [list(input().strip()) for _ in range(R)]
# 3. 최소 시간 출력
print(Processor(graph).execute())