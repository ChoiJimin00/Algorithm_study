import sys
input = sys.stdin.readline
# 1. 시작 정점(1)에서 임의의 정점가지 거리를 구하여 가장 먼 거리를 구함
# 2. 1에서 찾은 가장 먼 거리를 시작 지점으로 하여 가장 긴 거리를 찾음 

def get_diameter(start, tree):
    visited = [0]*(N+1)
    
    max_dist = 0
    node = start
    
    stack = [[start, 0]]
    while stack:
        v, distance = stack.pop()
        visited[v] = 1
        
        for adj_v, dist in tree[v]:
            if visited[adj_v] == 0:
                stack.append([adj_v, dist+distance])
                new_dist = distance + dist
            
                if max_dist < new_dist:
                    max_dist = new_dist
                    node = adj_v
                
    return [node, max_dist]


if __name__ == '__main__':
    N = int(input())
    
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        p, c, w = map(int,input().split())
        tree[p].append((c,w))
        tree[c].append((p,w))
    
    node, dist = get_diameter(1,tree)
    print(get_diameter(node,tree)[1])