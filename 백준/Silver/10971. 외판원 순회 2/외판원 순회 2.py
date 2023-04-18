import sys
input = sys.stdin.readline

n = int(input())

# 1. 비용 행렬 입력받기
array = [list(map(int, input().split())) for _ in range(n)]
min_cost = int(1e9)
cost = []

# 2. 재귀 함수 정의
def backtracking() :
    global min_cost
    # 2-1. 종료 조건 설정 : 리스트의 길이가 n인 경우
    if len(cost) == n :
        # 첫 번째 인덱스 값 append
        total_cost = 0
        for i in range(n-1) :
            if array[cost[i]][cost[i+1]] : total_cost += array[cost[i]][cost[i+1]]
            # 한 번이라도 0이 나올 경우 return
            else : return
        if array[cost[-1]][cost[0]] == 0 : return
        else : total_cost += array[cost[-1]][cost[0]]
        # 최솟값이면 저장
        if total_cost < min_cost: min_cost = total_cost
        return

    for i in range(n) :
        # 2-2. 리스트에 수가 겹치지 않도록 append
        if i not in cost:
            cost.append(i)
            # 2-3. 재귀 함수 실행
            backtracking()
            # 2-4. 리스트 마지막 값 빼기
            cost.pop()


# 3. 재귀함수 실행
backtracking()
print(min_cost)