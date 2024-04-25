import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    
    visited = [-1]*(V+1)
    visited[start] = 0
    
    max_len = [0, 0] 
    
    while q:
        node, dist = q.popleft()
        
        for adj_n, adj_d in graph[node]:
            if visited[adj_n] == -1:
                cur_dist = dist + adj_d
                
                q.append((adj_n, cur_dist))
                visited[adj_n] = cur_dist
                
                if max_len[1] < cur_dist:
                    max_len[0] = adj_n
                    max_len[1] = cur_dist
        
    return max_len


if __name__ == '__main__':
    V = int(input())
    graph = [[] for _ in range(V+1)]
    
    for _ in range(V):
        tree = list(map(int, input().split()))
        node = tree[0]
        idx = 1
        while tree[idx] != -1:
            adj_n, adj_d = tree[idx], tree[idx+1]
            graph[node].append((adj_n, adj_d))
            idx += 2
            
    radius, _ = bfs(1) 
    print(bfs(radius)[1])