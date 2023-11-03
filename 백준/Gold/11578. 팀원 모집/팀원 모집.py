import sys
from itertools import combinations
input = sys.stdin.readline

def solution(n, m, array) :
    summation = 0
    for i in range(1, n+1) :
        summation += 2**i
    # 1. 팀원 리스트 생성
    team = []
    # 2.
    for arr in array :
        # 2-1. 각 팀원이 풀 수 있는 문제 비트화하기
        temp = 0b0000000000
        for num in arr[1:] :
            temp |= (1<<num)
        team.append(temp)
    # 3.
    for k in range(1, m+1) :
        # 3-1. 팀원 조합 구하기
        combination = list(combinations(team, k))
        # 3-2.
        for comb in combination :
            temp = 0b0000000000
            for c in comb :
                temp |= c
            # 모든 문제를 풀 수 있을 경우 결과 출력
            if temp == summation :
                print(k)
                exit()
    # 4. -1 출력
    print(-1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(m)]
    solution(n, m, array)