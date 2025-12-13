import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(idx):
    global ans

    # 1-1. 종료 조건 설정
    # 1-1-1. 현재 인덱스가 가장 오른쪽인 경우
    if idx == N:
        # 깰 수 있는 계란의 최대 개수 업데이트
        ans = max(ans, len([egg for egg in durability if egg<=0]))
        return

    # 1-2. 현재 인덱스의 계란이 깨져있거나, 깰 계란이 없는 경우
    if durability[idx] <= 0 or not [egg for target, egg in enumerate(durability) if egg>0 and target!=idx]:
        # 1-2-1. 백트래킹 실행
        backtracking(idx+1)
    # 1-3. 이외의 경우
    else:
        # 1-3-1.
        for target in range(N):
            # 예외 처리
            if idx == target : continue
            # 고른 계란이 깨지지 않은 경우
            if durability[target] > 0:
                # 계란 깨기
                durability[idx] -= weight[target]
                durability[target] -= weight[idx]
                # 백트래킹 실행
                backtracking(idx+1)
                # 계란 복구
                durability[idx] += weight[target]
                durability[target] += weight[idx]

N = int(input())
ans = 0

# 2. 계란의 내구도, 무게 리스트 생성
durability, weight = [], []
for _ in range(N):
    S, W = map(int, input().split())
    durability.append(S)
    weight.append(W)
# 3. 백트래킹 실행
backtracking(0)
# 4. 결과 출력
print(ans)