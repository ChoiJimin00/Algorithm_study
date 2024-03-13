from collections import deque
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    q = deque()
    
    for _ in range(N):
        order = list(map(str, input().split()))
        
        if order[0] == 'push':
            q.append(order[1])
        elif order[0] == 'pop':
            print(-1 if len(q)==0 else q.popleft())
        elif order[0] == 'size':
            print(len(q))
        elif order[0] == 'empty':
            print(1 if len(q) == 0 else 0)
        elif order[0] == 'front':
            print(-1 if len(q) == 0 else q[0])
        else:
            print(-1 if len(q) == 0 else q[-1])