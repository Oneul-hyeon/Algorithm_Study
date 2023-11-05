import sys
from collections import Counter
input = sys.stdin.readline

def solution(r, c, k, graph) :
    # 1. 현재 (r, c) 값이 k일 경우
    if r <= 3 and c <= 3 and graph[r-1][c-1] == k : print(0)
    else :
        # 2.
        for ans in range(1, 101) :
            # 2-1. R 연산이 가능한 경우
            if len(graph) >= len(graph[0]) :
                # 2-1-1.
                for i in range(len(graph)) :
                    line = graph[i]
                    # 카운팅
                    # 정렬
                    counter = sorted(Counter(line).items(), key = lambda x : [x[1], x[0]])
                    ins_array = []
                    for x, y in counter :
                        if x :
                            ins_array += [x, y]
                    # 결과값 삽입
                    graph[i] = ins_array
                # 2-1-2. 열의 최대 길이 구하기
                max_len = max([len(line) for line in graph])
                # 2-1-3. 제로 패딩
                for i in range(len(graph)) :
                    graph[i] += [0 for _ in range(max_len - len(graph[i]))]
                    if max_len > 100 :
                        graph[i] = graph[i][:100]
            # 2-2. C 연산이 가능한 경우
            elif len(graph) < len(graph[0]) :
                # 2-2-1. 행 / 열 뒤집은 배열 생성
                graph = list(zip(*graph))
                # 2-2-2.
                for i in range(len(graph)) :
                    line = graph[i]
                    # 카운팅
                    # 정렬
                    counter = sorted(Counter(line).items(), key=lambda x: [x[1], x[0]])
                    ins_array = []
                    for x, y in counter :
                        if x :
                            ins_array += [x, y]
                    # 결과값 삽입
                    graph[i] = ins_array
                # 2-2-2. 열의 최대 길이 구하기
                max_len = max([len(line) for line in graph])
                # 2-2-3. 제로 패딩
                for i in range(len(graph)) :
                    graph[i] += [0 for _ in range(max_len - len(graph[i]))]
                    if max_len > 100 :
                        graph[i] = graph[i][:100]

                # 2-3. 행/열 변경
                graph = list(zip(*graph))
            # 2-4. (r, c)에 k값이 있는 경우
            if r <= len(graph) and c <= len(graph[0]) and graph[r-1][c-1] == k :
                print(ans)
                break
        else : print(-1)

if __name__ == "__main__":
    r, c, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(3)]
    solution(r, c, k, graph)