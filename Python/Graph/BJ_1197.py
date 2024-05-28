import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        return find(parent[n])
    return parent[n]

def union(n1,n2):
    n1 = find(n1)
    n2 = find(n2)
    
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2

def kruskal(graph):
    result = 0
    
    for n1,n2,w in graph:
        if find(n1) != find(n2):
            union(n1,n2)
            result += w
            
    return result


if __name__ == '__main__':
    V,E = map(int, input().split())
    
    parent = [0]*(V+1)
    for i in range(V+1):
        parent[i] = i
    
    graph = []
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        graph.append([n1,n2,w])
    graph.sort(key=lambda x:x[2])
    
    print(kruskal(graph))