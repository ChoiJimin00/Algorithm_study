# 참고: 0-1 너비 우선 (https://xkdls19.tistory.com/63)
# a=0,1일때가 엣지케이스 (0일때 무한루프 도는 상황을 잡아야 함, 1에서 0으로 가는 경우를 막아야 함)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    que = deque()
    limit = 100001
    time = [0]*limit
    
    if x == 0:
        que.append(1)
    else:
        que.append(x)
    
    while que:
        x = que.popleft()
          
        if y == x:
            return time[x]
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < limit and time[nx]==0 :
                if nx == 2*x:
                    time[nx] = time[x]
                    que.appendleft(nx) # appendleft : 다른 연산보다 우선순위 부여
                else:
                    time[nx] = time[x] + 1
                    que.append(nx)
                
        
if __name__ == '__main__':
    N,K = map(int, input().split())
    
    if N == 0:
        if K == 0:
            print(0)
        else: 
            print(bfs(N,K)+1)
    else:
        print(bfs(N,K))