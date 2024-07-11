import sys
input = sys.stdin.readline

string1, string2 = " " + input().strip(), " " + input().strip()
# 1. LCS 리스트 생성
LCS = [[0 for _ in range(len(string2))] for _ in range(len(string1))]
# 2.
for i in range(1, len(string1)) :
    for j in range(1, len(string2)) :
        # 2-1. 비교하는 문자가 같을 경우 점화식 처리
        if string1[i] == string2[j] :
            LCS[i][j] = LCS[i-1][j-1] + 1
        # 2-2. 비교하는 문자가 다를 경우 점화식 처리
        else :
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
# 3. 결과 출력
print(LCS[-1][-1])