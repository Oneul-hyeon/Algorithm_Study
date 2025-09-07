import sys
input = sys.stdin.readline

# 1. 설치 공유기 수 산정 함수 정의
def calculate(distance):
    # 1-1. 0번 인덱스 좌표를 기준점으로 설정
    point = array[0]
    # 1-2.
    cnt = 1
    for target in array[1:]:
        # 1-2-1. 현재 좌표와 기준 좌표와의 거리가 설정한 거리를 초과하는 경우
        if target-point > distance:
            # 공유기 수 카운트
            cnt += 1
            # 기준 좌표 업데이트
            point = target
    # 1-3. 산정된 공유기 수 반환
    return cnt

N, C = map(int, input().split())
array = sorted([int(input()) for _ in range(N)])

# 2. 초기 left, right 값 설정
left, right = 0, array[-1]
# 3.
while left <= right:
    # 3-1. 중간값 설정
    mid = (left+right)//2
    # 3-2. 설치 공유기 수 산정
    # 3-3. 설치되어야 하는 공유기가 C개보다 같거나 많은 경우 start 값 조정
    if calculate(mid) >= C: left = mid+1
    # 3-4. 설치되어야 하는 공유기가 C개보다 적은 경우 end 값 조정
    else : right = mid-1

# 4. 결과 출력
print(left)