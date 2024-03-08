# BFS로 풀음 - 참고 블로그 : https://velog.io/@dark6ro/%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global parent
    global adj_list
    
    que = deque()
    que.append(1) # 1이 rootnode
    
    while que:
        n1 = que.popleft()
        
        for n2 in adj_list[n1]:
            if parent[n2] == 1:
                continue
            if parent[n2] == n2:
                parent[n2] = n1
                que.append(n2)    

if __name__ == '__main__':
    N = int(input())
    parent = list(range(N+1))
    adj_list = [[] for _ in range(N+1)]
    
    for _ in range(N-1):
        n1,n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
        
    bfs()
    
    for i in range(2,N+1):
        print(parent[i])