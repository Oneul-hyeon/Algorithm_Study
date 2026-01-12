import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline



# 1.프로세서 클래스 정의
class Processor:
    # 1-1. 초기화 함수 정의
    def __init__(self, N, M):
        self.N = N
        self.M = M
        # 1-1-1. 원판 정보 입력
        self.plate = [[]] + [deque(list(map(int, input().split()))) for _ in range(N)]

    # 1-2. 원판 회전 함수 정의
    def _rotate(self, x:int, d:int, k:int) -> None:
        # 1-2-1.
        for idx in range(x, self.N+1, x):
            # 원판 회전
            for _ in range(k):
                if d == 0:
                    self.plate[idx].appendleft(self.plate[idx].pop())
                elif d == 1:
                    self.plate[idx].append(self.plate[idx].popleft())

    # 1-3. 인접 수 제거 함수 정의
    def _remove(self) -> bool:
        # 1-3-1. 서브 리스트 생성
        # print(self.plate)
        # sub_plate = [deepcopy(plate[:]) for plate in self.plate]
        sub_plate = deepcopy(self.plate)
        # 1-3-2. 플래그 변수 생성
        flag = False
        # 1-3-3.
        for x in range(1, N+1):
            for y in range(M):
                for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    # 인접 인덱스 추출
                    nx, ny = x+dir_x, (y+dir_y)%self.M
                    # 예외 처리
                    if nx <= 0 or nx > N or self.plate[nx][ny] is None: continue
                    # 현재 수와 같은 경우
                    if self.plate[x][y] == self.plate[nx][ny]:
                        # 제거 처리
                        if sub_plate[x][y] is not None: sub_plate[x][y] = None
                        if sub_plate[nx][ny] is not None: sub_plate[nx][ny] = None
                        # 플래그 처리
                        if not flag: flag = True
        # 1-3-4. 수가 처리된 경우
        if flag:
            # 원판 정보 업데이트
            # self.plate = [plate[:] for plate in sub_plate]
            self.plate = deepcopy(sub_plate)
            return False
        # 1-3-5. 수가 처리되지 않은 경우
        else:
            return True

    # 1-4. 원판 수 업데이트 함수 정의
    def _update(self):
        # 1-4-1. 원판 수 추출
        values = [num for plate in self.plate for num in plate if num is not None]
        # 1-4-2. 평균 값 산정
        if values:
            mean = sum(values) / len(values)
            # 1-4-3.
            for x in range(1, N+1):
                for y in range(M):
                    if self.plate[x][y] is None: continue
                    # 현재 인덱스 값이 평균보다 작은 경우 1 더하기
                    if self.plate[x][y] < mean:
                        self.plate[x][y] += 1
                    # 현재 인덱스 값이 평균보다 큰 경우 1 빼기
                    elif self.plate[x][y] > mean:
                        self.plate[x][y] -= 1

    # 1-5. 실행 함수 정의
    def execute(self, T:int):
        # 1-5-1.
        for i in range(T):
            # 원판 회전
            self._rotate(*list(map(int, input().split())))
            # 인접 수 제거가 되지 않은 경우
            if self._remove():
                # 원판 수 업데이트r
                self._update()

N, M, T = map(int, input().split())
# 2. 프로세서 오브젝트 생성
processor = Processor(N, M)
# 3. 프로세서 실행
processor.execute(T)
# 4. 결과 출력
print(sum([num for plate in processor.plate for num in plate if num is not None]))