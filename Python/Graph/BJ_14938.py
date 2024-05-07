import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

def bfs(start,n,m,node_val):
    dist = [INF]*(n+1)
    q = deque()
    q.append([start,0])
    dist[start] = 0
    
    while q : 
        node, weight = q.pop()
        
        for adj_n, adj_w in graph[node]:
            cost = weight + adj_w
            if dist[adj_n] > cost:
                dist[adj_n] = cost
                q.append([adj_n, cost])
    
    item = 0
    for i in range(1,n+1):
        if dist[i] <= m :
            item += node_val[i-1]
    return item


if __name__ == '__main__':
    n,m,r = map(int, input().split())
    node = list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        n1,n2,w = map(int, input().split())
        graph[n1].append([n2,w])
        graph[n2].append([n1,w])
        
    items = []
    for i in range(1,n+1):
        items.append(bfs(i,n,m,node))
        
    print(max(items))