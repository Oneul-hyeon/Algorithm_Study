import sys, heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
array = sorted([list(map(int, input().split())) for _ in range(n)])

heap = []
for line in array :
    start, end = line[0], line[1]
    # 2. 첫 번째 end 값을 heap에 넣기
    if not heap : heapq.heappush(heap, end)
    else :
        # 2-1. heap의 최솟값이 start보다 작거나 같다면 pop
        if heap[0] <= start :
            heapq.heappop(heap)
        # 2-2 heap에 end값 push
        heapq.heappush(heap, end)
print(len(heap))