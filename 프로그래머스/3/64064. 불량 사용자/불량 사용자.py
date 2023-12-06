answer = []
def solution(user_id, banned_id):
    # 1. 백트래킹 함수 정의
    def backtracking(idx, combination) :
        # 1-1. 종료 조건 설정
        if idx == n :
            combination.sort()
            if combination not in answer :
                answer.append(combination)
            return
        # 1-2. 현재 불량 사용자 아이디에 해당하는 아이디가 없을 경우
        if not possible_id[idx] :
            backtracking(idx+1, combination)
        # 1-3. 현재 불량 사용자 아이디에 해당하는 아이디가 있을 경우
        else :
            # 1-3-1. 
            for id in possible_id[idx] :
                # 다음 아이디가 현재 아이디 목록에 없을 경우 백트래킹 실행
                if id not in combination :
                    backtracking(idx+1, combination + [id])
    
    n = len(banned_id)
    # 2. 불량 사용자로 가능한 아이디 리스트 생성
    possible_id = []
    # 3.
    for b_id in banned_id :
        # 3-1. 현재 불량 아이디로 가능한 아이디 리스트 생성
        array = []
        # 3-2.
        for u_id in user_id :
            # 가능할 경우 append
            if len(u_id) == len(b_id) :
                for i in range(len(b_id)) :
                    if b_id[i] == '*' : continue
                    if u_id[i] != b_id[i] : break
                else :
                    array.append(u_id)
        # 3-3. 불량 사용자로 가능한 아이디 리스트에 append
        possible_id.append(array)
    # 4. 백트래킹 실행
    backtracking(0, [])
    # 5. 결과 리턴
    return len(answer)