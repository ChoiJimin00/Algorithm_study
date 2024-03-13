import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
router = deque()

while True:
    p = int(input())
    
    if p == -1 : break
    elif p == 0 : router.popleft()
    else : 
        if len(router)<N:
            router.append(p)
    
if len(router)==0:
    print('empty')
else:
    for i in range(N):
        try: 
            print(router[i], end = ' ')
        except:
            break