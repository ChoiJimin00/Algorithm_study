import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N,M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

result = list(set([v for v in combinations_with_replacement(num, M)]))
result.sort()

for v in result:
    for i in range(len(v)):
        print(v[i], end=' ')
    print()