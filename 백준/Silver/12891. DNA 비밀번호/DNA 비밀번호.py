import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. DNA 문자열 리스트로 입력받기
string = input().rstrip()
a, c, g, t = map(int, input().split())
string_dic = {'A' : a, 'C' : c, 'G' : g, 'T' : t}
string_count = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
# 초기 카운트 딕셔너리 생성
count = 0
# 3. 최소 문자열 개수 체크
for i in range(n-m+1) :
    # 생성된 문자 처리
    if i > 0 :
        string_count[string[i + m - 1]] += 1
        string_count[string[i - 1]] -= 1
    else :
        for key, value in dict(Counter(string[:m])).items() : string_count[key] = value
    # 문자 체크
    for x in ['A','C','G','T'] :
        if string_dic[x] > string_count[x] :
            break
    else : count += 1

# 4. 결과 출력
print(count)