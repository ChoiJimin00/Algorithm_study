import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    global edges
    distance = [INF]*(N+1)
    distance[start] = 0
    
    for i in range(1,N+1):
        for j in range(1, N+1):
            for next, cost in edges[j]:
                if distance[next] > distance[j] + cost:
                    distance[next] = distance[j] + cost
                    if i == N: # N번째 반복에서 갱신되는 값이 있으면 negative cycle 존재함
                        return True
    return False
                    

if __name__ == '__main__':
    TC = int(input())
    
    for _ in range(TC):
        N,M,W = map(int, input().split())
        edges = [[] for _ in range(N+1)]
        for _ in range(M):
            S,E,T = map(int, input().split())    
            edges[S].append([E,T])
            edges[E].append([S,T])
        for _ in range(W):
            S,E,T = map(int, input().split())
            edges[S].append([E,(-1)*T])
            
        if bellman_ford(1):
            print('YES')
        else:
            print('NO')