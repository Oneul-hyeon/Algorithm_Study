import math
def solution(k, d):
    # 1. 출력 변수 설정 
    answer = 0
    # 2. 
    for i in range(0, d+1, k) :
        # 2-1. 점화식에 따른 점 찍기 카운팅
        answer += int(math.sqrt(d**2 - i**2))//k + 1
    # 3. 결과 리턴
    return answer