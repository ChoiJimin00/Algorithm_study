import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    maxDP = arr
    minDP = arr
    
    for _ in range(N-1):
        arr = list(map(int, input().split()))
        maxDP = [arr[0]+max(maxDP[:2]), arr[1]+max(maxDP[:]), arr[2]+max(maxDP[1:])]
        minDP = [arr[0]+min(minDP[:2]), arr[1]+min(minDP[:]), arr[2]+min(minDP[1:])]
        
    print(max(maxDP), min(minDP))