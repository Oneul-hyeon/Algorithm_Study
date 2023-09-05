import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    array = sorted(list(map(int, input().split())))
    # 1. 한 개 차이 중 최솟값 계산
    answer = min( array[1] - array[0], array[-1] - array[-2])
    # 2. 두 개 차이 중 최댓값 계산
    for i in range(2, n) :
        answer = max(answer, array[i] - array[i-2])
    # 3. 결과 출력
    print(answer)