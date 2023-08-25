import math
def solution(arrayA, arrayB):
    # 1. 공약수 반환 함수 선언
    def return_cd(array) :
        # 1-1. 반환 리스트 생성
        cd_array = set()
        # 1-2.
        gcd_ = array[0]
        for num in array[1:] :
            # 카드들의 최대 공약수 구하기
            gcd_ = math.gcd(gcd_, num)
        # 1-3.
        for i in range(1, int(gcd_ ** 0.5) + 1) :
            # 최대공약수의 약수 구하기
            if gcd_ % i == 0 :
                cd_array.add(i)
                cd_array.add(gcd_ // i)
        # 1-4. 리스트 반환
        return cd_array
    answer = 0
    # 2.
    for cd in return_cd(arrayA) :
        for num in arrayB :
            if num % cd == 0 : break # 나누어 떨어질 경우 break
        # for문 완료 시 최댓값 업데이트
        else : answer = max(answer, cd)
    # 3.
    for cd in return_cd(arrayB) :
        for num in arrayA :
            if num % cd == 0 : break # 나누어 떨어질 경우 break
        # for문 완료 시 최댓값 업데이트
        else : answer = max(answer, cd)
    # 4. 결과 리턴
    return answer