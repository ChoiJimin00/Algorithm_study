import sys
input = sys.stdin.readline

def dfs(n,idx):
    if n == M:
        answer.add(' '.join(value))
        return 
    
    for i in range(idx, N):
        value.append(str(nums[i]))
        dfs(n+1, i+1)
        value.pop()
        
        
if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    
    value = []
    answer = set()
    
    dfs(0,0)
    
    answer = list(answer)
    answer.sort()
    for a in answer:
        print(a)