import copy
import sys
input = sys.stdin.readline


# 사무실의 범위를 벗어나는지 체크
def check(row, col):
    return row < 0 or row >=N or col < 0 or col >=M
    
    
# cctv 번호, 위치 저장
def init():
    obj = []
    answer = 0
    for i in range(N):
        for j in range(M):
            if map[i][j] != 6 and map[i][j] != 0:
                obj.append((map[i][j], i, j))   # cctv번호, cctv 좌표 저장
            if map[i][j] == 0:answer += 1
    return obj, answer


# 각각의 방향에 대해 이동
def move(y, x, direc, map_copy):
    for d in direc:
        ny, nx = y, x
        
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어났거나 벽을 만났다면 
            if check(ny, nx) or map_copy[ny][nx] == 6:
                break
            # 빈칸이아니면 
            if map_copy[ny][nx] != 0:
                continue
            map_copy[ny][nx] = '#'


# 사각지대를 구하는 함수        
def zero_cnt(map_copy):
    global answer
    cnt = 0
    for i in map_copy:
        cnt += i.count(0)
    answer = min(answer, cnt) 
    

def dfs(level, map):
    map_copy = copy.deepcopy(map)           
    # 이전 상태가 실행되기전 바로 전 상태 저장
    
    if level == len(cctv):
        zero_cnt(map_copy)
        return			
    
    number, y, x  = cctv[level]
    
    for d in direction[number]:    
        move(y, x, d, map_copy)
        dfs(level+1, map_copy)   
        map_copy = copy.deepcopy(map)
        # 하나의 상태를 return 한 다음 바로 전 상태로 바꿈  


if __name__ == '__main__':
    N, M = map(int, input().split()) # 세로(N), 가로(M)
    map = [list(map(int, input().split())) for _ in range(N)]

    # 남, 동, 북, 서 
    dx,dy = [0, 1, 0, -1],[1, 0, -1, 0]
    
    # 감시해야하는 모든 방향 (각각의 cctv별로 감시할 수 있는 방향)
    direction = {
        1: [[0], [1], [2], [3]],           
        2: [[0, 2], [1, 3]],                    
        3: [[0, 1], [1, 2], [2, 3], [3, 0]],    
        4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],    
        5: [[0, 1, 2, 3]]                    
    }
    
    cctv, answer = init()
    dfs(0, map)
    print(answer)