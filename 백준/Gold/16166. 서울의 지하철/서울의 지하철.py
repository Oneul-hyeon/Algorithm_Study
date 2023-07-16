import sys, math
input = sys.stdin.readline

def dfs(sub, station, count) :
    global min_count

    if destination in subway[sub] :
        min_count = min(min_count, count)
        return
    if count >= min_count : return
    if False not in visited : return

    for next in subway[sub] :
        for i in range(1, n+1) :
            if i != station and next in subway[i] and not visited[i]:
                visited[i] = True
                dfs(i, next, count+1)
                visited[i] = False

n = int(input())
subway = [0] * (n+1)
starting_point = []
min_count = math.inf

for i in range(1, n+1) :
    subway_num = list(map(int, input().split()))[1:]
    if 0 in subway_num : starting_point.append(i)
    subway[i] = subway_num if i != 0 else list(set(subway_num))

destination = int(input())
for i in starting_point :
    visited = [False] * (n+1)
    dfs(i, 0, 0)

print(min_count) if min_count != math.inf else print(-1)