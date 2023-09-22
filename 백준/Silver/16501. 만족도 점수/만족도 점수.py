import sys
from itertools import combinations
input = sys.stdin.readline

# 1. 코트의 만족도 점수 계산 함수 생성
def return_score(people) :
    # 1-1. 인원의 실력 점수 리스트 생성 후 정렬
    array = []
    for idx in people :
        array.append(ability[idx])
    array.sort()
    # 1-2. 팀을 나눠 만족도 점수 계산
    score = 1 - (abs((array[0] + array[3])/2 - (array[1] + array[2])/2)/10)
    # 1-3. 계산된 점수 리턴
    return score
def solution(ability) :
    ans = -float('inf')
    # 2. 1번 코트에 들어갈 인원 조합 구하기
    combination = combinations(range(1, 9), 4)
    for court1 in combination :
        # 3. 2번 코트에 들어갈 인원 조합 구하기
        court2 = [i for i in range(1, 9) if i not in court1]
        # 4. 두 코트 중 낮은 만족도 구하기
        # 5. 만족도의 최댓값 업데이트
        ans = max(ans, min(return_score(court1), return_score(court2)))
    # 6. 결과 출력
    print(round(ans, 2))
    
if __name__ == '__main__' :
    ability = [0] + list(map(float, input().split()))
    solution(ability)