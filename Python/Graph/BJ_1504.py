import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(edges, n1, n2): 
    ## 1) 1 -> n1까지 최소경로
    start = 1
    distance = [INF]*(N+1)
    q = []
    dist = 0
    heapq.heappush(q,(dist,start)) # 우선순위(거리), 노드 값
    distance[start] = dist
    
    while q : 
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in edges[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    
    if distance[n1] == 1e9: return 1e9
    d1 = distance[n1]
    
    
    ## 2) n1 -> n2까지 최소경로
    start = n1
    distance = [INF]*(N+1)
    q = []
    dist = 0
    heapq.heappush(q,(dist,start))
    distance[start] = dist
    
    while q : 
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in edges[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
                
    if distance[n2] == 1e9: return 1e9
    d2 = distance[n2]
    
    ## 3) n2 -> n까지 최소경로
    start = n2
    distance = [INF]*(N+1)
    q = []
    dist = 0
    heapq.heappush(q,(dist,start))
    distance[start] = dist
    
    while q : 
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in edges[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    
    if distance[N] == 1e9: return 1e9
    d3 = distance[N]
    
    return d1+d2+d3


if __name__ == '__main__':
    N,E = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        edges[n1].append([n2,w])
        edges[n2].append([n1,w])
    n1, n2 = map(int, input().split())
    
    result = min(dijkstra(edges,n1,n2), dijkstra(edges,n2,n1))
    if result >= 1e9:
        print(-1)
    else:
        print(result)