import sys
input = sys.stdin.readline


# 1. 솔루션 함수 정의
def solution(X: int, Y: int, D: int, T: int) -> float:
    # 1-1. 전체 거리 계산(10번 째에서 반올림)
    distance = round((X**2 + Y**2) ** 0.5, 10)
    # 1-2. 전체 거리를 D로 나눈 나머지가 없는 경우
    if distance % D == 0:
        # 1-2-1. 전체를 걷는 시간과 전체를 점프하는 시간의 최솟값 반환
        return min(distance, distance // D * T)
    # 1-3. 1회 점프 거리가 전체 거리보다 큰 경우
    elif D > distance:
        # 1-3-1. 전체를 걷거나, 점프를 1번만 하거나, 점프를 2번 하는 경우의 최솟값 반환
        return min(distance, T + (D - distance), 2 * T)
    # 1-4. 1회 점프 거리가 전체 거리보다 큰 경우
    else:
        # 1-4-1. 점프를 최대한 많이 한 경우의 시간이 걷는 시간보다 더 적은 경우
        # 점프하는 경우 소요 시간 산정
        if (jump_time := distance // D * T) < (jump_distance := distance // D * D):
            # 잔여 거리를 점프하는 경우와 걷는 경우 소요 시간을 산정하여 업데이트된 최솟값 반환
            return jump_time + min(T, distance - jump_distance)
        # 1-4-2. 점프를 최대한 많이 한 경우의 시간이 걷는 시간보다 더 많은 경우
        else:
            # 전체 걷는 시간 반환
            return distance


# 2. 솔루션 함수 실행
print(solution(*list(map(int, input().split()))))