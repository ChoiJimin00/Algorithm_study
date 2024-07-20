import sys
input = sys.stdin.readline

def chk(i,j,k):
    if k == '<':
        return i<j
    else:
        return i>j


def dfs(result):
    global min_val, max_val
    
    if len(result) == k+1:
        if min_val == '':
            min_val = result
        else:
            max_val = result
        return 
    
    for i in range(10):
        if not visited[i]:
            if len(result) == 0 or chk(result[-1],str(i),sign[len(result)-1]):
                visited[i] = True
                dfs(result+str(i))
                visited[i] = False
            
                
if __name__ == '__main__':
    k = int(input())
    sign = list(input().split())
    
    min_val, max_val = '',''
    visited = [False]*10
    dfs('')
    
    print(max_val)
    print(min_val)