s, n = map(str, input().rstrip().split())
s = int(s)
# 1. 숫자별 필요한 구역 생성
numbers = {'0' : [1, 2, 3, 5, 6, 7], '1' : [3, 7], '2' : [2, 3, 4, 5, 6], '3' : [2, 3, 4, 6, 7],
           '4' : [1, 3, 4, 7], '5' : [1, 2, 4, 6, 7], '6' : [1, 2, 4, 5, 6, 7],
           '7' : [2, 3, 7], '8' : [1, 2, 3, 4, 5, 6, 7], '9' : [1, 2, 3, 4, 6, 7]}
# 2. 출력 리스트 생성
answer = [[] for _ in range(2 * s + 3)]
# 3.
for number in n :
    # 3-1. 숫자 리스트 생성
    number_lst = [[' ' for _ in range(s+2)] for _ in range(2 * s + 3)]
    # 3-2.
    for area in numbers[number] :
        string = '-' if area % 2 == 0 else '|'
        if area == 1 :
            for i in range(1, 1 + s) : number_lst[i][0] = string
        elif area == 2 :
            for j in range(1, 1 + s) : number_lst[0][j] = string
        elif area == 3 :
            for i in range(1, 1 + s) : number_lst[i][-1] = string
        elif area == 4 :
            for j in range(1, 1 + s) : number_lst[len(number_lst) // 2][j] = string
        elif area == 5 :
            idx = len(number_lst) // 2 + 1
            for i in range(idx, idx + s) : number_lst[i][0] = string
        elif area == 6 :
            for j in range(1, 1 + s): number_lst[-1][j] = string
        else :
            idx = len(number_lst) // 2 + 1
            for i in range(idx, idx + s) : number_lst[i][-1] = string
    # 3-3. 행 별로 출력 리스트에 삽입
    for i in range(2 * s + 3) :
        answer[i] += number_lst[i] + [' ']
# 4. 결과 출력
for line in answer :
    print(''.join(line))