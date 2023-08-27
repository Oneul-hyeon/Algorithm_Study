from collections import defaultdict

def solution(tickets):
    global answer
    # 1. DFS 함수 선언
    def dfs(starting_point, route, count):
        global answer
        # 1-1. 종료 조건 설정
        if count == 0:
            # 출력 리스트에 route 삽입
            answer.append(route)
        # 1-2.
        for destination in airport[starting_point]:
            idx = airport[starting_point].index(destination)
            # 현재 공항에서 도착지 제거
            airport[starting_point].pop(idx)
            # dfs 실행
            dfs(destination, route + [destination], count - 1)
            # 현재 공항에 도착지 삽입
            airport[starting_point].insert(idx, destination)
    answer = []
    # 2. 모든 공항 정보 생성
    airports = list(set(sum(tickets, [])))
    # 3. 딕셔너리에 공항 정보를 key로, 빈 리스트를 value로 설정
    airport = defaultdict()
    for p in airports:
        airport[p] = []
    # 4.
    for s, d in tickets:
        # 딕셔너리의 출발지 인덱스에 도착지 삽입
        airport[s].append(d)
    # 5. DFS 실행
    dfs('ICN', ['ICN'], len(tickets))
    # 6. 결과 리턴
    return sorted(answer)[0]
    # 5. DFS 실행
    dfs('ICN', [], len(tickets))
    # 6. 결과 리턴
    return sorted(answer)[0]