import sys
input = sys.stdin.readline

def dfs(idx):
    if len(tmp) == 6:
        print(*tmp)
        return 
    
    for i in range(idx, cnt):
        tmp.append(nums[i])
        dfs(i+1)
        tmp.pop()
        

if __name__ == '__main__':
    
    while True:
        nums = list(map(int,input().split()))
        cnt = nums[0]
        nums = nums[1:]
        
        if cnt == 0:
            break
        else:
            tmp = []
            dfs(0)
            print()