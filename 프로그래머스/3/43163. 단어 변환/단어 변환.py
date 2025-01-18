from collections import deque

def solution(begin, target, words):
    # 1. 단어 변환 체크 함수 정의
    def check(word1, word2) :
        # 1-1. 카운트 변수 생성
        cnt=0
        # 1-2. 서로 다른 문자 수 체크
        for idx in range(length) :
            if word1[idx] != word2[idx] : cnt += 1
        # 1-3. 서로 다른 문자 수가 1개일 경우 True, 이외의 경우 False return
        return True if cnt == 1 else False
    length=len(begin)
    # 2. 큐 생성 후 (begin, 0, 0) 삽입
    queue = deque([])
    queue.append((begin, 0, 0))
    # 3.
    while queue :
        # 3-1. 큐에서 값 반환
        now, visited, step = queue.popleft()
        # 3-2.
        for idx, next in enumerate(words) :
            # 3-2-1. 다음 단어로 변환한 적이 없으면서 다음 문자로 변환이 가능한 경우
            if not visited & (1 << idx) and check(now, next) :
                # 다음 문자가 target인 경우 단계 수 + 1 return
                if next == target : return step + 1
                # 이외의 경우 큐에 정보 삽입
                else :
                    visited |= (1 << idx)
                    queue.append((next, visited, step + 1))
    # 4. 0 return
    return 0