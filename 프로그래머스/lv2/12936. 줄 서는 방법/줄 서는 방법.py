import math
def solution(n, k):
    answer = []
    k -= 1
    # 1. 정렬된 수가 들어있는 리스트 만들기
    array = list(range(1, n+1))
    while array :
        # 2-1. 출력 리스트에 수 넣기
        answer.append(array.pop(k // math.factorial(n-1)))
        # 2-2. k 재정의
        k = k % math.factorial(n-1)
        # 2-3. n 값 1 빼기
        n -= 1
    return answer