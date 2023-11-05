import sys
input = sys.stdin.readline

def solution(n, c, m, information) :
    # 1. 현재 실린 짐의 목표 지점 딕셔너리 생성
    target = {i : 0 for i in range(1, n+1)}
    # 2. 박스 정보 정렬
    information.sort(key = lambda x : [x[1], x[0]])
    ans =  0
    # 3.
    for s, e, a in information :
        volume = 0
        # 3-1. 출발지에서 실을 수 있는 박스 수 계산
        for i in range(1, s+1) : volume += target[i]
        for i in range(s, e+1) :
            if target[i] > 0 : volume += target[i]
        # 3-2. 실을 수 없는 경우 continue
        if volume >= c : continue
        # 3-3. 딕셔너리에 정보 저장
        if a > c - volume : a = c - volume
        target[s] += a
        target[e] -= a
        # 3-4. 출력 리스트에 값 더하기
        ans += a
    # 4. 결과 출력
    print(ans)

if __name__ == "__main__":
    n, c = map(int, input().split())
    m = int(input())
    information = [list(map(int, input().split())) for _ in range(m)]
    solution(n, c, m, information)