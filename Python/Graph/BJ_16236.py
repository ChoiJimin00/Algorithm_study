import sys
from collections import deque
input = sys.stdin.readline  

def count_fish(x,y,shark_size):
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    tmp = []
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if fishbowl[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    
                    if fishbowl[nx][ny]<shark_size and fishbowl[nx][ny]!=0: # 먹을 수 있는 물고기
                        tmp.append((nx,ny,distance[nx][ny]))
                        
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기를 먹는다
    return sorted(tmp, key=lambda x : (-x[2],-x[0],-x[1]))
                        


if __name__ == '__main__':
    N = int(input())
    fishbowl = [list(map(int, input().split())) for _ in range(N)]
    
    sx,sy = 0,0
    for i in range(N):
        for j in range(N):
            if fishbowl[i][j] == 9:
                x = i
                y = j
                break
            
    cnt = 0
    size = 2
    result = 0
    while True:
        shark = count_fish(x,y,size)
        
        if len(shark) == 0: # 먹을 수 있는 물고기가 공간에 없는 경우
            break
        
        # 먹을 수 있는 물고기
        nx,ny,dist = shark.pop()
        
        result += dist
        fishbowl[x][y],fishbowl[nx][ny] = 0,0
        
        x,y = nx,ny
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0

    print(result)