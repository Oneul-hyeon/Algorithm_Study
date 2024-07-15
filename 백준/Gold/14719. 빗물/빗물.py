import sys
input = sys.stdin.readline

_, w = map(int, input().split())
array = list(map(int, input().split()))

# 1. 출력 변수 생성
ans = 0
# 2,
for idx, height in enumerate(array) :
    if idx == 0 or idx == len(array) - 1 : continue
    # 2-1. 해당 인덱스에 차오를 물의 높이 구하기
    min_height = min(max(array[:idx]), max(array[idx+1:]))
    # 2-2. 해당 높이가 현재 높이보다 높을 경우 출력 변수 업데이트
    if (mod := min_height - height) > 0 : ans += mod
# 3. 결과 출력
print(ans)