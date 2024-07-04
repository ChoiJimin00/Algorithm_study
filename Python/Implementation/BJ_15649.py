import sys
input = sys.stdin.readline

def dfs():
    if len(stack) == M :
        print(*stack)
        return
        
    for i in range(1,N+1):
        if visited[i]:
            continue
        
        visited[i] = True
        stack.append(i)
        
        dfs()
            
        visited[i] = False
        stack.pop()


if __name__ == '__main__':
    N,M = map(int, input().split())
    stack = []
    visited = [False]*(N+1)  # 중복 제거
    dfs()