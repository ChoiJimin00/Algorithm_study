import sys
input = sys.stdin.readline

def sort_times(height):
    
    sorted = []
    result = 0
    for h in height:
        sorted.append(h)
        for i in range(len(sorted)):
            if sorted[i] > h :
                result += 1
        sorted.sort()
    return result
        
        
if __name__ == '__main__':
    P = int(input())
    
    for _ in range(P):
        height = list(map(int, input().split()))
        print(height[0], sort_times(height[1:]))