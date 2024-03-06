# 시간초과 참고 링크 : https://www.acmicpc.net/board/view/122519
import sys
from collections import deque
input = sys.stdin.readline

# bfs 함수
def bfs():
    global box
    global tomato
    global zero_cnt
    global wall_cnt
    
    box_size = len(box)* len(box[0])*len(box[0][0])
    
    # 1-1)벽을 제외하고, 전부 다 익은 토마토
    if box_size == wall_cnt + len(tomato):
        return 0
    
    # 1-2)벽을 제외하고, 전부 다 안 익은 토마토
    if box_size == wall_cnt + zero_cnt:
        return -1

    day = 1
    dx,dy,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]
    
    while tomato:
        x,y,z,flag = tomato.popleft()
        
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            
            if nx<0 or nx>=M or ny<0 or ny>=N or nz<0 or nz>=H :
                continue
            
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = flag+1
                zero_cnt -= 1
    
                tomato.append([nx,ny,nz, flag+1])
                
                # day update
                if flag+1 > day:
                    day = flag+1
           
        # 2-1) BFS 진행 중에 안 익은 토마토가 없는 경우
        if zero_cnt == 0:
            return day
    # 2-2) BFS 진행 후에도 안 익은 토마토 있는 경우       
    return -1


if __name__ == '__main__':
    M,N,H = map(int, input().split())
    box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
    
    tomato = deque() # 익은 토마토의 위치
    zero_cnt = 0 # 안익은 토마토 개수
    wall_cnt = 0 # 벽의 개수
    
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if box[k][j][i] == 1:
                    tomato.append([i,j,k,0])
                elif box[k][j][i] == 0:
                    zero_cnt += 1
                else:
                    wall_cnt += 1
    
    print(bfs())