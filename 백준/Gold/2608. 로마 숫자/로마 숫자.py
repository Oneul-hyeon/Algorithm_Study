import sys
input = sys.stdin.readline

# 1. 아라비아 숫자 변환 함수 정의
def to_arabia(roma_num) :
    arabia = 0
    #1-1.
    while roma_num :
        # 1-1-1. 왼쪽 문자 추출
        string = roma_num.pop(0)
        # 1-2-1. 해당 문자가 I, X, C일 경우
        if string in ["I", "X", "C"] :
            # 다음 문자랑 합한 결과가 IV, IX, XL, XC, CD, CM 중에 있을 경우
            if roma_num and string + roma_num[0] in ["IV", "IX", "XL", "XC", "CD", "CM"] :
                # 왼쪽 문자 한 번 더 추출
                string += roma_num.pop(0)
        # 1-2-3. 출력 값 업데이트
        arabia += roma2arabia[string]
    # 1-3. 숫자 반환
    return arabia
# 2. 두 로마 숫자 사용 가능여부 함수 정의
def check(num) :
    # 2-1. 상반되는 문자를 사용한 적이 있는 경우
    if counter[conflicting_characters[num]] == 0 :
        return False
    # 2-2. 이외의 경우
    else :
        return True
# 3. 문자 카운트 함수 정의
def counting(num, cnt) :
    # 3-1. 주어진 문자 감소
    counter[num] -= cnt
    # 3-2. 2글자짜리 수인 경우 처리
    if len(num) == 2 :
        for n in num.split() :
            counter[n] -= 1
# 4. 로마 숫자 변환 함수 정의
def to_roma(arabia) :
    roma = ""
    # 4-1.
    for key, value in roma2arabia.items() :
        # 4-1-1. 남은 수를 현재 아라비아 수로 나눈 몫이 0보다 클 때
        if arabia // value > 0 :
            # 현재 로마 숫자가 2글자인 경우
            if len(key) == 2 :
                # 사용 불가능할 경우 continue
                if not check(key) : continue
            # 로마 숫자 업데이트
            # 남은 수 업데이트
            if arabia // value >= counter[key] :
                roma += key * counter[key]
                arabia -= value * counter[key]
                counting(key, counter[key])
            else :
                cnt = arabia // value
                roma += key * cnt
                arabia -= value * cnt
                counting(key, cnt)
            # 남은 수가 없다면 break
            if arabia == 0 : break
    # 4-2. 로마 숫자 반환
    return roma

roma_num1, roma_num2 = list(input().rstrip()), list(input().rstrip())

# 5. 로마-아라비아 딕셔너리 생성
roma2arabia = {"M" : 1000, "CM" : 900, "D" : 500, "CD" : 400, "C" : 100,
               "XC" : 90, "L" : 50, "XL" : 40, "X" : 10,
               "IX" : 9, "V" : 5, "IV" : 4, "I" : 1}
# 6. 상반되는 문자 딕셔너리 생성
conflicting_characters = {"IV" : "IX", "IX" : "IV",
                          "XL" : "XC", "XC" : "XL",
                          "CD" : "CM", "CM" : "CD"}
# 7. 카운터 딕셔너리 생성
counter = {"V": 1, "L": 1, "D": 1,
           "I": 3, "X": 3, "C": 3, "M": 3,
           "IV" : 1, "IX" : 1, "XL" : 1, "XC" : 1, "CD" : 1, "CM" : 1}
# 7. 아라비아 숫자 구하기
ans_arabia = to_arabia(roma_num1) + to_arabia(roma_num2)
# 8. 로마 숫자 구하기
ans_roma = to_roma(ans_arabia)
# 9. 결과 출력
print(f"{ans_arabia}\n{ans_roma}")