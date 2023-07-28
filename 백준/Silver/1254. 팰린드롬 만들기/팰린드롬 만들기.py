import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = string1[::-1]
l = 0
while True :
    plus_s = string1[:l]
    if string1 + plus_s[::-1] == plus_s + string2 :
        print(len(string1) + l)
        break
    else : l+=1