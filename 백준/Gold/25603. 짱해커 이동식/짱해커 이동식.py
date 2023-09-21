import sys
input = sys.stdin.readline

# 1. 주어진 범위 내 최솟값 인덱스 반환 함수 정의
def return_idx(idx) :
    cost = float('inf')
    # 1-1.
    for i in range(idx+k, idx, -1) :
        # 더 작은 비용 값을 가지는 경우
        if costs[i] < cost :
            # 인덱스, 비용 업데이트
            new_idx = i
            cost = costs[i]
    # 1-2. 업데이트 된 인덱스와 비용 반환
    return new_idx, cost
def solution(n, k, costs) :
    # 2. 초기 범위 내 최솟값을 갖는 인덱스와 비용 설정 
    idx = costs[:k].index(min(costs[:k]))
    answer = costs[idx]
    # 3.
    while idx + k < n :
        # 3-1. 최솟값 인덱스 반환 함수 실행
        idx, cost = return_idx(idx)
        # 3-2. 최댓값 업데이트
        answer = max(answer, cost)
    # 4. 결과 출력
    print(answer)
if __name__ == '__main__' :
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    solution(n, k, costs)