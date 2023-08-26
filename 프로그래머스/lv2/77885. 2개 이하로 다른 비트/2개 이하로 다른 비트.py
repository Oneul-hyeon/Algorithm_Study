# 1. 최솟값 반환 함수 정의
def return_min(num) :
    # 1-1. 짝수인 경우
    if num % 2 == 0 :
        # 1을 더한 값 리턴
        return num + 1
    # 1-2. 홀수인 경우
    else :
        # 이진 비트로 변환
        bit = list('0' + bin(num)[2:])
        for i in range(len(bit)-1, -1, -1) :
            # '0'값을 가지는 인덱스 찾기
            if bit[i] == '0' :
                index = i
                break
        # 값 변환
        bit[index], bit[index+1] = '1', '0'
        # 10진수로 변환한 값 리턴
        return int(''.join(bit), 2)

def solution(numbers):
    # 2. 결과 리스트 리턴
    return [return_min(num) for num in numbers]