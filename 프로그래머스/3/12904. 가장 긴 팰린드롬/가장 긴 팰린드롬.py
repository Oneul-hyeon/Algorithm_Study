def solution(s):
    # 1. 팰린드롬 체크 함수 정의
    def check(string) :
        # 1-1. left, right 설정
        left, right = 0, len(string) - 1
        # 1-2.
        while left < right :
            # 1-2-1. left, right 인덱스의 글자가 다를 경우 False 반환
            if string[left] != string[right] : return False
            # 1-2-2. left, right 값 변환
            left += 1
            right -= 1
        # 1-3. True 반환
        return True
    # 2.
    for length in range(len(s), 0, -1) :
        for i in range(len(s) - length + 1) :
            if check(s[i : i + length]) :
                return length