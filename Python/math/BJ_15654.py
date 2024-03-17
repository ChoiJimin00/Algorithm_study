import sys
from itertools import permutations
input = sys.stdin.readline

N,M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()

for i in permutations(num,M):
    for j in range(M):
        print(i[j], end=' ')
    print()