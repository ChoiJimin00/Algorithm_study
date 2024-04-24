import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 재귀로 구현한 DFS
def dfs1(v):
    global graph, visited
    
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs1(i)
            
# stack으로 구현한 DFS        
def dfs2(start):
    global graph, visited
    
    stack = [start]
    while stack:
        v = stack.pop()
        
        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
    

if __name__ == '__main__':
    n,m = map(int, input().split()) 
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    cnt = 0
    visited = [False]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            dfs2(i)
            cnt += 1
            
    print(cnt)