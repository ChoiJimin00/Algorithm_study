import sys
input = sys.stdin.readline

def min_house():
    global house
    
    for i in range(1,len(house)):
        for j in range(3):
            house[i][j] += min(house[i-1][:j] + house[i-1][j+1:])
    
    return min(house[-1])

if __name__ == '__main__':
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]
    print(min_house())