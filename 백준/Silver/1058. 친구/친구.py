import sys
input = sys.stdin.readline

n = int(input())
# 1. 친구 관계 입력받기
graph = [list(input().rstrip()) for _ in range(n)]
# 2. 친구 여부 2차원 리스트 생성
result = [[0 for _ in range(n)] for _ in range(n)]
# 3. 플로이드 워셜 알고리즘 수행
for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            if a != b and not result[a][b] :
                if graph[a][b] == 'Y' or (graph[a][k] == 'Y' and graph[k][b] == 'Y') : result[a][b] = 1
# 4. 가장 유명한 사람의 2-친구 수 출력
print(max([sum(line) for line in result]))