import sys
import copy
from collections import deque
input = sys.stdin.readline

def bfs():
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    tmp_graph = copy.deepcopy(graph)
    
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i,j))
                
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))
        
    global answer
    cnt = 0
    for i in range(N):
        cnt += tmp_graph[i].count(0)
    answer.append(cnt)
                

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return 
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j]=1
                make_wall(cnt+1)
                graph[i][j]=0 # 백트래킹


if __name__ == '__main__':
    N,M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    answer = []
    make_wall(0)
    print(max(answer))