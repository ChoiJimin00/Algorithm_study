import sys
input = sys.stdin.readline

def dfs():
    if len(num) == M:
        print(*num)
        return 
    
    for i in range(1, N+1):
        num.append(i)
        dfs()
        num.pop()
    
if __name__ == '__main__':
    N,M = map(int, input().split())
    
    num = []
    dfs()