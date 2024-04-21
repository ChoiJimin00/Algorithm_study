import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    # 우선순위 큐로 dijkstra 알고리즘 구현 - 비용(cost)을 우선순위 index로 사용
    q = []
    heapq.heappush(q,(0,start))
    
    distance = [INF]*(N+1)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[1:]
    

if __name__ == '__main__':
    N,M,X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a,b,c = map(int, input().split())
        graph[a].append([b,c])
        
    start = X
    path = dijkstra(start)
    
    for i in range(1, N+1):
        if i == X :
            continue
        path[i-1] += dijkstra(i)[X-1]
        
    print(max(path))