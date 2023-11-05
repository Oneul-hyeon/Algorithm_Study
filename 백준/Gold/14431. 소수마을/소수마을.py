import sys
from math import sqrt
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

def solution(x1, y1, x2, y2, n) :
    # 1. 다익스트라 함수 생성
    def dijkstra(x, y) :
        # 1. 힙 생성 후 현재 (거리, 위치) 정보 입력
        heap = []
        heappush(heap, (0, x, y))
        # 2.
        while heap :
            # 2-1. 거리, 위치 인덱스 반환
            d, x, y = heappop(heap)
            # 2-2. 이미 처리된 경우 continue
            if distance[(x, y)] < d : continue
            # 2-3.
            for i, j in array :
                # 현재 노드와 다음 노드 간 거리 계산
                sub_d = int(sqrt((x - i) ** 2 + (y - j) ** 2))
                # 소수일 경우
                if check[sub_d] :
                    dist = d + sub_d
                    # 거리가 더 적을 경우
                    if dist < distance[(i, j)] :
                        # 거리 정보 업데이트
                        distance[(i, j)] = dist
                        # 힙에 정보 삽입
                        heappush(heap, (dist, i, j))

    # 2. 가능한 최대 길이 구하기
    max_len = int(sqrt(2 * (6000 ** 2))) + 1
    # 3. 소수 판별 리스트 생성
    check = [True for _ in range(max_len+1)]
    check[0], check[1] = False, False
    # 4. 에라토스테네스의 체
    for i in range(2, int(sqrt(max_len)) + 1) :
        if check[i] :
            for j in range(i+i, max_len+1, i) :
                if check[j] : check[j] = False
    # 5. 거리 정보 딕셔너리 생성
    distance = defaultdict(int)
    array = [(x2, y2)]
    # 6. 노드 정보 입력
    distance[(x1, y1)], distance[(x2, y2)] = 0, int(1e9)
    for _ in range(n) :
        x, y = map(int, input().split())
        distance[(x, y)] = int(1e9)
        array.append((x, y))
    # 7. 다익스트라
    dijkstra(x1, y1)
    # 8. 결과 출력
    print(-1) if distance[(x2, y2)] == int(1e9) else print(distance[(x2, y2)])

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    solution(x1, y1, x2, y2, n)