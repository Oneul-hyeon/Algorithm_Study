import sys
from collections import deque
input = sys.stdin.readline
def solution(n, d, k, c):
    # 1. 최댓값 변수 선언
    ans = 0
    # 2. 큐 생성
    queue = deque()
    array = list(int(input()) for _ in range(n))
    array.extend(array[:k-1])
    # 3.
    for num in array :
        # 3-1. 큐의 길이가 k개 미만일 경우
        if len(queue) < k :
            # 초밥 번호 삽입
            queue.append(num)
            # 큐의 길이가 k인 경우 최댓값 업데이트
            if len(queue) == k :
                ans = len(set(queue) | set([c]))
        # 3-2. 큐의 길이가 k개인 경우
        else :
            # 먹을 수 있는 초밥 업데이트
            queue.popleft()
            queue.append(num)
            # 최댓값 업데이트
            ans = max(ans, len(set(queue) | set([c])))
    # 4. 결과 출력
    print(ans)
    
if __name__ == "__main__" :
    n, d, k, c = map(int, input().split())
    solution(n, d, k, c)