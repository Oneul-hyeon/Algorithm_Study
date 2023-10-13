import sys
input = sys.stdin.readline

def solution(n, information) :
    # 1. 출력 리스트 생성
    ans = []
    # 2. 버스 노선 정보 정렬
    information.sort()
    # 3. 초기 s, e 세팅
    s, e, c = information[0]
    # 4.
    for i in range(1, n) :
        ns, ne, nc = information[i]
        # 4-1. 현재 도착 노선과 해당 인덱스의 출발점이 연결되지 않았을 경우
        if e < ns :
            # 출력 리스트에 정보 입력
            ans.append([s, e, c])
            # s, e 재정의
            s, e, c = ns, ne, nc
        # 4-2. 현재 도착 노선이 해당 인덱스의 출발점을 포함하는 경우
        else :
            # e, 비용 재설정
            e, c = max(e, ne), min(c, nc)
    # 5. 마지막 노선 정보 삽입
    ans.append([s, e, c])
    # 6. 결과 출력
    print(len(ans))
    for line in ans :
        print(*line)

if __name__ == '__main__' :
    n = int(input())
    information = [list(map(int, input().split())) for _ in range(n)]
    solution(n, information)