import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 지나갈 수 있는 길인지 여부 체크 함수 선언
def check(road) :
    # 1-1. 초기 높이 설정
    h = road[0]
    # 1-2. 경사로 설치 리스트 생성
    install = [False] * n
    # 1-3.
    idx = 1
    while idx < n :
        # 1-3-1. 높이가 같은 경우
        if h == road[idx] : idx += 1
        # 1-3-2. 높이가 다를 경우
        else :
            # 높이 차이가 1보다 높은 경우
            if abs(h - road[idx]) > 1 : return False
            # 이외의 경우
            else :
                # 올라가는 경사로를 설치해야 하는 경우
                if h < road[idx] :
                    # 높이가 다르거나 해당 위치에 이미 경사로가 설치된 경우
                    if idx + 1 - l < 0 or len(set(road[idx-l:idx])) != 1 or len(set(install[idx-l:idx+1])) != 1:
                        return False
                    else :
                        h = road[idx]
                # 내려가는 경사로를 설치해야 하는 경우
                else :
                    # 높이가 다를 경우
                    if len(set(road[idx:idx+l])) != 1 or idx + l - 1 >= n : return False
                    else :
                        for i in range(idx, idx+l) :
                            install[i] = True
                        h = road[idx]
                        idx += l
    return True

ans = 0
# 2. 행 체크
for line in graph :
    if check(line) :
        ans += 1
# 3. 열 체크
graph_col = list(zip(*graph))
for line in graph_col :
    if check(line) :
        ans += 1
# 4. 결과 출력
print(ans)