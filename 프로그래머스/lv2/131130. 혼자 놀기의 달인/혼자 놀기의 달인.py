def solution(cards):
    n = len(cards)
    cards = [0] + cards
    # 1. 출력 리스트 설정
    answer = []
    # 2. 방문 여부 리스트 생성
    visited = [False] * (n+1)
    # 3. 
    for i in range(1, n+1) :
        # 3-1. 방문하지 않은 인덱스일 경우
        if not visited[i] :
            idx = i
            cnt = 0
            while not visited[idx] :
                # 방문 처리
                visited[idx] = True
                # 카운팅
                cnt += 1
                # 인덱스 재정의
                idx = cards[idx]
            # 출력 리스트에 카운트 삽입
            answer.append(cnt)
    # 4. 출력 리스트의 첫 인덱스에 모든 카드를 카운팅한 경우
    if answer[0] == n : return 0
    # 5. 최고 점수 출력
    answer.sort(reverse = True)
    return answer[0] * answer[1]