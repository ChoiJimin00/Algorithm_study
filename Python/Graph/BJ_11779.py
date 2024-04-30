import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(edges, start, end):
    q = []
    heapq.heappush(q,[0,start])
    distance = [INF]*(n+1)
    distance[start] = 0
    prev = [0]*(n+1)
    
    while q:
        weight, node = heapq.heappop(q)
        
        if distance[node] < weight:
            continue
        
        for adj_n, adj_w in edges[node]:
            cost = adj_w + weight
            if cost < distance[adj_n]:
                distance[adj_n] = cost
                prev[adj_n] = node
                
                heapq.heappush(q,[cost,adj_n])
              
    path = [end]
    v = end
    while v != start:
        v = prev[v]
        path.append(v)
    path.reverse()

    print(distance[end])
    print(len(path))
    print(*path)
    

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    edges = [[] for _ in range(n+1)]
    
    for _ in range(m):
        n1,n2,w = map(int,input().split())
        edges[n1].append([n2,w])
        
    start, end = map(int, input().split())
    dijkstra(edges, start, end)