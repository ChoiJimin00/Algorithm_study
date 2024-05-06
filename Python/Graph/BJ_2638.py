import sys
from collections import deque
input = sys.stdin.readline

# 공기를 기준으로 bfs 탐색
def melting():
    global cheese
    
    q = deque()
    q.append([0,0])
    visited = [[0]*M for _ in range(N)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
        
    while q:
        x,y = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
                
            if cheese[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny] = 1
                q.append([nx,ny])
            
            # 치즈 방문 횟수 count
            if cheese[nx][ny]==1:
                visited[nx][ny] += 1
    
    # 방문 횟수가 2회 이상인 치즈 제거
    cnt_cheese = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                cheese[i][j] = 0
                cnt_cheese += 1
                
    return cnt_cheese
    

if __name__ == '__main__':
    N,M = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    
    while melting():
        cnt += 1
        
    print(cnt)