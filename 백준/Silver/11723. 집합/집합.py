import sys
input = sys.stdin.readline

m = int(input())
S = 0
for _ in range(m) :
    command = input().rstrip()
    if command == 'all' :
        S = ( 1 << 20 ) - 1
    elif command == 'empty' :
        S = 0
    else :
        c, n = command.split()
        n = int(n) - 1
        if (c == "add" and not S & ( 1 << n )) or (c == "remove" and S & ( 1 << n )) : S ^= ( 1 << n )
        elif c == "check" : print(1 if S & ( 1 << n ) else 0)
        elif c == "toggle" : S ^= ( 1 << n )
