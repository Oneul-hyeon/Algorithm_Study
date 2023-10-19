ans = int(1e9)
def solution(begin, target, words):
    # 1. 다른 알파벳 개수 체크 함수 정의
    def check(word1, word2) :
        cnt = 0
        # 1-1. 
        for i in range(l) :
            # 두 알파벳이 다를 경우 카운팅
            if word1[i] != word2[i] :
                cnt += 1
        # 1-2. 다른 알파벳 개수 반환
        return cnt
    # 2. DFS 함수 정의
    def dfs(now, cnt) :
        global ans
        # 2-1. 종료 조건 설정
        if now == target :
            ans = min(ans, cnt)
        # 2-2.
        for i in range(len(words)) :
            # 다음 단어로 변환한 적이 없고 다른 알파벳이 1개인 경우
            if not visited[i] and check(now, words[i]) == 1 :
                # 방문 처리
                visited[i] = True
                # DFS 실행
                dfs(words[i], cnt + 1)
                # 방문 해제
                visited[i] = False
    # 3. 변환할 수 없는 경우 0 출력
    if target not in words : return 0
    else :
        # 4. 단어 길이 변수 생성
        l = len(begin)
        # 5. 방문 여부 리스트 생성
        visited = [False for _ in range(len(words))]
        # 6. DFS 실행
        dfs(begin, 0)
        # 7. 결과 리턴
        return ans