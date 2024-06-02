import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    
    coordi = []
    for _ in range(N):
        coordi.append(list(map(int, input().split())))
    coordi.append(coordi[0])
    
    x,y = 0,0
    for i in range(N):
        x += coordi[i][0] * coordi[i+1][1]
        y += coordi[i][1] * coordi[i+1][0]
    
    print(round(abs((x-y)/2),1))