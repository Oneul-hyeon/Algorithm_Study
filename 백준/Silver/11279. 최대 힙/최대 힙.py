import sys
import heapq
input = sys.stdin.readline
test_case = int(input())

heap = []
for i in range(test_case):
    x = int(input())
    if x > 0 : heapq.heappush(heap, -x)
    elif x == 0 :
        if len(heap) == 0 : print(0)
        else :
            print(-heapq.heappop(heap))
