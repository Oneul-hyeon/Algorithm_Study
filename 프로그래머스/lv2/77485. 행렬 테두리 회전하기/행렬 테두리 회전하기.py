def solution(rows, columns, queries):
    
    # 1. 테두리 회전 재귀 함수 선언 :
    def rotate(x1, y1, x2, y2) :
        min_num = int(1e9)
        # 1-1. 각 모서리 함수 별도 저장
        left_top = graph[x1][y1]
        right_top = graph[x1][y2]
        left_bottom = graph[x2][y1]
        right_bottom = graph[x2][y2]
        # 1-2. 테두리 위쪽 회전
        for j in range(y2, y1, -1) :
            graph[x1][j] = graph[x1][j-1]
            min_num = min(min_num, graph[x1][j])
        # 1-3. 테두리 오른쪽 회전
        for i in range(x2, x1, -1) :
            graph[i][y2] = graph[i-1][y2]
            min_num = min(min_num, graph[i][y2])
        # 1-4. 테두리 아래쪽 회전
        for j in range(y1, y2) :
            graph[x2][j] = graph[x2][j+1]
            min_num = min(min_num, graph[x2][j])
        # 1-5. 테두리 왼쪽 회전
        for i in range(x1, x2) :
            graph[i][y1] = graph[i+1][y1]
            min_num = min(min_num, graph[i][y1])
        # 1-6. 예외 인덱스 처리
        graph[x1][y1+1] = left_top
        graph[x1+1][y2] = right_top
        graph[x2-1][y1] = left_bottom
        graph[x2][y2-1] = right_bottom
        # 1-7. 가장 작은 수 처리
        min_num = min(min_num, left_top, right_top, left_bottom, right_bottom)
        return min_num
        
    answer = []
    # 2. graph 생성
    graph = [[0] * columns for _ in range(rows)]
    idx = 1
    for i in range(rows) :
        for j in range(columns) :
            graph[i][j] = idx
            idx += 1
    # 3.
    for x1, y1, x2, y2 in queries :
        # 테두리 회전
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1))
    # 4. 결과 출력
    return answer