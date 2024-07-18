import sys, copy
input = sys.stdin.readline

def opers(direction, state):
    
    # 1. 왼쪽 방향
    if direction == 0 :
        for i in range(N):
            cursor = 0
            for j in range(1, N):
                
                if state[i][j] == 0:
                    continue
                
                tmp = state[i][j]
                state[i][j] = 0
                
                if state[i][cursor] == 0: # 비어 있으면 옮긴다
                    state[i][cursor] = tmp
                elif state[i][cursor] == tmp: # 같으면 합친다
                    state[i][cursor] *= 2
                    cursor += 1
                else: # 비어있지 않고 다른 값이면, 옆에 붙힘
                    cursor += 1
                    state[i][cursor] = tmp
           
    # 2. 오른쪽 방향         
    if direction == 1 :
        for i in range(N):
            cursor = N-1
            for j in range(N-1,-1,-1):
                
                if state[i][j] == 0:
                    continue
                
                tmp = state[i][j]
                state[i][j] = 0
                
                if state[i][cursor] == 0: 
                    state[i][cursor] = tmp
                elif state[i][cursor] == tmp: 
                    state[i][cursor] *= 2
                    cursor -= 1
                else: 
                    cursor -= 1
                    state[i][cursor] = tmp
     
    # 3. 위쪽 방향               
    if direction == 2 :
        for j in range(N):
            cursor = 0
            for i in range(1, N):
                
                if state[i][j] == 0:
                    continue
                
                tmp = state[i][j]
                state[i][j] = 0
                
                if state[cursor][j] == 0: 
                    state[cursor][j] = tmp
                elif state[cursor][j] == tmp: 
                    state[cursor][j] *= 2
                    cursor += 1
                else: 
                    cursor += 1
                    state[cursor][j] = tmp
                    
    # 4. 아래쪽 방향          
    if direction == 3 :
        for j in range(N):
            cursor = N-1
            for i in range(N-1,-1,-1):
                
                if state[i][j] == 0:
                    continue
                
                tmp = state[i][j]
                state[i][j] = 0
                
                if state[cursor][j] == 0: 
                    state[cursor][j] = tmp
                elif state[cursor][j] == tmp: 
                    state[cursor][j] *= 2
                    cursor -= 1
                else: 
                    cursor -= 1
                    state[cursor][j] = tmp

    return state


def dfs(times, state):
    if times == 5:
        max_values.append(max(map(max, state)))
        return
    
    for i in range(4):
        copy_state = copy.deepcopy(state)
        new_state = opers(i, copy_state)
    
        dfs(times+1, new_state)


if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    max_values = []
    dfs(0,board)
    print(max(max_values))