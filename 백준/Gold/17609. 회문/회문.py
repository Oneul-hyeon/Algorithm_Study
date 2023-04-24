import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    string = input().rstrip()
    # 1. 회문 여부 체크
    if string == string[::-1] : print(0)
    # 2. 회문이 아닐 경우
    else :
        # 3. start, end 설정
        start, end = 0, len(string)-1
        # 4. while문
        while start<end :
            # 5. start, end 인덱스의 문자가 동일한지 체크
            # 5-1. 동일하지 않은 경우
            if string[start] != string[end] :
                # 1) start += 1 했을 때 나머지 문자가 동일한지 체크
                # 2) end -= 했을 때 나머지 문자가 동일한지 체크
                if string[start+1:end+1] == string[start+1:end+1][::-1] or string[start:end] == string[start:end][::-1]: ans = 1
                else : ans = 2
                break
            # 5-2. 동일한 경우
            else :
                start += 1
                end -= 1
        # 6. 결과 출력
        print(ans)
