import sys
from collections import deque
input = sys.stdin.readline

# 1. BFS 함수 정의
def bfs(array) :
    # 1-1. 부모 정보 리스트 생성
    node = [0 for _ in range(n+1)]
    node[1] = 1
    # 1-2. 큐에 루트 노드 삽입
    queue = deque()
    queue.append(1)
    # 1-3.
    while queue :
        # 인덱스 반환
        parent = queue.popleft()
        for child in array[parent] :
            # 노드에 부모 정보가 입력되지 않은 경우
            if not node[child] :
                # 부모 정보 입력
                node[child] = parent
                # 큐에 다음 노드 삽입
                queue.append(child)
    # 1-4. 부모 정보 리스트 반환
    return node

def solution(n, information) :
    array = [[] for _ in range(n+1)]
    # 2. 간선 정보 입력
    for a, b in information :
        array[a].append(b)
        array[b].append(a)
    # 3. BFS 실행
    node = bfs(array)
    # 4. 결과 출력
    for i in range(2, n+1) :
        print(node[i])

if __name__ == '__main__' :
    n = int(input())
    information = [list(map(int, input().split())) for _ in range(n-1)]
    solution(n, information)