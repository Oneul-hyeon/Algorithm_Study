import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(x, y, cnt):
    global ans, checked

    # 1-1. 최대 칸 수 업데이트
    ans = max(ans, cnt)
    # 1-2.
    for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        # 1-2-1. 다음 위치 설정
        nx, ny = x+dir_x, y+dir_y
        # 1-2-2. 예외 처리
        if nx<0 or nx>=R or ny<0 or ny>=C: continue
        # 1-2-3. 다음 위치에 방문하지 않았으면서, 해당 알파벳을 사용하지 않는 경우
        if not checked & (1 << (index:=ord(graph[nx][ny])-standard)) and not visited[nx][ny]:
            # 방문 처리
            visited[nx][ny] = True
            # 알파벳 사용 처리
            checked |= (1<<index)
            # 백트래킹 실행
            backtracking(nx, ny, cnt+1)
            # 방문 해제
            visited[nx][ny] = False
            # 알파벳 사용 해제
            checked &= ~(1<<index)

R, C = map(int,input().split())
graph = [list(input().strip()) for _ in range(R)]

# 2. 방문 여부 리스트 생성
visited = [[False for _ in range(C)] for _ in range(R)]
# 3. 알파벳 사용 여부 변수 생성
checked = 0
# 4. 정답 변수 생성
ans = 0
# 5. 백트래킹 실행
standard = ord("A")
visited[0][0] = True
checked |= (1<<ord(graph[0][0])-standard)
backtracking(0, 0, 1)
# 6. 정답 출력
print(ans)
