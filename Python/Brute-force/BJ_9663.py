import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
row = [0]*N

def chk_attack(x):
    # 상하좌우, 대각선에 퀸이 있는지 체크
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i): # 같은 행에 퀸이 있거나, 대각선에 퀸이 있는 경우
            return True
    return False
        
def dfs(start):
    global cnt 
    
    if start == N :
        cnt += 1
    
    else:
        for i in range(N):
            #[start, i]에 퀸을 놓음
            row[start] = i
            if not chk_attack(start):
                dfs(start+1)

dfs(0)
print(cnt)