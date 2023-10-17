import sys
input = sys.stdin.readline

def solution() :
    q = int(input())
    ans_p = ''
    ans_n = 0
    # 1. 초기 최솟값, 최댓값 설정
    min_, max_ = -10**18, 10**18
    # 2.
    for i in range(1, q+1) :
        # 2-1. 수와 정보 입력받기
        n, c = map(str, input().rstrip().split())
        n = int(n)
        # 2-2. '^' 명령일 경우
        if c == '^' :
            if n < min_ : continue
            # 모순되지 않은 경우 최솟값 업데이트
            if n < max_ : min_ = n+1
            # 모순된 경우
            else : print(f'Paradox!\n{i}'); break
        # 2-3. 'v' 명령일 경우
        elif c == 'v' :
            if n > max_ : continue
            # 모순되지 않은 경우 최솟값 업데이트
            if n > min_ : max_ = n-1
            # 모순된 경우
            else : print(f'Paradox!\n{i}'); break
        # 2-4. 최솟값과 최댓값이 같은 경우
        if min_ == max_ :
            if not ans_p :
                ans_p, ans_n = 'I got it!', i
    # 3. 답을 찾지 못한 경우
    else :
        if ans_p : print(f'{ans_p}\n{ans_n}')
        else: print('Hmm...')

if __name__ == "__main__":
    solution()