import sys
input = sys.stdin.readline

def dfs(a,n): # a: 멤버 수, n: 탐색하는 멤버의 index
    global result
    
    if a == N//2:
        start, link = 0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += map[i][j]
                elif not visited[i] and not visited[j]:
                    link += map[i][j]
                    
        result = min(result, abs(start - link))
        return 
    
    for i in range(n,N):
        if visited[i]:
            continue
        
        visited[i] = True
        dfs(a+1,i+1) 
        visited[i] = False
    

if __name__ == '__main__':
    N = int(input())
    map = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [False]*N
    result = 1e9
    dfs(0,0)
    
    print(result)