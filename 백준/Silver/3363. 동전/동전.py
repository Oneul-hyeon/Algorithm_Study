import sys
input = sys.stdin.readline

def solution() :
    array = [list(map(str, input().rstrip().split(' '))) for _ in range(3)]
    # 1. 무거울 가능성, 가벼울 가능성이 있는 리스트 생성
    big, small = set(list(map(str, range(1, 13)))), set(list(map(str, range(1, 13))))
    # 2.
    for _ in range(3) :
        for information in array :
            idx = -1
            for i in range(len(information)) :
                if information[i] in ['<', '>', '='] :
                    idx = i
                    break
            sign, info1, info2 = information[idx], set(information[:idx]), set(information[idx+1:])
            # 3-1.
            if sign == '>' :
                big = big & info1
                small = small & info2
            # 3-2.
            elif sign == '<' :
                big = big & info2
                small = small & info1
            else :
                big = big - (info1 | info2)
                small = small - (info1 | info2)
    # 4. 결과 출력
    if not big and not small : print('impossible')
    elif not small and len(big) == 1 : print(f'{big.pop()}+')
    elif not big and len(small) == 1 : print(f'{small.pop()}-')
    else : print('indefinite')
if __name__ == "__main__":
    solution()