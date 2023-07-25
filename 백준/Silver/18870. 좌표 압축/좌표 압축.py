import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
array_2 = array.copy()
array_2 = sorted(list(set(array_2)))
dic = {array_2[i]:i for i in range(len(array_2))}
for i in array :
    print(dic[i], end=' ')