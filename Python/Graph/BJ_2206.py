import sys
from collections import deque
input = sys.stdin.readline

def bfs(sx,sy,sd):
    global map
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    
    q = deque()
    q.append((sx,sy,sd))
    
    while q:
        x,y,d = q.popleft()
        
        if x==N-1 and y==M-1:
            return visited[x][y][d]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            
            # 다음 step이 벽 & 파괴한 적이 없는 경우
            if map[nx][ny]==1 and d == 0:
                visited[nx][ny][1] = visited[x][y][0]+1
                q.append((nx,ny,1))
            
            # 다음 step이 길 & 한번도 방문하지 않은 곳
            elif map[nx][ny]==0 and visited[nx][ny][d] == 0:
                visited[nx][ny][d] = visited[x][y][d]+1
                q.append((nx,ny,d))
    return -1
    

if __name__ == '__main__':
    N,M = map(int, input().split())
    map = [list(map(int, input().strip())) for _ in range(N)]
    
    # 3차원 행렬로 벽의 파괴를 파악 -> visited[x][y][0]은 벽 파괴 가능할 때, 현재까지 거리 / [x][y][1]은 불가능할 때, 현재까지 거리
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1  # 시작점에서 거리 1로 설정
    
    print(bfs(0,0,0))