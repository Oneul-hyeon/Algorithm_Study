import sys
from collections import deque
#도시의 개수 n, 도로의 개수 m, 거리정보 k, 출발 도시의 번호x
#--> 최단 거리가 k인 도시 찾기

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
queue = deque()
min_distance = [-1] * (n+1)
min_distance[x] = 0

queue.append(x)
while queue:
    now = queue.popleft()
    for next in graph[now] :
        if min_distance[next] == -1:
            min_distance[next] = min_distance[now] + 1
            queue.append(next)
check = False
for i in range(len(min_distance)):
    if min_distance[i] == k :
        print(i)
        check = True
if not check : print(-1)