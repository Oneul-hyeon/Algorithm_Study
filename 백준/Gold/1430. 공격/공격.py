import sys
from collections import deque
input = sys.stdin.readline

def solution(n, r, d, x, y, information):
    # 1. 배수 변수 생성
    multiple = 0
    # 2. 방문 여부 비트 생성
    visited = 0
    # 3. 큐 생성
    queue = deque()
    # 4.
    for idx, info in enumerate(information) :
        nx, ny = info
        # 4-1. 적과의 사정 거리 안에 들 경우
        if r ** 2 >= (nx - x) ** 2 + (ny - y) ** 2 :
            # 큐에 좌표 삽입
            queue.append((nx, ny, 1))
            # 방문 처리
            visited |= ( 1 << idx )
            # 배수 업데이트
            multiple += 1
    # 5.
    while queue :
        # 5-1. 좌표 인덱스 반환
        a, b, m = queue.popleft()
        m /= 2
        # 5-2.
        for idx, info in enumerate(information) :
            nx, ny = info
            # 5-2-1. 방문한 적이 없으며 현재 탑과 에너지를 주고받을 수 있는 경우
            if not visited & ( 1 << idx ) and  r ** 2 >= (nx - a) ** 2 + (ny - b) ** 2 :
                # 배수 업데이트
                multiple += m
                # 방문 처리
                visited |= ( 1 << idx )
                # 큐에 다음 포탑 위치 삽입
                queue.append((nx, ny, m))
    # 6. 결과 출력
    print(round(d * multiple, 3))

if __name__ == "__main__" :
    n, r, d, x, y = map(int, input().split())
    information = [list(map(int, input().split())) for _ in range(n)]
    solution(n, r, d, x, y, information)