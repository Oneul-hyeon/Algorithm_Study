import sys
input = sys.stdin.readline

N, L = map(int, input().split())
info = sorted([list(map(int, input().split())) for _ in range(N)])

# 1. 널빤지 수, 널빤지 종료 지점 초기화
diff = info[0][1] - (start:=info[0][0])
cnt = diff//L if diff%L == 0 else diff//L + 1
end = start + L * cnt - 1
# 2.
for s, e in info[1:]:
    # 2-1. 현재 널빤지의 종료 지점이 새로운 웅덩이의 종료 지점보다 큰 경우
    if end > e:
        pass
    # 2-2. 현재 널빤지의 종료 지점이 새로운 웅덩이의 시작 지점보다 작은 경우
    elif end < s:
        # 2-2-1. 널빤지 수 업데이트
        _cnt = diff//L if (diff:=e-s)%L == 0 else diff//L + 1
        cnt += _cnt
        # 2-2-2. 널빤지 종료 지점 업데이트
        end = s + L * _cnt - 1
    # 2-3. 현재 널빤지의 종료 지점이 새로운 웅덩이의 시작 지점보다 큰 경우
    elif end >= s:
        # 2-3-1. 널빤지 수 업데이트
        _cnt = diff//L if (diff:=e-end-1)%L == 0 else diff//L + 1
        cnt += _cnt
        # 2-3-2. 널빤지 종료 지점 업데이트
        end = end+1 + L * _cnt - 1
# 3. 결과 출력
print(cnt)