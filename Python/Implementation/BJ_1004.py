import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        x1, y1, x2, y2 = list(map(int, input().split()))
        
        n = int(input())
        cnt = 0
        
        for _ in range(n):
            x,y,r = list(map(int, input().split()))
            dist1 = (x1-x)**2 + (y1-y)**2
            dist2 = (x2-x)**2 + (y2-y)**2
            squ_r = r**2
            
            if squ_r > dist1 and squ_r > dist2:
                continue
            elif squ_r > dist1: 
                cnt += 1
            elif squ_r > dist2: 
                cnt += 1
                
        print(cnt)