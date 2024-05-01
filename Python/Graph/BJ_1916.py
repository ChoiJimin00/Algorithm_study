import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(start, end):
    dist = [INF]*(N+1)
    q = []
    heapq.heappush(q, [0, start])
    dist[start] = 0
    
    while q:
        weight, node = heapq.heappop(q)
        
        if dist[node] < weight:
            continue
        
        for adj_n, adj_w in graph[node]:
            cost = weight + adj_w
            if dist[adj_n] > cost:
                dist[adj_n] = cost
                heapq.heappush(q, [cost, adj_n])
                
    return dist[end]


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        n1, n2, w = map(int, input().split())
        graph[n1].append([n2, w])
        
    start, end = map(int, input().split())
    
    print(dijkstra(start, end))