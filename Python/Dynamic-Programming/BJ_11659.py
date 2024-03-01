import sys
input = sys.stdin.readline

N,M = map(int, input().split())
num = [0]+list(map(int, input().split()))

for i in range(1, N+1):
    num[i] = num[i-1]+num[i]
    
for _ in range(M):
    i, j = map(int, input().split())
    print(num[j]-num[i-1])