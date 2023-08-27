def solution(n, s):
    answer = []
    if n>s : return [-1]
    else :
        answer = [s//n] * n
        if s%n :
            for i in range(s%n) :
                answer[-1-i]+=1
        return answer