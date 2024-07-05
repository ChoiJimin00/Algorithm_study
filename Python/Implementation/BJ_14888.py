import sys
input = sys.stdin.readline

def dfs(n, temp):
    global max_val, min_val
    
    if n == N-1:
        max_val = max(temp, max_val)
        min_val = min(temp, min_val)
        return 
    
    if oper[0] != 0:
        oper[0] -= 1
        dfs(n+1, temp + nums[n+1])
        oper[0] += 1
        
    if oper[1] != 0:
        oper[1] -= 1
        dfs(n+1, temp - nums[n+1])
        oper[1] += 1
        
    if oper[2] != 0:
        oper[2] -= 1
        dfs(n+1, temp * nums[n+1])
        oper[2] += 1
    
    if oper[3] != 0:
        oper[3] -= 1
        dfs(n+1, int(temp/nums[n+1]))
        oper[3] += 1
        

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    oper = list(map(int, input().split()))
    
    max_val, min_val = -1e9, 1e9
    dfs(0,nums[0])
    
    print(max_val)
    print(min_val)