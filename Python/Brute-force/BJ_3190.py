from collections import deque
import sys
input = sys.stdin.readline

# 구현 사항
# 1. 맵은 0, 사과 2, 뱀은 1로 채우기
# 2. 뱀이 이동할 때 머리, 꼬리는 한칸씩 전진 (꼬리 pop, 머리 append)
# 3. 이동했을 때 사과먹으면, 머리 전진 꼬리 그대로 (머리 append) - 사과있던 space = 0으로 바꾸기
# 4. 방향 전환 타이밍에 맞춰 L:왼쪽 D:오른쪽

def turn(alpha):
    global direction
    
    if alpha == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    

def dummy():
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    
    snake = deque()  # 뱀의 좌표
    snake.append((0,0))
    
    cnt = 0
    x, y = 0,0  # 머리의 좌표
    space[x][y] = 1
    
    while True:
        cnt += 1
        x += dx[direction]
        y += dy[direction]
        
        if x<0 or x>=N or y<0 or y>=N:
            break
        
        if space[x][y] == 2: # 사과 먹을 경우
            space[x][y] = 1
            snake.append((x,y))
            
            if cnt in dict:
                turn(dict[cnt])
                
        elif space[x][y] == 0: # 빈칸인 경우
            space[x][y] = 1
            snake.append((x,y))
            tx, ty = snake.popleft()
            space[tx][ty] = 0
            
            if cnt in dict:
                turn(dict[cnt])
                
        else:  # 더이상 이동하지 않는 경우
            break
            
    print(cnt)
    
    
if __name__ == '__main__':
    N = int(input())
    space = [[0]*N for _ in range(N)]
    
    K = int(input()) # 사과
    for _ in range(K):
        x,y = map(int, input().split())
        space[x-1][y-1] = 2
        
    dict = {} # 방향 
    L = int(input())
    for _ in range(L):
        X, C = input().split()
        dict[int(X)] = C
        
    direction = 0

    dummy()