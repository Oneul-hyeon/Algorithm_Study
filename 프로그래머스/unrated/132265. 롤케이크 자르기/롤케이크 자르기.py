from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    # 1. left, right 설정
    left, right = defaultdict(), Counter(topping)
    # 2.
    for i in range(len(topping)) :
        # 2-1. left에 토핑 정보 추가하기
        try : left[topping[i]] += 1
        except : left[topping[i]] = 1
        # 2-2. right에 토핑 정보 제거하기
        right[topping[i]] -= 1
        # 2-3. right에 값이 0 이 되었다면 제거
        if right[topping[i]] == 0 : del right[topping[i]]
        # 2-4. 재료 수 비교
        if len(left) == len(right) : answer += 1
    # 3. 결과 출력
    return answer