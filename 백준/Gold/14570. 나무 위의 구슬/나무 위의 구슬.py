import sys
input = sys.stdin.readline

def solution(n, child, k) :
    # 1. 현재 노드 변수 설정
    now = 1
    # 2.
    while child[now] != [-1, -1] :
        # 2-1. 자식 노드가 1개일 경우
        if child[now].count(-1) == 1 :
            now = child[now][1] if child[now][0] == -1 else child[now][0]
        # 2-2. 자식 노드가 2개일 경우
        else :
            # 홀수 번째 구슬인 경우
            if k % 2 != 0 :
                now = child[now][0]
                k = k//2 + 1
            # 짝수 번째 구슬인 경우
            else :
                now = child[now][1]
                k //= 2
    # 3. 결과 출력
    print(now)
    
if __name__ == "__main__" :
    n = int(input())
    child =[[]]
    for _ in range(n) :
        child.append(list(map(int, input().split())))
    k = int(input())
    solution(n, child, k)