import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
# 1. 위치 리스트 생성
position = [0 for _ in range(1_000_001)]
# 2.
for i in array :
    # 2-1. 현재 위치에 화살이 있을 경우
    if position[i] :
        # 2-1-1. 현재 위치의 화살 감소
        position[i] -= 1
    # 2-2. 화살 다음 위치로 이동
    position[i-1] += 1
# 3. 결과 출력
print(sum(position))