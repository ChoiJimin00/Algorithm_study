import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global map
    start_x, start_y, distance = start
    
    q = deque([start])
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    
    visited = [[-1]*m for _ in range(n)]
    visited[start_x][start_y] = distance
    
    while q:
        con = q.popleft()
        x,y,distance = con[0],con[1],con[2]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map[nx][ny] == 1 and visited[nx][ny] == -1 :
                visited[nx][ny] = distance+1
                q.append([nx,ny,distance+1])
                
    # 벽 표시
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                visited[i][j] = 0
    
    # 출력
    for i in range(n):
        print(*visited[i])
        

if __name__ == '__main__':
    n,m = map(int, input().split())
    map = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                start = [i,j,0]
                
    bfs(start)