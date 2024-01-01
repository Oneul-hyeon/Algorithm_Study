import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def solution():
    # 1. 배열 -> 비트 변환 함수 정의
    def array2bit(array):
        # 1-1. 비트 생성
        bit = 0
        # 1-2.
        for i in range(4):
            for j in range(4):
                # 1-2-1. 해당 인덱스 값이 'L'일 경우 비트 삽입
                if array[i][j] == 'L':
                    bit |= (1 << 4 * i + j)
        # 1-3. 비트 반환
        return bit

    # 2. bfs 함수 정의
    def bfs(start):
        def check(bit, idx1, idx2, cnt):
            bit ^= (1 << idx1)
            bit ^= (1 << idx2)

            # 타켓과 같을 경우 자리 바꿈 횟수 + 1 반환
            if bit == target:
                print(cnt+1)
                exit()
            else:
                # 방문하지 않은 경우
                if not visited[bit]:
                    # 방문 처리
                    visited[bit] = True
                    queue.append((bit, cnt + 1))

        # 2-1. 큐에 (현재 배치 비트, 0) 삽입
        queue = deque()
        queue.append((start, 0))
        # 2-2. 방문 여부 딕셔너리 생성 후 방문 처리
        visited = defaultdict(bool)
        visited[start] = True
        # 2-3.
        while queue:
            # 2-3-1. 큐에서 (현재 배치 비트, 자리 바꿈 횟수) 반환
            now, cnt = queue.popleft()
            # 2-3-2.
            for i in range(4):
                for j in range(4):
                    # 타겟과 다를 경우
                    idx = 4 * i + j
                    # 열변환
                    # 현재 인덱스의 좌우가 다른 문자일 경우 비트 변환
                    r = idx + 1
                    if r < 4 * (i + 1) and (now & (1 << idx) != now & (1 << r)):
                        check(now, idx, r, cnt)
                    # 행 변환
                    d = idx + 4
                    if d <= 16 and (now & (1 << idx) != now & (1 << d)):
                        check(now, idx, d, cnt)

    now = [list(input().rstrip()) for _ in range(4)]
    target = []
    while True:
        line = input().rstrip()
        if line:
            target.append(list(line))
            target.extend(list(input().rstrip()) for _ in range(3))
            break
    # 3. 현재 배치와 타겟 배치를 비트로 변환
    now = array2bit(now)
    target = array2bit(target)
    # 4. bfs 결과 출력
    print(bfs(now) if now != target else 0)

if __name__ == "__main__":
    solution()