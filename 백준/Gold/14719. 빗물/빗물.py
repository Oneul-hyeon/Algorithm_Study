import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

# 1. 빗물의 총량 변수 생성
ans = 0
# 2.
for idx, height in enumerate(blocks):
    # 2-1. 예외 처리
    if idx == 0 or idx == w-1 : continue
    # 2-2. 물이 고일 수 있는 가능 높이 선정
    possible_height = min(max(blocks[:idx]), max(blocks[idx+1:]))
    # 2-3. 가능 높이가 현재 열의 높이보다 높을 경우
    if (mod:=possible_height-height) > 0 :
        # 빗물의 총량 업데이트
        ans += mod
# 3. 결과 출력
print(ans)