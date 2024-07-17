import sys
input = sys.stdin.readline

def dfs(times):
    if times == M : 
        print(*tmp)
        return 
    
    for i in range(0, N):
        tmp.append(nums[i])
        dfs(times+1)
        tmp.pop()

if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    
    tmp = []
    dfs(0)