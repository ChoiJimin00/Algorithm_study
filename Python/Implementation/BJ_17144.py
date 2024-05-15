import sys
import copy
input = sys.stdin.readline

def diffusion(map):
    tmp_map = copy.deepcopy(map)
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    for i in range(r):
        for j in range(c):
            if map[i][j] >= 5:
                value = map[i][j]//5
                cnt = 0
                
                for idx in range(4):
                    nx = i + dx[idx]
                    ny = j + dy[idx]
                    
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    
                    if map[nx][ny] == -1:
                        continue
                    
                    tmp_map[nx][ny] += value
                    cnt += 1
                tmp_map[i][j] -= (value*cnt)
    
    return tmp_map
           
                
def air_clean(map):
    
    for i in range(r):
        if map[i][0] == -1:
            x1,y1 = i,0
            break
    x2,y2 = x1+1, 0
    
    # counter clock-wise air cleaning
    nx, ny = x1-1, y1
    while nx-1 >= 0:
        map[nx][0] = map[nx-1][0]
        nx -= 1
    while ny+1 <= c-1:
        map[0][ny] = map[0][ny+1]
        ny += 1
    while nx+1 <= x1:
        map[nx][c-1] = map[nx+1][c-1]
        nx += 1
    while ny-1 >= 1:
        map[x1][ny] = map[x1][ny-1]
        ny -= 1
    map[x1][y1+1] = 0
        
    # clock-wise air cleaning
    nx, ny = x2+1, y2
    while nx+1 <= r-1:
        map[nx][0] = map[nx+1][0]
        nx += 1
    while ny+1 <= c-1:
        map[r-1][ny] = map[r-1][ny+1]
        ny += 1
    while nx-1 >= x2:
        map[nx][c-1] = map[nx-1][c-1]
        nx -= 1
    while ny-1 >= 1:
        map[x2][ny] = map[x2][ny-1]
        ny -= 1
    map[x2][y2+1] = 0
    
    return map
    
    
def cycle(map):
    for _ in range(t):
        tmp_map = diffusion(map)
        map = air_clean(tmp_map)
        
    result = 2
    for i in range(r):
        result += sum(map[i])
    print(result)
        

if __name__ == '__main__':
    r,c,t = map(int, input().split())
    map = [list(map(int, input().split())) for _ in range(r)]
    
    cycle(map)