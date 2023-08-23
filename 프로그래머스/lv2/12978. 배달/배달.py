import sys
def solution(N, road, K):
    # 1. 플로이드-워셜을 위한 리스트 생성
    array = [[sys.maxsize] * (N+1) for _ in range(N+1)]
    # 2. 자신의 마을 내의 이동경로 처리
    for i in range(1, N+1) : array[i][i] = 0
    # 3. 
    for a, b, c in road :
        # 간선 정보 입력
        array[a][b] = min(array[a][b], c)
        array[b][a] = min(array[b][a], c)
    # 4. 플로이드-워셜 알고리즘
    for k in range(1, N+1) :
        for a in range(1, N+1) :
            for b in range(1, N+1) :
                if a != b :
                    array[a][b] = min(array[a][b], array[a][k] + array[k][b])
    # 5. 1번 마을에서 K시간 내로 배달이 가능한 마을 수 카운팅
    answer = 0
    for i in range(1, N+1) :
        if array[1][i] <= K : answer += 1
    # 6. 결과 리턴
    return answer