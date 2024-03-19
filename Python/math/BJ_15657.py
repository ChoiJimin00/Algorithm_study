import sys
from itertools import combinations
from itertools import combinations_with_replacement
input = sys.stdin.readline

if __name__ == '__main__':
    N,M = map(int, input().split())
    
    num = list(map(int, input().split()))
    num.sort()
    
    
    for i in combinations_with_replacement(num, M):
        for j in range(len(i)):
            print(i[j],end=' ')
        print()