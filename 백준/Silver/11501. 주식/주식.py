import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    array = list(map(int, input().split()))
    ans = 0
    max_num = 0
    # 1.
    for i in range(n-1, -1, -1) :
        # 1-1. 해당 인덱스 값이 더 클 경우 최댓값 초기화
        if max_num < array[i] : max_num = array[i]
        # 1-2. 이외의 경우 이익 더하기
        else :
            ans += max_num - array[i]
    # 2. 결과 출력
    print(ans)