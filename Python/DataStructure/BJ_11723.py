import sys
input = sys.stdin.readline

num = set()

M = int(input())
for _ in range(M):
    cmd = input().split()
    
    if cmd[0] == 'add':
        num.add(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in num:
            num.remove(cmd[1])
    elif cmd[0] == 'check':
        print(1 if cmd[1] in num else 0)
    elif cmd[0] == 'toggle':
        if cmd[1] in num:
            num.remove(cmd[1])
        else:
            num.add(cmd[1])
    elif cmd[0] == 'all':
        num = set([str(i) for i in range(1, 21)])
    else:
        num = set()