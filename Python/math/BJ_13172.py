import sys
input = sys.stdin.readline
MOD = 1000000007

def calc(n,x):
    if x == 1:
        return n
    v = calc(n, x//2)
    if x%2 == 0:
        return v*v%MOD
    else:
        return v*v*(n%MOD)

if __name__ == '__main__':
    M = int(input())
    
    result = 0
    for _ in range(M):
        n,s = map(int, input().split())
        rn = calc(n, MOD-2)
        result = (result + rn*s%MOD)%MOD
    
    print(result)