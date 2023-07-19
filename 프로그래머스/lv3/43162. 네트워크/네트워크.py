from collections import deque

def solution(n, computers):
    answer = 0
    def bfs(x, y) :
        queue = deque()
        queue.append((x, y))
        while queue :
            x, y = queue.popleft()
            visited[x][y] = True
            for ny in range(n) :
                if computers[x][ny] and ny != y and not visited[x][ny] :
                    visited[x][ny] = True
                    queue.append((ny, x))

        return 1

    ans = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] and not visited[i][j] :
                answer += bfs(i, j)
    return answer