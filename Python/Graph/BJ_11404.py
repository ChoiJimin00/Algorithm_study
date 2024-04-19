import sys
input = sys.stdin.readline

def floyd(n,edges):
    
    ## 그래프 초기화
    map = [[1e9]*n for _ in range(n) ]
    
    for e in edges:
        map[e[0]-1][e[1]-1] = min(map[e[0]-1][e[1]-1],e[2])
        
    ## 그래프 shortest path update
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    map[i][j] = 0
                    continue
                map[i][j] = min(map[i][k] + map[k][j], map[i][j])
    
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1e9:
                map[i][j] = 0
                           
    return map

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    edges = [list(map(int, input().split())) for _ in range(m)]
    
    map = floyd(n,edges)
    for m in map:
        print(*m)