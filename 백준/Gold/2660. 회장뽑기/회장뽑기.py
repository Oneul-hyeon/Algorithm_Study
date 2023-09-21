import sys
input = sys.stdin.readline

def solution(n, information) :
    # 1. 플로이드-워셜을 위한 배열 생성
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    # 2. 회원 정보 입력받기
    for a, b in information :
        graph[a][b] = 1
        graph[b][a] = 1
    # 3. 플로이드-워셜
    for k in range(1, n+1) :
        for a in range(1, n+1) :
            for b in range(1, n+1) :
                if a != b :
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    # 4. 회원별 점수 구하기
    score = [max(graph[i][1:i] + graph[i][i+1:]) for i in range(n+1)]
    # 5. 결과 출력
    candidate = [i for i in range(1, n+1) if i != 0 and score[i] == min(score[1:])]
    print(min(score[1:]), len(candidate))
    print(*candidate)

if __name__ == '__main__' :
    n = int(input())
    information = []
    while True :
        info = list(map(int, input().split()))
        if info != [-1, -1] :
            information.append(info)
        else :
            break
    solution(n, information)