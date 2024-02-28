import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [-1,0,1,0], [0,1,0,-1] # 북 동 남 서

# 근처 4칸 중 청소할 곳이 있는지 확인하는 함수
def check_room(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            return True
    return False

clean_cnt = 0
while True:
    # 1) 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2
        clean_cnt += 1
        
    # 3) 사방에 청소할 칸 존재
    if check_room(r,c):
        while True:
            d = (4+d-1) % 4 # 3.1 방향 반시계 방향으로 회전
            if room[r+dx[d]][c+dy[d]] == 0: # 바라보는 방향이 청소가 되지 않은 칸이라면
                r = r + dx[d]
                c = c + dy[d]
                break
            
    # 2) 사방에 청소할 칸 존재 X  
    else:
        if room[r - dx[d]][c - dy[d]]== 1: # 2.2 바라보는 방향의 뒤가 벽 
            break
        else: # 2.1 한칸 후진
            r = r - dx[d]
            c = c - dy[d]
                 
print(clean_cnt)