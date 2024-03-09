# DFS, DP로 풀 수 있음
import sys
input = sys.stdin.readline
 
# 방법 1 ) DFS로 푸는 방법
def dfs(x,y,direction):
    global house
    n = len(house)
        
    state = []
    state.append([x,y,direction]) # direction: 가로(0), 세로(1), 대각선(2)
        
    cnt = 0
    while state:
        x,y,direction = state.pop()
        
        if (x==n-1 and y==n-1): 
            cnt += 1
            continue
    
        if direction == 0 : # 가로
            # 가로
            nx,ny = x,y+1
            if 0<=nx<n and 0<=ny<n and house[nx][ny]==0:
                state.append([nx,ny,0])
            # 대각선
            nx,ny = x+1, y+1
            if 0<=nx<n and 0<=ny<n:
                if house[nx][ny]==0 and house[nx-1][ny]==0 and house[nx][ny-1]==0:
                    state.append([nx,ny,2])
                    
        elif direction == 1 : # 세로
            # 세로
            nx,ny = x+1,y
            if 0<=nx<n and 0<=ny<n and house[nx][ny]==0:
                state.append([nx,ny,1])
            # 대각선
            nx,ny = x+1, y+1
            if 0<=nx<n and 0<=ny<n:
                if house[nx][ny]==0 and house[nx-1][ny]==0 and house[nx][ny-1]==0:
                    state.append([nx,ny,2])
        
        else: # 대각선
            # 가로
            nx,ny = x,y+1
            if 0<=nx<n and 0<=ny<n and house[nx][ny]==0:
                state.append([nx,ny,0])
            # 세로
            nx,ny = x+1,y
            if 0<=nx<n and 0<=ny<n and house[nx][ny]==0:
                state.append([nx,ny,1])
            # 대각선
            nx,ny = x+1, y+1
            if 0<=nx<n and 0<=ny<n:
                if house[nx][ny]==0 and house[nx-1][ny]==0 and house[nx][ny-1]==0:
                    state.append([nx,ny,2])
    return cnt

# 방법 2 ) DP로 푸는 방법
def dp():
    global house
    n = len(house)

    dp=[[[0,0,0] for _ in range(n)] for _ in range(n)] # 0번 요소: x좌표 / 1번 요소: y좌표 / 2번 요소: 방향 (가로 0, 세로 1, 대각선 2)
    
    dp[0][1][0] = 1
    
    for i in range(2,n):
        if house[0][i] == 0:
            dp[0][i][0] = dp[0][i-1][0]
            
    for i in range(1,n):
        for j in range(1,n):
            if house[i][j] == 1: # 벽을 만난 경우
                continue
            
            # house[i][j]가 가로 방향일 수 있는 경우 : 이전 칸 house[i][j-1]가 가로 일때, house[i][j-1]가 대각선일때
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] 
            # house[i][j]가 세로 방향일 수 있는 경우 : 이전 칸 house[i-1][j]가 세로 일때, house[i-1][j]가 대각선일때
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] 
            
            # house[i][j]가 대각선 일 수 있는 경우: house[i-1][j-1]의 모든 경우(가로,세로,대각선)일때
            if house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] = sum(dp[i-1][j-1])
            
    return sum(dp[n-1][n-1])
                
if __name__ == '__main__':
    n = int(input())
    house = [list(map(int,input().split())) for _ in range(n)]
    
    if (house[0][2]==1 and house[1][2] == 1) or (house[n-1][n-2]==1 and house[n-2][n-1]==1) or house[n-1][n-1]==1:
        print(0)
    
    else:
        #print(dfs(0,1,0))
        print(dp())