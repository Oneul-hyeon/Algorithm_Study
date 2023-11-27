import sys
input = sys.stdin.readline

def solution(l, r):
    # 1. 두 수의 단위가 다를 경우
    if len(str(l)) != len(str(r)) : print(0)
    # 2. 두 수의 단위가 같을 경우
    else :
        ans = 0
        l, r = str(l), str(r)
        for l1, r1 in zip(l, r) :
            if l1 == r1 :
                if l1 == '8' : ans += 1
            else : break
        print(ans)

if __name__ == "__main__" :
    l, r = map(int, input().split())
    solution(l, r)