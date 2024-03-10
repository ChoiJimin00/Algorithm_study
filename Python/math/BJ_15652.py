from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline


# 방법 1) combinations_with_replacement 라이브러리 이용
def combi(N,M):
    N = [i for i in range(1,N+1)]
    for i in combinations_with_replacement(N,M):
        result = ''
        for r in i:
            result += (str(r) +' ')
                   
        print(result)
    return

# 방법 2) dfs 방법 이용
def dfs(start):
    global N
    global M
    global num_list
    
    if len(num_list) == M:
        print(' '.join(map(str,num_list)))
        return
        
    for i in range(start, N+1):
        num_list.append(i)
        dfs(i)
        num_list.pop()

    
if __name__ == '__main__':
    N,M = map(int,input().split())
    #combi(N,M)
    num_list = []
    dfs(1)