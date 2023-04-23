import sys
input = sys.stdin.readline
# 1. 재귀 함수 선언
def dfs(consonants, vowels, index) :
    # 2. 종료 조건 설정
    if index == l :
        # 2-1. 자음, 모음의 조건 체크 후 출력
        if consonants >=2 and vowels >=1 :
            print(''.join(password))
    # 3. for문
    for char in array :
        # password가 알파벳이 증가하는 순서로 설정되어 있으므로 '오름차순'으로 되어 있음
         if password == [] or ord(password[-1]) < ord(char):
            # 3-1. 리스트에 알파벳 append
            password.append(char)
            # 3-2. 해당 인덱스의 알파벳이 자음인지 모음인지 체크
            # 3-4. 모음일 경우 재귀 함수 실행
            if char in ['a', 'e', 'i', 'o','u'] : dfs(consonants, vowels+1, index+1)
            # 3-3. 자음일 경우 재귀 함수 싫행
            else : dfs(consonants+1, vowels, index+1)
            # 3-5. 리스트에서 알파벳 빼기
            password.pop()
#4. 변수 입력받기
l, c = map(int, input().split())
array = list(map(str, input().rstrip().split()))
password = []
# 5. 알파벳 리스트 정렬하기
array.sort()
# 6.재귀함수 실행
dfs(0, 0, 0)