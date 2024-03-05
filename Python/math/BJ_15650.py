import sys
from itertools import combinations
input = sys.stdin.readline

def combi(n,m):
    n = [i for i in range(1,n+1)]
    comb = combinations(n,m)
    
    for co in comb:
        result = ''
        for i in co:
            result += (str(i)+' ')
            
        print(result)
    
    return 

if __name__ == '__main__':
    N,M = map(int, input().split())
    combi(N,M)