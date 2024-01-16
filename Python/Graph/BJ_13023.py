import sys
input = sys.stdin.readline

N,M = map(int,input().split())

adj_list = [[] for i in range(N)]

for i in range(M):
    a, b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visit = [False]*N
ans = False

def DFS(s, depth):
    global ans
    visit[s] = True

    if depth >= 4:
        ans = True
        return

    for next in adj_list[s]:
        if not visit[next]:
            DFS(next, depth+1)
            visit[next] = False

for i in range(N):
    DFS(i, 0)
    visit[i] = False
    if ans:
        break
print(1 if ans else 0)
