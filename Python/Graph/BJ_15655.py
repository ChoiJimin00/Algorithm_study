import sys
input = sys.stdin.readline

def dfs(idx, times):
    if times == M:
        print(*tmp)
        return 
    
    for i in range(idx+1, N):
        tmp.append(nums[i])
        dfs(i,times+1)
        tmp.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    
    tmp = []
    dfs(-1,0)