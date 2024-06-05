import sys
input = sys.stdin.readline

def topology_sort():
    q = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            
    result = []
    while q:
        q.sort()
        v = q.pop(0)
        result.append(v)
        
        for n in graph[v]:
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)
                
    return result


if __name__ == '__main__':
    N,M = map(int, input().split())
    
    graph =[[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    
    for i in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
        
    print(*topology_sort())