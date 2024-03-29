import sys
input = sys.stdin.readline

def BinarySearch(arr,key):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high)//2
        
        if key < arr[mid]:
            high = mid-1
        elif key > arr[mid]:
            low = mid+1
        elif key == arr[mid]:
            if high == mid:
                break
            high = mid
    
    if key == arr[mid]:
        return mid
    else:
        return -1

if __name__ == '__main__':
    N, M = map(int,input().split())
    A = sorted([int(input()) for _ in range(N)])
    
    for _ in range(M):
        B = int(input())
        print(BinarySearch(A,B))