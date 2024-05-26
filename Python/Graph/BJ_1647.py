import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a        
    else:
        parent[a] = b
        

if __name__ == '__main__':
    N,M = map(int, input().split())
    
    parent = [0]*(N+1)
    for i in range(N+1):
        parent[i] = i
       
    graph = [] 
    for _ in range(M):
        h1,h2,w = map(int, input().split())
        graph.append([h1,h2,w])
        
    graph.sort(key=lambda x:x[2])
    
    result = 0
    max_cost = 0
    for edge in graph:
        start, end, cost = edge
        
        if find(start) != find(end):
            union(start, end)
            result += cost
            max_cost = max(cost, max_cost)
    
    print(result - max_cost)