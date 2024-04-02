import sys
input = sys.stdin.readline

def cnt_eight(L,R):
    while len(L) != len(R):
        L = '0' + L
    
    cnt = 0
    for i in range(len(L)):
        if L[i] == '8' and R[i] == '8':
            cnt += 1
        elif L[i] == R[i]:
            continue
        else: 
            break
            
    return cnt
            
if __name__ == '__main__':
    L,R = map(str,input().split())
    print(cnt_eight(L,R))