import sys
from collections import deque
input = sys.stdin.readline

# 1. 소수 판별 함수 정의
def check() :
    global number

    number[0], number[1] = False, False
    # 1-1.
    for i in range(2, 1_000_001) :
        # 해당 수가 소수일 경우
        if number[i] :
            for k in range(i*2, 1_000_001, i) :
                # 소수 여부 처리
                number[k] = False
# 2. bfs 함수 정의
def bfs(now) :
    # 2-1. 큐에 (현재 위치, 0) 삽입
    queue = deque()
    queue.append((now, 0))
    # 2-2. 방문 여부 리스트 생성 후 현재 위치 방문 처리
    visited = [False] * 1_000_001
    visited[n] = True
    # 2-3.
    while queue :
        # (위치, 핑거 스냅 횟수) 반환
        now, count = queue.popleft()
        #
        for next in [now // 2, now // 3, now + 1, now - 1] :
            # 예외 처리
            if next <= 0 or next > 1_000_000 : continue
            # 종료 조건
            if next in array : return count + 1 # 핑거 스냅 횟수 + 1 반환
            # 해당 위치에 방문하지 않은 경우
            if not visited[next] :
                # 방문 처리
                visited[next] = True
                # 큐에 (다음 위치, 핑거 스냅 횟수 + 1) 삽입
                queue.append((next, count + 1))

number = [True] * 1_000_001
# 3. 소수 판별 함수 실행
check()
t = int(input())
for _ in range(t) :
    n, a, b = map(int, input().split())
    # 4. 목표 범위 안의 소수 리스트 생성
    array = [i for i in range(a, b+1) if number[i]]
    # 5. 목표 범위 안에 소수가 없는 경우
    if not array : ans = -1
    # 6. 현재 생명체 수가 목표 범위 안에 드는 경우
    elif n in array : ans = 0
    # 7. 이외의 경우
    else :
        # bfs 실행
        ans = bfs(n)
    # 8. 결과 출력
    print(ans)