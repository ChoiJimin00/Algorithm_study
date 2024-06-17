import sys
from collections import deque
input = sys.stdin.readline

def topology():
    q = deque()
    
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            
    result = []
    while q:
        n = q.popleft()
        result.append(n)
        
        for v in graph[n]:
            indegree[v] -= 1
        
            if indegree[v] == 0:
                q.append(v)
                
    return result
        

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    indegree = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        n1, n2 = map(int, input().split())
        indegree[n2] += 1
        graph[n1].append(n2)
    
    print(*topology())