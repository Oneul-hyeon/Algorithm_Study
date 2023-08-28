def solution(numbers):
    # 1. numbers 의 값을 문자열로 변환
    numbers = [str(num) for num in numbers]
    # 2. 정렬
    numbers.sort(key = lambda x : x * 3, reverse = True)
    # 3. 결과 리턴
    return str(int(''.join(numbers)))