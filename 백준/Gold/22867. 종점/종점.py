import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution(n, bus_schedule) :
    # 1. 밀리 초 변환 함수 정의
    def convert(time) :
        # 1-1. 시, 분, 초를 밀리초 값으로 변환
        t = 0
        time = time.replace('.', ':')
        for x, y in zip(map(int, time.split(':')), [3600000, 60000, 1000, 1]) :
            t += x * y
        return t
    # 2. 버스 시간표 정렬
    bus_schedule.sort()
    # 3. 힙 생성
    heap = []
    # 4.
    for IN, OUT in bus_schedule :
        # 4-1. 버스의 진입 시가느 진출 시간을 밀리 초로 변환
        IN, OUT = convert(IN), convert(OUT)
        # 4-2. 버스의 진입 시간이 최소 힙의 진출 시간보다 늦을 경우
        if not heap or IN < heap[0] :
            # 힙에 다음 버스의 진출 시간 삽입
            heappush(heap, OUT)
        # 4-3. 버스의 진입 시간이 최소 힙의 진출 시간보다 같거나 빠를 경우
        else :
            # 힙에서 최솟값 제거
            heappop(heap)
            # 힙에 다음 버스의 진출 시간 삽입
            heappush(heap, OUT)
    # 5. 힙의 길이 출력
    print(len(heap))

if __name__ == "__main__" :
    n = int(input())
    bus_schedule = [list(map(str, input().rstrip().split())) for _ in range(n)]
    solution(n, bus_schedule)