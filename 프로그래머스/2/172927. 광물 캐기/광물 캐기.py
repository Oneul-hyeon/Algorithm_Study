def solution(picks, minerals) :
    # 1. 백트래킹 함수 정의
    def backtracking(pick, now, idx) :
        nonlocal answer
        
        # 1-1. 종료 조건 설정
        if pick.count(0) == 3 :
            # 최소 피로도 업데이트
            answer = min(answer, now)
            return
        # 1-2. 곡괭이 선택
        for i in range(3) :
            # 1-2-1. 이미 해당 곡괭이를 다 썼을 경우 continue
            if pick[i] == 0 : continue
            next_idx, next = idx, now
            # 1-2-2.
            for _ in range(5) :
                next_idx += 1
                # 모든 광물을 다 캔 경우
                if next_idx == l :
                    # 최소 피로도 업데이트
                    answer = min(answer, next)
                    break
                # 광물 캐기
                next += fatigue[minerals[next_idx]][i]
            # 1-2-3. 현재 곡괭이로 광물을 다 캔 경우
            else :
                # 사용한 곡괭이 처리
                pick[i] -= 1
                # 백트래킹 실행
                backtracking(pick, next, next_idx)
                # 곡괭이 복구
                pick[i] += 1
        
    l = len(minerals)
    answer = float("INF")
    # 2. 광물 별 피로도 설정
    fatigue = {"diamond" : [1, 5, 25], "iron" : [1, 1, 5], "stone" : [1, 1, 1]}
    # 3. 백트래킹 실행
    backtracking(picks, 0, -1)
    # 4. 결과 리턴
    return answer