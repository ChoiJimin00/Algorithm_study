import sys
import bisect
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    
    a = int(input())
    an = list(map(int, input().split()))
    
    b = int(input())
    bn = list(map(int, input().split()))
    
    # 누적합 (prefix)
    ann, bnn = [],[]
    for i in range(a):
        for j in range(i+1, a+1):
            #ann[sum(an[i:j])] += 1
            ann.append(sum(an[i:j]))
    for i in range(b):
        for j in range(i+1, b+1):
            #bnn[sum(bn[i:j])] += 1
            bnn.append(sum(bn[i:j]))

    ann.sort()
    bnn.sort()
    
    result = 0
    for i in range(len(ann)):
        tmp = T - ann[i]
        left = bisect.bisect_left(bnn, tmp)
        right = bisect.bisect_right(bnn, tmp)
        result += (right-left)
        
    print(result)