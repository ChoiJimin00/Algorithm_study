import sys
input = sys.stdin.readline


def bitonic_list():
    ascend = [0]*len(num)
    descend = [0]*len(num)
    
    for i in range(len(num)):
        tmp = 0 
        
        for j in range(i):
            if num[j] < num[i]:
                if tmp < ascend[j]+1:
                    tmp = ascend[j]+1
                    
        ascend[i] = tmp
        
    for i in range(len(num)-1,-1,-1):
        tmp = 0
        
        for j in range(len(num)-1,i,-1):
            if num[j] < num[i]:
                if tmp < descend[j]+1:
                    tmp = descend[j]+1
                    
        descend[i] = tmp
            
    for i in range(len(num)):
        ascend[i] += descend[i]
        
    return max(ascend)+1
                
        
if __name__ == '__main__':
    N = int(input())
    num = list(map(int, input().split()))
    
    print(bitonic_list())