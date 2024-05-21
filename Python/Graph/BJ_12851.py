import sys
from collections import deque
input = sys.stdin.readline

def find(N,K):
    q = deque()
    q.append(N)
    
    result, cnt = 0,0 # 가장 빠른 시간, 방법의 수
    visited = [0]*100001 # 최대 크기
    
    while q:
        v = q.popleft()
        
        tmp = visited[v]
        if v == K:
            result = tmp
            cnt += 1
            continue
    
        for n in [v-1, v+1, v*2]:
            if 0 <= n <= 100000 and (visited[n]==0 or visited[n]==visited[v]+1): #범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
                visited[n] = visited[v]+1
                q.append(n)
                
    print(result)
    print(cnt)

if __name__ == '__main__':
    N,K = map(int,input().split())
    find(N,K)