import sys
from collections import deque
from typing import List
input = sys.stdin.readline

# 1. 프로세서 클래스 생성
class Processor:
    # 1-1. initialize 함수 정의
    def __init__(self, graph):
        # 1-1-1. 방향 리스트 생성
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 1-1-2. 모눈종이 변수 생성
        self.graph = graph
        # 1-1-3. 시간 변수 생성
        self.time = 0
        # 1-1-4. 치즈 인덱스 생성
        self.cheeze = [(x, y) for x in range(N) for y in range(M) if graph[x][y]]

    # 1-2. 외부 공간 판별 함수 정의
    def _get_outer_space(self) -> List[List[bool]]:
        # 1-2-1. 큐 생성 후 (0, 0) 인덱스 삽입
        queue = deque([(0, 0)])
        # 1-2-2. 방문 여부 리스트 생성 후 (0, 0) 인덱스 방문 처리
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[0][0] = True
        # 1-2-3.
        while queue:
            # 큐에서 위치 인덱스 반환
            x, y = queue.popleft()
            for dir_x, dir_y in self.dirs:
                # 다음 위치 설정
                nx, ny = x+dir_x, y+dir_y
                # 예외 처리
                if nx<0 or nx>=N or ny<0 or ny>=M: continue
                # 다음 위치가 빈 공간이면서 방문하지 않은 경우
                if not self.graph[nx][ny] and not visited[nx][ny]:
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 다음 위치 삽입
                    queue.append((nx, ny))
        # 1-2-4. 방문 여부 리스트 반환
        return [row[:] for row in visited]

    # 1-3. 녹는 치즈 판별 함수 정의
    def _melting_cheese(self, outer_space:List[List[bool]]) -> None:
        # 1-3-1. 서브 치즈 인덱스 생성
        sub_cheeze = []
        # 1-3-2.
        for x, y in self.cheeze:
            # 카운트 변수 생성
            cnt = 0
            for dir_x, dir_y in self.dirs:
                # 다음 위치 설정
                nx, ny = x+dir_x, y+dir_y
                # 다음 위치가 빈 공간이면서 외부 공간인 경우 카운팅
                if not self.graph[nx][ny] and outer_space[nx][ny]:
                    cnt += 1
            # 카운팅이 2개 미만인 경우 녹지 않으므로 서브 치즈 인덱스에 삽입
            if cnt < 2:
                sub_cheeze.append((x, y))
            else:
                self.graph[x][y] = 0
        # 1-3-3. 치즈 인덱스 업데이트
        self.cheeze = sub_cheeze[:]

    # 1-4. 실행 함수 정의
    def execute(self):
        # 1-4-1.
        while self.cheeze:
            # 외부 공간 리스트 생성
            outer_space = self._get_outer_space()
            # 녹는 치즈 판별
            self._melting_cheese(outer_space)
            # 시간 업데이트
            self.time += 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 2. 프로세서 오브젝트 생성
processor = Processor(graph)
# 3. 프로세서 실생
processor.execute()
# 4. 결과 출력
print(processor.time)