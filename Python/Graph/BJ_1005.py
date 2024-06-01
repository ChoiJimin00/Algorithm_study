import sys
from collections import deque
input = sys.stdin.readline

# 위상 정렬
def topology_sort():
    dp = [0]*(N+1) # 해당 건물까지 걸리는 시간
    
    q = deque()
    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)
            dp[i] = value[i]
            
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            indegree[i] -= 1
            dp[i] = max(dp[v]+value[i], dp[i])

            if indegree[i] == 0:
                q.append(i)
    return dp[W]      
    
if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        N,K = map(int, input().split())
        value = [0]+list(map(int, input().split()))
    
        indegree = [0]*(N+1)
        graph = [[] for _ in range(N+1)]
        
        for _ in range(K):
            a,b = map(int, input().split())
            graph[a].append(b)
            indegree[b] += 1
        
        W = int(input())
            
        print(topology_sort())