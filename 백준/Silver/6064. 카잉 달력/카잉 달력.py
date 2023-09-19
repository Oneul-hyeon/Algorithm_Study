import sys
input = sys.stdin.readline

def solution(N, M, x, y) :
    # 1. N, M 크기 비교 후 업데이트
    if N < M :  N, M, x, y = M, N, y, x
    # 2.
    for k in range(x, N * M + 1, N) :
        # 2-1. k-y가 M의 배수일 경우 k 리턴
        if (k - y) % M == 0 : return k
    # 3. -1 리턴
    return -1

if __name__ == '__main__' :
    k = int(input())
    for _ in range(k) :
        N, M, x, y = map(int, input().split())
        print(solution(N, M, x, y))