R,C = map(int,input().split())
matrix = []

for _ in range(R):
    matrix.append(list(map(str,input())))

def dfs(x,y):
    stack = []
    stack.append((x,y))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    alpha = [] # 현재 경로에 포함된 알파벳 저장
    branch = [] # 경로가 2개 이상의 path로 쪼개지는 경우의 alphabet 저장 : 형식 (alphabet, times)
    max_length = 0
    
    while stack:
        x,y = stack.pop()
        alpha.append(matrix[x][y]) # 경로에 alphabet 추가
        #breakpoint()
        
        origin_stack = len(stack)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=R or ny<0 or ny>=C:
                continue
            
            if matrix[nx][ny] not in alpha:
                stack.append((nx,ny))
                
        if len(stack) - origin_stack >= 2: # 경로가 3가지 이상으로 갈 수 있는 경우
            alphabet = matrix[x][y]
            times = len(stack) - origin_stack
            branch.append((alphabet,times))
            #breakpoint()
                
        if origin_stack == len(stack): # DFS 더 이상 진행하지 못하는 경우
            
            # 최대 길이 업데이트:
            if len(alpha) > max_length:
                max_length = len(alpha)
            
            alphabet,times = branch.pop()
            #breakpoint()
            
            if times != 0:
                while True:
                    last = alpha.pop()
                    
                    if last == alphabet:
                        break
                times -= 1
                
                if times != 0:
                    branch.append((alphabet, times))
                    alpha.append(alphabet)
                    
            if times == 0 : # branch가 없는 경우 -> 이전 branch로 옮겨야 함
                try:
                    alphabet,times = branch.pop()
                    while True:
                        last = alpha.pop()
                        
                        if last == alphabet:
                            break
                    times -= 1
                    
                    branch.append((alphabet, times))
                    alpha.append(alphabet)
                except:
                    continue
                    
    return max_length    
            
            
            
print(dfs(0,0))
            